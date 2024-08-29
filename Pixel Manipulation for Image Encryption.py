pip install pillow

from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
  
    encrypted_array = (image_array + key) % 256
    
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    decrypted_array = (image_array - key) % 256
    
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

def main():
    choice = input("Type 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").lower()
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the key (an integer value): "))

    if choice == 'encrypt':
        encrypt_image(image_path, key)
    elif choice == 'decrypt':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
