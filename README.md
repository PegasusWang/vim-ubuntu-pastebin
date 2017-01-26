# vim-ubuntu-pastebin

## Usage:
Paste your current vim bufffer content to http://paste.ubuntu.com/, support many filetypes, support vim compiled with python or python3. Just in your vim and execute `:Pastebin`, then vim will print pasted url, you can open it in your browser(automaticlly when use desktop). Note this plugin shares your file public, if your file is private you may use gist.github or scp command.

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

If you want to learn write vim plugin use python, see this youtube radio [Writing Vim plugins with Python](https://www.youtube.com/watch?v=vMAeYp8mX_M)
[vim-plugin-starter-kit](https://github.com/JarrodCTaylor/vim-plugin-starter-kit)


## 中文简介:
如果你和我一样记性不好老是记不住scp命令怎么使的，可以试试直接安装这个插件之后在vim里执行 `:Pastebin` ，代码会自动贴到http://paste.ubuntu.com然后自动打开浏览器。
如果你对怎么用python写vim插件有兴趣可以参考以上油管视频链接或者我的博客。
