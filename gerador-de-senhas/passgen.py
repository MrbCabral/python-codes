#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from random import choice
from argparse import ArgumentParser

def tokensGen(options):
  tokens = ''
  if ('l' in options): # minúsculas
    tokens += 'abcdefghijklmnopqrstuvwxyz'
  if ('u' in options): # maiúsculas
    tokens += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if ('d' in options): # decimais
    tokens += '1234567890'
  if ('p' in options): # pontuação
    tokens += '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
  return tokens


def passwordGen(lenght, options='ludp'):
  tokens = tokensGen(options)
  password = ''.join(choice(tokens) for i in range(lenght))
  return password

parser = ArgumentParser(description = "Gerador de senhas.")
parser.add_argument("--lenght", dest="lenght", type=int, default=10,
                          help="Quantidade de caracteres da senha gerada.")
parser.add_argument("--types", dest="types", default='ludp', required=False,
                          help="Caracteres geradores da senha.\
                            l - letras minúsculas\
                            u - letras maiúsculas\
                            d - números decimais\
                            p - pontuação")
args = parser.parse_args()

print(passwordGen(args.lenght,args.types))