# -*- coding: utf-8 -*-

import os
import requests
import webbrowser

try:
    from urllib import urlencode    # py2
except ImportError:
    from urllib.parse import urlencode   # py3


PASTEBIN_SUPPORT_TYPE = frozenset([
    'text',
    'Cucumber',
    'abap',
    'ada',
    'ahk',
    'antlr',
    'antlr-as',
    'antlr-cpp',
    'antlr-csharp',
    'antlr-java',
    'antlr-objc',
    'antlr-perl',
    'antlr-python',
    'antlr-ruby',
    'apacheconf',
    'applescript',
    'as',
    'as3',
    'aspx-cs',
    'aspx-vb',
    'asy',
    'basemake',
    'bash',
    'bat',
    'bbcode',
    'befunge',
    'blitzmax',
    'boo',
    'c',
    'c-objdump',
    'cfm',
    'cfs',
    'cheetah',
    'clojure',
    'cmake',
    'coffee-script',
    'common-lisp',
    'console',
    'control',
    'cpp',
    'cpp-objdump',
    'csharp',
    'css',
    'css+django',
    'css+erb',
    'css+genshitext',
    'css+mako',
    'css+myghty',
    'css+php',
    'css+smarty',
    'cython',
    'd',
    'd-objdump',
    'delphi',
    'diff',
    'django',
    'dpatch',
    'duel',
    'dylan',
    'erb',
    'erl',
    'erlang',
    'evoque',
    'factor',
    'felix',
    'fortran',
    'gas',
    'genshi',
    'genshitext',
    'glsl',
    'gnuplot',
    'go',
    'gooddata-cl',
    'groff',
    'haml',
    'haskell',
    'html',
    'html+cheetah',
    'html+django',
    'html+evoque',
    'html+genshi',
    'html+mako',
    'html+myghty',
    'html+php',
    'html+smarty',
    'html+velocity',
    'hx',
    'hybris',
    'ini',
    'io',
    'ioke',
    'irc',
    'jade',
    'java',
    'js',
    'js+cheetah',
    'js+django',
    'js+erb',
    'js+genshitext',
    'js+mako',
    'js+myghty',
    'js+php',
    'js+smarty',
    'jsp',
    'lhs',
    'lighty',
    'llvm',
    'logtalk',
    'lua',
    'make',
    'mako',
    'maql',
    'mason',
    'matlab',
    'matlabsession',
    'minid',
    'modelica',
    'modula2',
    'moocode',
    'mupad',
    'mxml',
    'myghty',
    'mysql',
    'nasm',
    'newspeak',
    'nginx',
    'numpy',
    'objdump',
    'objective-c',
    'objective-j',
    'ocaml',
    'ooc',
    'perl',
    'php',
    'postscript',
    'pot',
    'pov',
    'prolog',
    'properties',
    'protobuf',
    'py3tb',
    'pycon',
    'pytb',
    'python',
    'python3',
    'ragel',
    'ragel-c',
    'ragel-cpp',
    'ragel-d',
    'ragel-em',
    'ragel-java',
    'ragel-objc',
    'ragel-ruby',
    'raw',
    'rb',
    'rbcon',
    'rconsole',
    'rebol',
    'redcode',
    'rhtml',
    'rst',
    'sass',
    'scala',
    'scaml',
    'scheme',
    'scss',
    'smalltalk',
    'smarty',
    'sourceslist',
    'splus',
    'sql',
    'sqlite3',
    'squidconf',
    'ssp',
    'tcl',
    'tcsh',
    'tex',
    'text',
    'trac-wiki',
    'v',
    'vala',
    'vb.net',
    'velocity',
    'vim',
    'xml',
    'xml+cheetah',
    'xml+django',
    'xml+erb',
    'xml+evoque',
    'xml+mako',
    'xml+myghty',
    'xml+php',
    'xml+smarty',
    'xml+velocity',
    'xquery',
    'xslt',
    'yaml',
])


def post_buffer_to_ubuntu_pastebin(buffer, filetype, open_in_borwser=True):
    """ post current file buffer content to http://paste.ubuntu.com/
    and return url.

    Args:
        buffer (vim.current.buffer)
        filetype (str)

    Returns:
        url (str)
    """
    lines = os.linesep.join(list(buffer))
    url = 'http://paste.ubuntu.com/'
    data = urlencode(
        {
            'poster': os.environ.get('USER', 'anonymous'),
            'syntax': filetype if filetype in PASTEBIN_SUPPORT_TYPE else 'text',
            'content': lines
        }
    ).encode('utf-8')
    r = requests.post(url, data=data, allow_redirects=True)
    if open_in_borwser:
        webbrowser.open_new_tab(r.url)
    return r.url
