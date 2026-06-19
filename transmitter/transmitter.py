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


def generate_digital_signal(bitArr):
    bit_rate = 100       
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


def generate_analog_wave(bitArr, bitRate, fCarr=1000, fSampling=44100):
    T = 1.0 / bitRate
    
    samplesPerBit = int(fSampling * T) 
    allSamples = len(bitArr) * samplesPerBit
    t = np.arange(allSamples) / fSampling

    wave = np.cos(2 * np.pi * fCarr * t)
    mappingBits = np.array([1 if int(b) == 0 else -1 for b in bitArr])
    modulatingSignal = np.repeat(mappingBits, samplesPerBit)
    modulatedSignal = wave * modulatingSignal

    plt.figure(figsize=(12, 4))
    plt.plot(t, modulatedSignal, color='#1f77b4', linewidth=1.5)
    
    for i in range(1, len(bitArr)):
        plt.axvline(x=i * T, color='red', linestyle='--', alpha=0.5)

    plt.title(f'Sygnał BPSK | Bity: {bitArr} | Bit Rate: {bitRate} bps')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def main():
    print('Enter any text:')
    initialText = input()
    decimalSum = sum_of_digits(initialText)
    binaryNumber = dec_to_bin(decimalSum)
    bitArray = digits_to_array(binaryNumber)
    generate_analog_wave(bitArray, 100)


main()






