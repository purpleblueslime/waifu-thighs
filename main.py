from flask import Flask, Response
from os import walk
from random import choice

app = Flask('waifu-thighs')

@app.get('/')
def func():
  for root, d, imgs in walk('./imgs/'):
    img = choice(imgs)

  rbee = open(f'./imgs/{img}', 'rb') # rbee 
  return Response(rbee, mimetype='image/png')

# Un-comment this if not using vercel ;)
# app.run() 