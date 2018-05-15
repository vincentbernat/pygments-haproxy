# -*- coding: utf-8 -*-
# Copyright (c) 2018 Vincent Bernat <bernat@luffy.cx>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Keyword, Punctuation
from pygments.token import String, Number, Name


class HAProxyLexer(RegexLexer):
    name = "HAProxy"
    aliases = ["haproxy"]
    tokens = {
        'root': [
            (r'#.*?\n', Comment.Singleline),

            # Sections
            (r'(global|default)\n', Keyword.Namespace),
            (r'(listen|frontend|backend|ruleset)(\s+)(\w*)(\n)',
             bygroups(Keyword.Namespace, Text, Name, Text)),

            # Generic tokens
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r'(\[)'
             r'([a-f0-9]{4}:[a-f0-9:]+)(:\d+\.\d+\.\d+\.\d+)?'
             r'(\]:)(\d+)',
             bygroups(Punctuation, Number, Number, Punctuation,
                      Number)),  # IPv6 with port
            (r'[a-f0-9]{4}:[a-f0-9:]+(:\d+\.\d+\.\d+\.\d+)?(/\d+)?',
             Number),  # IPv6 or IPv6 CIDR
            (r'(\d+\.\d+\.\d+\.\d+)(:)(\d+)',
             bygroups(Number, Punctuation, Number)),  # IPv4 with port
            (r'\d+\.\d+\.\d+\.\d+(/\d+)?', Number),  # IPv4 or IPv4 CIDR

            # First word on each line is a directive name
            (r'^([ \t]*)([-\w]+)',
             bygroups(Text, Name.Function)),

            # Remaining...
            (r'[ \t]+', Text),
            (r'\n', Text),
            (r'\d+', Number),
            (r'\S+', Text),
        ],
    }
