haha
" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages available in Debian.
runtime! debian.vim

set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
" vim git plugin
Plugin 'tpope/vim-fugitive'
" its a colorscheme
Plugin 'https://github.com/freeo/vim-kalisi'
" folds for python
Plugin 'tmhedberg/SimpylFold'
"fuzzy file search activated by -
Plugin 'kien/ctrlp.vim'
" syntax checking
Plugin 'scrooloose/syntastic'
Plugin 'flazz/vim-colorschemes'  " nice colors!


call vundle#end()
filetype plugin indent on
" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous

" options, so any other options should be set AFTER setting 'compatible'.
"set compatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
"set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"if has("autocmd")
"  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
"endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"if has("autocmd")
"  filetype plugin indent on
"endif
let mapleader = ","

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.
set showmatch		" Show matching brackets.
set ignorecase		" Do case insensitive matching
set smartcase		" Do smart case matching
set incsearch		" Incremental search
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
"set mouse=a		" Enable mouse usage (all modes)

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif

"tabspaces
set tabstop=4
set shiftwidth=4
set expandtab
set smarttab

set backspace=indent,eol,start " allow backspacing over everything in insert mode
set autoindent " always set autoindenting on
set copyindent " copy the previous indentation on autoindenting
set number " always show line numbers

set hlsearch " highlight search terms
nmap <f3> :set number! number?<cr> 
"toggle line numbers by F3

set history=1000 " remember more commands and search history
set undolevels=1000 " use many muchos levels of undo
set nobackup " do not keep backup files, it's 70's style cluttering
set noswapfile " do not write annoying intermediate swap files,

nnoremap <leader>q :q<CR>
nnoremap <leader>w :w<CR>

"ctrl + j/k/l/h for switching windows instead of ctrl-w + h/j/k/l
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" When editing a file, always jump to the last cursor position
autocmd BufReadPost *
\ if ! exists("g:leave_my_cursor_position_alone") |
\ if line("'\"") > 0 && line ("'\"") <= line("$") |
      \ exe "normal g'\"" |
      \ endif |
      \ endif

nnoremap ; :
:command W w
:command WQ wq
:command Wq wq
:command Q q
:command Qa qa
:command QA qa

set wildmenu
set wildmode=full

" hide matches on <leader>space
nnoremap <leader><space> :nohlsearch<cr>

inoremap jj <ESC>
nnoremap <F2> :set invpaste paste?<CR>
set pastetoggle=<F2>
set showmode

set background=dark
"colorscheme kalisi
colorscheme wombat256
map - :CtrlP<cr>
iabbrev adn and
iabbrev pdb import ipdb; ipdb.set_trace()
iabbrev jlog console.log "<text here>"
let g:ctrlp_custom_ignore =  '\v\.(js|svg|txt|json|html|styl|md)$'
:set textwidth=80
:set colorcolumn=+1

" For simplyfold plugin
" show docstrings as preview
let g:SimpleFold_docstring_preview = 1

"syntax checking
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0


"give us 256 colors
set term=screen-256color
set autoread
