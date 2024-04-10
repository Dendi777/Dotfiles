-- coc-nvim --
local opts = {silent = true, noremap = true, expr = true, replace_keycodes = false}
vim.keymap.set("i", "<TAB>", 'coc#pum#visible() ? coc#pum#confirm() : v:lua.check_back_space() ? "<TAB>" : coc#refresh()', opts)
vim.keymap.set("n", "gd", "<Plug>(coc-definition)", {silent = true})

-- neotree --
vim.keymap.set('n', '<C-n>', '<Cmd>Neotree toggle<CR>')

-- nvim windows --
local map = vim.api.nvim_set_keymap
map('n', '<C-Left>', '<C-w>h', {noremap = true})
map('n', '<C-Right>', '<C-w>l', {noremap = true})
map('n', '<C-Down>', '<C-w>j', {noremap = true})
map('n', '<C-Up>', '<C-w>k', {noremap = true})
