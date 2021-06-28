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
                <h2><span class="titulo">Numeração de calçado BR para EUA:</span></h2>
                <form action="" method="post">
                      <input type="radio" id="1" name="variacao" value="1" checked>
                      <label class="radinho" for="1">Masculino</label> 
                      <input type="radio" id="2" name="variacao" value="2">
                      <label class="radinho" for="2">Feminino</label><br>
                    <div>
                        <label>Digite a numeração brasileira:</label>
                        <input type="text" name="r" placeholder="38">
                    </div>
                    <input type="submit" value="Converter">
                </form>
        </div>


""")
#
form = cgi.FieldStorage()
br = form.getvalue("r")
fm = form.getvalue("variacao")
if br:
    print(f"""
                <br>
                <h2><span class="titulo">Resultado:</span></h2>
                {functions.sapato(int(fm), int(br))}
    """)

print("""
    </div>
</div>
""")

funcoes.lateral()
print('</div>')

funcoes.footer()
