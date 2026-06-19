import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sounddevice as sd


def sum_of_digits(text):
    sum = 0
    
    for character in text:
        digit = ord(character)
        sum += digit
    return sum


def dec_to_bin(dec):
    res = ''  
    while dec > 0:
        res = str(dec & 1) + res
        dec >>= 1
    return res


def digits_to_array(n):
    arr = []
    
    for bit in str(n):
        arr.extend(bit)

    signalArr = np.array(arr)

    return signalArr


def print_digital_signal(bitArr):
    bit_rate = 1000       
    Tb = 1 / bit_rate 

    y = bitArr + [bitArr[-1]]
    t = np.arange(len(y)) * Tb

    plt.figure(figsize=(10, 4))
    plt.step(t, y, where='post', linewidth=2, color='#1f77b4')

    plt.ylim(-0.2, 1.2)        
    plt.yticks([0, 1])         
    plt.xlabel('Time (s)')
    plt.ylabel('State')
    plt.title(f'Digital Signal (bit rate: {bit_rate} bps, Tb = {Tb} s)')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()


def main():
    print('Enter any text:')
    initialText = input()
    decimalSum = sum_of_digits(initialText)
    binaryNumber = dec_to_bin(decimalSum)
    bitArray = digits_to_array(binaryNumber)
    print_digital_signal(bitArray)



main()






