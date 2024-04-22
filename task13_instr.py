#coding: utf-8
from ipaddress import *

network = ip_network('192.168.0.0/255.255.128.0') # создаем сеть

for ip in network: # прохожусь по ip адресу это сети
    print(int(ip)) # переводим в ip адрес в числовое значение в десятичную систему
    print(format(ip,"b"))               # print(bin(ip)[2:]) # переводим в ip адрес в числовое значение в двоичную систему
