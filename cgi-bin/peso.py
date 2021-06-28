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
                <h2><span class="titulo">Peso em KG para LBS:</span></h2>
                <form action="" method="post">
                    <div>
                        <label>Massa em quilos:</label>
                        <input type="text" name="p" placeholder="3.5">
                    </div>
                    <input type="submit" value="Converter">
                </form>
        </div>


""")
#
form = cgi.FieldStorage()
br = form.getvalue("p")
if br:
    print(f"""
                <br>
                <h2><span class="titulo">Resultado:</span></h2>
                {functions.peso(float(br))}
    """)

print("""
    </div>
</div>
""")

funcoes.lateral()
print('</div>')

funcoes.footer()
