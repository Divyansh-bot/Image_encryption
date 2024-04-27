
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

def encrypt_image(key, input_image_path, output_image_path):
    with open(input_image_path, "rb") as f:
        input_image = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    padded_image_data = pad(input_image, AES.block_size)
    encrypted_image_data = cipher.encrypt(padded_image_data)
    with open(output_image_path, "wb") as f:
        f.write(encrypted_image_data)

def decrypt_image(key, input_image_path, output_image_path):
    with open(input_image_path, "rb") as f:
        encrypted_image_data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_image_data = cipher.decrypt(encrypted_image_data)
    unpadded_image_data = unpad(decrypted_image_data, AES.block_size)
    with open(output_image_path, "wb") as f:
        f.write(unpadded_image_data)

def main():
    key = get_random_bytes(16)
    input_image_path = input("Enter the path of the input image file: ")
    output_image_path = input("Enter the path for the output image file: ")
    encrypt_image(key, input_image_path, output_image_path)
    print("Image encrypted successfully.")

    decrypt_choice = input("Do you want to decrypt the image (yes/no)? ").lower()
    if decrypt_choice == "yes":
        input_encrypted_image_path = input("Enter the path of the encrypted image file: ")
        output_decrypted_image_path = input("Enter the path for the decrypted image file: ")
        decrypt_image(key, input_encrypted_image_path, output_decrypted_image_path)
        print("Image decrypted successfully.")

if __name__ == "__main__":
    main()
