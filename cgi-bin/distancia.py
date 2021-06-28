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
                <h2><span class="titulo">Distância em KM para MILHAS:</span></h2>
                <form action="" method="post">
                    <div>
                        <label>Distancia em km:</label>
                        <input type="text" name="km" placeholder="1.6">
                    </div>
                    <input type="submit" value="Converter">
                </form>
        </div>


""")
#
form = cgi.FieldStorage()
br = form.getvalue("km")
if br:
    print(f"""
                <br>
                <h2><span class="titulo">Resultado:</span></h2>
                {functions.distancia(float(br))} milhas
    """)

print("""
    </div>
</div>
""")

funcoes.lateral()
print('</div>')

funcoes.footer()
