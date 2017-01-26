# vim-ubuntu-pastebin

## Usage:
Paste your current vim bufffer content to http://paste.ubuntu.com/, support many filetypes, support vim compiled with python or python3. Just in your vim and execute `:Pastebin`, then vim will print pasted url, you can open it in your browser. Note this plugin shares your file public, if your file is private you may use gist.github or scp command.

- Post current buffer to http://paste.ubuntu.com/

    :Pastebin


## Installation

Required vim compiled with +python or +python3.

- pip install requests            # pip3 install requests

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/PegasusWang/vim-ubuntu-pastebin ~/.vim/bundle/vim-ubuntu-pastebin`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/PegasusWang/vim-ubuntu-pastebin'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/PegasusWang/vim-ubuntu-pastebin'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/PegasusWang/vim-ubuntu-pastebin'` to .vimrc
  - Run `:PlugInstall`

## Author
- PegasusWang
