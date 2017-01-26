" --------------------------------
" Add our plugin to the path
" --------------------------------

if !(has('python3') || has('python'))
    echo "Error: Required vim compiled with +python or +python3"
    finish
endif


if has('python3')
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Function(s)
" --------------------------------
function! Pastebin()
python3 << endOfPython


from vim_ubuntu_pastebin import post_buffer_to_ubuntu_pastebin
filetype = vim.eval('&filetype')
url = post_buffer_to_ubuntu_pastebin(vim.current.buffer, filetype)
print(url)

endOfPython
endfunction
endif


if has('python')
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Function(s)
" --------------------------------
function! Pastebin()
python << endOfPython


from vim_ubuntu_pastebin import post_buffer_to_ubuntu_pastebin
filetype = vim.eval('&filetype')
url = post_buffer_to_ubuntu_pastebin(vim.current.buffer, filetype)
print(url)

endOfPython
endfunction
endif


" --------------------------------
"  Expose our commands to the user
" --------------------------------
"
command! Example call Pastebin()
command! -nargs=0 Pastebin call Pastebin()
