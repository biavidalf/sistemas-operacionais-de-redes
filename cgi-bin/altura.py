#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import cgitb

import funcoes
import functions

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

cgitb.enable()

funcoes.conv()

print('<div id="principal">')
print("""
<div id="principal">
    <div id="postagens">

        <div class="postagem">
                <h2><span class="titulo">Altura de METROS para PÉS:</span></h2>
                <form action="" method="post">
                    <div>
                        <label>Comprimento em metros:</label>
                        <input type="text" name="m" placeholder="1.68">
                    </div>
                    <input type="submit" value="Converter">
                </form>
        </div>


""")
#
form = cgi.FieldStorage()
br = form.getvalue("m")
if br:
    print(f"""
                <br>
                <h2><span class="titulo">Resultado:</span></h2>
                {functions.comprimento(float(br))}.
    """)

print("""
    </div>
</div>
""")

funcoes.lateral()
print('</div>')

funcoes.footer()
