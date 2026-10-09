-- Pandoc Lua filter used by build_exam_sheets.py.
-- Turns the body of a sheet (.qmd) into compact LaTeX for the exam PDF:
--   level-2 heading          -> \sheetsection{...}
--   paragraph that is bold   -> \sheetlabel{...}   (name of a formula)
--   display formula          -> sheetformula environment; the formula is cut
--                               at every top-level \qquad so that its parts
--                               can wrap inside a narrow column
--   code block               -> fancyvrb Verbatim (small monospaced font)
--   pipe table               -> tabular / tabularx (longtable cannot be used
--                               inside multicols)
--   ::: {.sheet-wide} block  -> set across the full page width, outside
--                               the columns
-- The filter never changes the content of a formula or of a code line.

local function latex(blocks)
  local s = pandoc.write(pandoc.Pandoc(blocks), 'latex')
  return (s:gsub('%s+$', ''))
end

local function raw(s) return pandoc.RawBlock('latex', s) end

-- Cut a formula at \qquad, but not inside braces, \left...\right, or
-- \begin...\end.
local function split_formula(tex)
  local parts, depth, start, i, n = {}, 0, 1, 1, #tex
  while i <= n do
    local c = tex:sub(i, i)
    if c == '\\' then
      local name = tex:match('^%a+', i + 1)
      if name == nil then
        i = i + 2
      else
        if name == 'begin' or name == 'left' then
          depth = depth + 1
        elseif name == 'end' or name == 'right' then
          depth = depth - 1
        elseif name == 'qquad' and depth == 0 then
          parts[#parts + 1] = tex:sub(start, i - 1)
          start = i + 1 + #name
        end
        i = i + 1 + #name
      end
    else
      if c == '{' then depth = depth + 1 elseif c == '}' then depth = depth - 1 end
      i = i + 1
    end
  end
  parts[#parts + 1] = tex:sub(start)
  local out = {}
  for _, p in ipairs(parts) do
    p = p:gsub('^%s+', ''):gsub('%s+$', ''):gsub('%s*\n%s*', ' ')
    if p ~= '' then out[#out + 1] = '$\\displaystyle ' .. p .. '$' end
  end
  return out
end

local function only_display_math(inlines)
  local math = nil
  for _, x in ipairs(inlines) do
    if x.t == 'Math' and x.mathtype == 'DisplayMath' and math == nil then
      math = x
    elseif x.t ~= 'Space' and x.t ~= 'SoftBreak' then
      return nil
    end
  end
  return math
end

local function header(el)
  return raw('\\sheetsection{' .. latex({pandoc.Plain(el.content)}) .. '}')
end

local function para(el)
  if #el.content == 1 and el.content[1].t == 'Strong' then
    return raw('\\sheetlabel{' .. latex({pandoc.Plain(el.content[1].content)}) .. '}')
  end
  local math = only_display_math(el.content)
  if math then
    local parts = split_formula(math.text)
    return raw('\\begin{sheetformula}\n' ..
      table.concat(parts, '\\sheetsep\n') .. '\n\\end{sheetformula}')
  end
  for _, x in ipairs(el.content) do
    if x.t == 'Math' and x.mathtype == 'DisplayMath' then
      error('exam_sheet.lua: put every $$ formula in a paragraph of its own')
    end
  end
  return nil
end

local function codeblock(el)
  return raw('\\begin{Verbatim}\n' .. el.text .. '\n\\end{Verbatim}')
end

-- A column is "tight" when every body cell holds only code, symbols, and
-- punctuation. Tight columns keep their natural width, the others wrap.
-- In a full-width block no column wraps.
local function is_tight(blocks)
  local tight = true
  pandoc.walk_block(pandoc.Div(blocks), {
    Str = function(s) if s.text:match('%w') then tight = false end end
  })
  return tight
end

local function make_table(el, wide)
  local t = pandoc.utils.to_simple_table(el)
  local ncol = #t.aligns
  local tight, any_wrap = {}, false
  for j = 1, ncol do
    tight[j] = true
    for _, row in ipairs(t.rows) do
      if not is_tight(row[j]) then tight[j] = false end
    end
    if not tight[j] then any_wrap = true end
  end
  if wide then any_wrap = false end
  local spec = {}
  for j = 1, ncol do
    if tight[j] or not any_wrap then
      spec[j] = 'l'
    else
      spec[j] = '>{\\raggedright\\arraybackslash}X'
    end
  end
  local lines, head = {}, {}
  for j = 1, ncol do head[j] = '\\textbf{' .. latex(t.headers[j]) .. '}' end
  lines[#lines + 1] = table.concat(head, ' & ') .. ' \\\\ \\hline'
  for _, row in ipairs(t.rows) do
    local cells = {}
    for j = 1, ncol do cells[j] = latex(row[j]) end
    lines[#lines + 1] = table.concat(cells, ' & ') .. ' \\\\'
  end
  local colspec = '@{}' .. table.concat(spec, '') .. '@{}'
  local open, close
  if any_wrap then
    open = '\\begin{tabularx}{\\linewidth}{' .. colspec .. '}'
    close = '\\end{tabularx}'
  else
    open = '\\begin{tabular}{' .. colspec .. '}'
    close = '\\end{tabular}'
  end
  return raw('\\begin{sheettable}\n' .. open .. '\n' ..
    table.concat(lines, '\n') .. '\n' .. close .. '\n\\end{sheettable}')
end

local function convert(blocks, wide)
  return pandoc.walk_block(pandoc.Div(blocks), {
    Header = header,
    Para = para,
    CodeBlock = codeblock,
    Table = function(el) return make_table(el, wide) end,
  }).content
end

-- The body is set in columns. A top-level `::: {.sheet-wide}` block leaves
-- the columns, spans the page, and the columns start again after it.
function Pandoc(doc)
  local out, in_columns = {}, false
  local function columns(on)
    if on and not in_columns then
      out[#out + 1] = raw('\\begin{multicols}{\\sheetcolumns}')
    elseif in_columns and not on then
      out[#out + 1] = raw('\\end{multicols}')
    end
    in_columns = on
  end
  for _, block in ipairs(doc.blocks) do
    local wide = block.t == 'Div' and block.classes:includes('sheet-wide')
    columns(not wide)
    local source = wide and block.content or {block}
    for _, b in ipairs(convert(source, wide)) do out[#out + 1] = b end
  end
  columns(false)
  return pandoc.Pandoc(out, doc.meta)
end
