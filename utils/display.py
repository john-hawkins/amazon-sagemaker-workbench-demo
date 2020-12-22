# -*- coding: utf-8 -*-
"""
Set of helper functions for displaying files and data
"""

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import IPython

def display_file(myfile):
    """
      Open the named file and print it inside the notebook
    """
    with open(myfile) as f:
        code = f.read()

    formatter = HtmlFormatter()
    return IPython.display.HTML(
        '<style type="text/css">{}</style>{}'.format(
            formatter.get_style_defs('.highlight'),
            highlight(code, PythonLexer(), formatter)
        )
    )


