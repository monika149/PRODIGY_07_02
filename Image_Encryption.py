print('----ENCYRPT AND DECRYPT THE IMAGES HERE----')

file_path = ''

# function to encrypt or decrypting the image
def manipulate_image(img, key, en_de_img):
    file = open(img, 'rb')
    image = file.read()
    file.close()
    image = bytearray(image)
    for i, j in enumerate(image):
        image[i] = j ^ key

    file = open(en_de_img, 'wb')
    file.write(image)
    file.close()



try:
    encrypt_or_decrypt = int(input("\n[*]Select: \n1.Encrypt \n2.Decrypt\n3.Exit\nEnter your choice: "))
    if (encrypt_or_decrypt == 1):
        key = int(input('Enter the key: '))
        file_path = input('Enter the file path: ')
        name_after_encrypt=input("Enter the path and name of the image with extension after encryption: ")
        manipulate_image(file_path,key,name_after_encrypt)
        print("Encrypted!!Kindly check the path you provided")

    elif (encrypt_or_decrypt == 2):
        key = int(input('Enter the key that was used to encrypt: '))
        file_path = input('Enter the file path : ')
        name_after_decrypt = input("Enter the path and name of the image with extension after decryption: ")
        manipulate_image(file_path, key, name_after_decrypt)
        print("Decrypted!!Kindly check the path you provided")
    elif (encrypt_or_decrypt == 3):
        exit()
    else:
        print("Please enter valid input!!")

except ValueError:
        print('Enter a valid value')
except FileNotFoundError:
    print("Correct File path is not given or the target doesnt exists")