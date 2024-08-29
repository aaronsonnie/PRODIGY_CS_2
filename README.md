# PRODIGY_CS_2
Image Encryption Tool Using Pixel Manipulation
This Python program allows you to encrypt and decrypt images by manipulating the pixels through basic mathematical operations.

# Features
Encryption: Encrypts an image by applying a mathematical operation to each pixel.
Decryption: Decrypts the image by reversing the mathematical operation applied during encryption.
Flexible Input: Works with any image file format supported by the Pillow library.

# How It Works
The program first reads an image and converts it into a NumPy array to facilitate pixel manipulation. For encryption, a mathematical operation (such as addition modulo 256) is applied to each pixel using a specified key. For decryption, the reverse operation (subtraction modulo 256) is applied using the same key, effectively restoring the original image.

# Requirements
Python 3.x
Pillow library
