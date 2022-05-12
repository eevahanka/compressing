import random
import string
import huffman
import zlw
import file_acces
import time
import os
from statistics import mean

textf = "speed.txt"
hufff = "speed.huff"
lii = "liirum.txt"
zlwf = "speed.zlw"
many = 100000
mult = 10

def make_string(length):
    letters = string.printable
    stringg = ''.join(random.choice(letters) for i in range(length))
    return stringg

def huff_speed():
    speeds = []
    for i in range(mult):
        random_string = make_string(many)
        start = time.time()
        huffman.huffman(random_string)
        end = time.time()
        speeds.append(end-start)
    return speeds

def liirum():
    liiru = file_acces.open_file(lii)
    comp_string = huffman.huffman(liiru)
    file_acces.write_bytes(hufff, comp_string)
    s1= file_acces.get_file_size(lii)
    s2 = file_acces.get_file_size(hufff)
    smaller = compare(s1, s2)
    os.remove(hufff)
    print("original size: ", s1)
    print("huff")
    print(smaller)
    comp_string = zlw.zlw(liiru)
    file_acces.write_bytes(zlwf, comp_string)
    s2 = file_acces.get_file_size(zlwf)
    smaller = compare(s1, s2)
    os.remove(zlwf)
    print("lzw")
    print(smaller)

def zlw_good():
    amounts  = []
    for i in range(10):
        random_string = make_string(many)
        comp_string = zlw.zlw(random_string)
        file_acces.create_file(textf, random_string)
        file_acces.write_bytes(zlwf, comp_string)
        s1= file_acces.get_file_size(textf)
        s2 = file_acces.get_file_size(zlwf)
        smaller = compare(s1, s2)
        amounts.append(smaller)
        os.remove(textf)
        os.remove(zlwf)
    return amounts

def huff_good():
    amounts  = []
    for i in range(10):
        random_string = make_string(many)
        comp_string = huffman.huffman(random_string)
        file_acces.create_file(textf, random_string)
        file_acces.write_bytes(hufff, comp_string)
        s1= file_acces.get_file_size(textf)
        s2 = file_acces.get_file_size(hufff)
        smaller = compare(s1, s2)
        amounts.append(smaller)
        os.remove(textf)
        os.remove(hufff)
    return amounts

def get_average_speed(speeds:list):
    return mean(speeds)

def zlw_speed():
    speeds = []
    for i in range(10):
        random_string = make_string(many)
        start = time.time()
        zlw.zlw(random_string)
        end = time.time()
        speeds.append(end-start)
    return speeds

def compare(original_size, new_size):
    smaller_prosents = (original_size - new_size)/original_size *100
    return smaller_prosents

def multis():
    ghh = huff_speed()
    print("huff speed")
    print(ghh)
    print(get_average_speed(ghh))
    ghh = zlw_speed()
    print("zlw speed")
    print(ghh)
    print(get_average_speed(ghh))
    ghh = huff_good()
    print("huff amount")
    print(ghh)
    print(get_average_speed(ghh))
    ghh = zlw_good()
    print("zlw amount")
    print(ghh)
    print(get_average_speed(ghh))

if __name__ == "__main__":
    liirum()
    



