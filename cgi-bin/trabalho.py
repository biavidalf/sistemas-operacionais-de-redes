#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import cgitb
import funcoes

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

cgitb.enable()

funcoes.trab()

print('<div id="principal">')
funcoes.trabalho()
funcoes.lateral()
print('</div>')

funcoes.footer()
