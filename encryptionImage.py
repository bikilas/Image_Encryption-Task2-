from PIL import Image
import numpy as np
import random

# Encryption function with per-pixel random key
def encrypt_image(input_image_path, output_image_path):
    try:
        # Load the image
        img = Image.open(input_image_path)
        img_array = np.array(img, dtype=np.uint8)
        
        # Generate a random key for each pixel (the same shape as the image array)
        np.random.seed(42)  # Set a seed for reproducibility, change or remove for randomness
        random_key = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)
        
        # Encrypt by XORing the image array with the random key
        encrypted_array = np.bitwise_xor(img_array, random_key)
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")
        
        # Optionally return the random key for decryption
        return random_key
    
    except FileNotFoundError:
        print(f"Error: File not found at {input_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Decryption function using the saved random key
def decrypt_image(encrypted_image_path, output_image_path, random_key):
    try:
        # Load the encrypted image
        img = Image.open(encrypted_image_path)
        img_array = np.array(img, dtype=np.uint8)
        
        # Decrypt by XORing the encrypted array with the random key
        decrypted_array = np.bitwise_xor(img_array, random_key)
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")
    
    except FileNotFoundError:
        print(f"Error: File not found at {encrypted_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_image_path = r'D:\ENCRYPTION\Image_Encryption-Task2-\image\iman.jpg'  # Path to the original image
encrypted_image_path = r'D:\ENCRYPTION\Image_Encryption-Task2-\encrypted_iman.png'  # Path where encrypted image will be saved
decrypted_image_path = r'D:\ENCRYPTION\Image_Encryption-Task2-\decrypted_iman.png'  # Path where decrypted image will be saved

# Encrypt the image with random pixel-level keys
random_key = encrypt_image(input_image_path, encrypted_image_path)

# Decrypt the image using the saved random key
decrypt_image(encrypted_image_path, decrypted_image_path, random_key)
