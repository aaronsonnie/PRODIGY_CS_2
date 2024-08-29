# PRODIGY_CS_2

# Image Encryption Tool using Pixel Manipulation
You can perform operations like applying a basic mathematical operation to each pixel to achieve image encryption.This Python program allows you to encrypt and decrypt images using pixel manipulation techniques. 

# Features
Encryption: Encrypts an image by applying a mathematical operation to each pixel.
Decryption: Decrypts an image by reversing the applied mathematical operation.
Flexible Input: Accepts any image file supported by Pillow.

# How It Works
The program reads an image and converts it into a NumPy array for pixel manipulation. During encryption, a mathematical operation (addition modulo 256) is applied to each pixel using a specified key. During decryption, the inverse operation (subtraction modulo 256) is applied using the same key to restore the original image.

# Requirements
Pillow library
Python 3.x

