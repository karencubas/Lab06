def menu():
    print("Menu\n-------------\n"
          "1.Encode\n2.Decode\n3.Quit\n")

##Karen C. Cubas
def encode(original):
    encoded = ""
     ## Shift digits of original up by 3
    for char in original:
        if int(char) < 7:
           encoded += str(int(char) + 3)
        if int(char) >= 7:
           encoded += str(int(char) + 3 -10 )

    return encoded
def decode(encoded):
    ## Partner
    decoded = ""

    return decoded

if __name__ == '__main__' :

    while True:
       menu()

       option = int(input("Please enter an option: "))

       ## Encode password
       if option == 1:
           original = input("Please enter your password to encode: ")
           encoded = encode(original)
           print("Your password has been encoded and stored!\n")

       ## Decode password
       if option == 2:
           decoded = decode(encoded)
           print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")

       ## Quit program
       if option == 3:
           exit()
