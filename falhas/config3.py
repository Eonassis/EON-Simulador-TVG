#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sementes random 
RANDOM_SEED = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

#tempo maximo de simulacao
MAX_TIME = 10000000  

#ERLANG_MIN = 300
ERLANG_MIN = 550

#ERLANG_MAX = 380
ERLANG_MAX = 850

#pabrao 20
ERLANG_INC = 50 

#quantidade de repeticoes padrao 10
REP = 10

#numero de requisicoes padrao 100.000 100000
NUM_OF_REQUESTS = 100000

#tramanho das bandas >>>>>> MEXER NO CODIGO AO ALTERAR BANDAS >>>>
#BANDWIDTH = [100, 150, 200, 250, 300, 350, 400]
BANDWIDTH = [10]

#classes de trafego
CLASS_TYPE = [1, 2, 3]

#divisao do trafego por classes
CLASS_WEIGHT = [0.15, 0.25, 0.60]

#topologia
TOPOLOGY = 'usa'

##### aki aumenta o tarfego, reduzindo o tempo por requisicao ########
#tempo por requisicao padrao 1.0 gera 50% block, 2.0 gera 13% block, 0.5 gera 60% block 
HOLDING_TIME = 1 / 2


#quantidade slot Eon 400
SLOTS = 400

#tamanho do slot ghz
SLOT_SIZE = 12.5

#N_PATH 15
N_PATH = 50

#tempo inicio do desastre 3600
TIME_CASC_INI = 7.500

#tempo entre os desastres 
TIME_CASC = 3.600

#duracao do desastre
TIME_DESAS = 43.200

#pontos de falha = pontoA, pontoB, tempo para falhar 
			 #[[6,9,1],[9,11,3],[7,9,6],[9,12,6],[9,10,9],[6,7,9],[11,12,9]]
LINK_POINTS = [[7,8,TIME_CASC_INI],
			   [9,10,TIME_CASC_INI],
			   [5,8,TIME_CASC_INI+(TIME_CASC)],
			   [8,10,TIME_CASC_INI+(TIME_CASC*2)],
			   [10,13,TIME_CASC_INI+(TIME_CASC*3)],
			   [7,9,TIME_CASC_INI+(TIME_CASC*3)],
			   [9,12,TIME_CASC_INI+(TIME_CASC*3)]]

#pontos de falha = no, tempo [[4,2], [2,5]]
NODE_POINTS = [[8,TIME_CASC_INI+(TIME_CASC*3)+0.1]]

#alpha 
ALPHA = [1 , 0.5 , 0.4, 0.3, 0.1]
