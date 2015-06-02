#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Drew Brokke
# Copyright (c) 2015 Drew Brokke
#
# License: MIT
#

"""This module exports the CheckSourceFormatting plugin class."""

from SublimeLinter.lint import NodeLinter, util


class CheckSourceFormatting(NodeLinter):

    """Provides an interface to check-source-formatting."""

    syntax = ('javascript', 'html', 'css', 'velocity', 'freemarker', 'java server pages (jsp)', 'sass')
    cmd = 'check_sf @ --no-color'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'^.+?(?P<line>\d+): (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    comment_re = r'\s*/[/*]'

