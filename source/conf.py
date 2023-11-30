# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '我的HPC文档'
copyright = '2023, houys2'
author = 'houys2'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx-prompt',
    'sphinx_copybutton',
    # 'sphinx_substitution_extensions',
    'sphinx.ext.autosectionlabel',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_immaterial'
]

# 解析文件格式
source_suffix = {'.rst': 'restructuredtext',
                 '.txt': 'markdown',
                 '.md': 'markdown'
                 }

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_static_path = ['_static']





# -- HTML theme settings -----------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_immaterial'
html_favicon = 'favicon.png'
html_title = 'LICO超算平台用户手册 Documentation'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logos.png'

# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the repo location to get a badge with stats
    'repo_url': 'https://10.240.214.64/',
    'repo_name': 'LiCO HPC',

    # Visible levels of the global TOC; -1 means unlimited
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,


    # Do not download google fonts
    "font": False,

    # Light and dark mode
    'palette': [{ 'media': '(prefers-color-scheme: light)',
                 'scheme': 'default',
                 "primary": "blue",
                 "accent": "blue",
                 'toggle': {
                    'icon': 'material/lightbulb-outline',
                    'name': 'Switch to dark mode',
                 },
                },
                { 'media': '(prefers-color-scheme: dark)',
                  'scheme': 'slate',
                  "primary": "blue",
                  "accent": "blue",
                  'toggle': {
                    'icon': 'material/lightbulb',
                    'name': 'Switch to light mode',
                 },
                },
               ]
}

# Add doc prefix for atutlabeling
autosectionlabel_prefix_document = True

# Image Match Order for HTML Builder
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg',
    'image/jpg'
]

# Image Match Order for HTML Builder
from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = [
    'image/pdf',
    'image/png',
    'image/jpeg',
    'image/jpg'
]


rst_prolog = """
.. |my_variable| replace:: "我的变量"
"""

# LaTeX PDF customization
latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    'fncychap' : '\\usepackage[Bjornstrup]{fncychap}',

    # Additional stuff for the LaTeX preamble.
    # Reference: http://sychen.logdown.com/posts/2015/03/05/sphinx-pdf-chinese-support
    'preamble': r"""
    \usepackage{xeCJK}
    \usepackage{fontspec}
    \usepackage{indentfirst} % 中文首行缩进
	  \let\cleardoublepage\clearpage
    \setlength{\parindent}{2em}
    \setCJKmainfont{Adobe Song Std}
    \setCJKmonofont[Scale=0.9]{Adobe Heiti Std}
    \setCJKfamilyfont{song}{Adobe Song Std}
    \setCJKfamilyfont{sf}{Adobe Song Std}
    \XeTeXlinebreaklocale "zh"          % 設定斷行演算法為中文
    \XeTeXlinebreakskip = 0pt plus 1pt  % 設定中文字距與英文字距
    """,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}
