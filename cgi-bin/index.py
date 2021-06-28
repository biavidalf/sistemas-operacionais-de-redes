#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import cgitb
import funcoes

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

cgitb.enable()

funcoes.header()

print('<div id="principal">')
funcoes.index()
funcoes.lateral()
print('</div>')

funcoes.footer()
