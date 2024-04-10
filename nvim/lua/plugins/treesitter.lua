return {
  {
    "nvim-treesitter/nvim-treesitter",
    config = function()
      require'nvim-treesitter.configs'.setup {
        ensure_installed = { "lua", "vim", "vimdoc", "python", "c", "asm", "cpp", "rust", "go", "typescript", "javascript", "html", "css" },
        highlight = { enable = true, use_languagetree = true, },
        indent = { enable = true },
      }
    end,
  }
}
