#!/usr/bin/python3

""" An autokey implementation, for fun purpose
    Copyright (C) 2022 Louis Lacoste

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. """

import argparse  # For the script to be able to parse arguments
import string  # To get the list of ASCII letters


def generate_tabula_recta():
    """ Function to generate a tabula recta.
    Return: a tabula recta in form of a dictionnary of dictionnaries
        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
      ----------------------------------------------------
    A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
    C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
    D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
    E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
    F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
    G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
    H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
    I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
    J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
    K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
    L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
    M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
    N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
    O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
    P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
    Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
    R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
    S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
    T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
    U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
    V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
    W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
    X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
    Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
    Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
    """
    # Retrieving the alphabet letters
    alphabetLetters = string.ascii_uppercase

    # Filling all the rows
    dictTabulaRecta = {rowLetter: {} for rowLetter in alphabetLetters}
    for index, rowLetter in enumerate(alphabetLetters):
        # Adding the shifted letters at the beginning of the sequence
        currentLettersSequence = alphabetLetters[index:] + \
            alphabetLetters[:index-26]
        dictTabulaRecta[rowLetter] = {columnLetter: currentLetter for columnLetter, currentLetter in zip(
            alphabetLetters, currentLettersSequence)}
    return dictTabulaRecta


def pretty_tabula_display():
    tabulaRecta = generate_tabula_recta()
    print(" "*4 + ' '.join(string.ascii_uppercase))
    print(" "*3 + "-"*2*26)
    for rowLetter, columnLetter in tabulaRecta.items():
        print(f"{rowLetter} | {' '.join(columnLetter.values())}")

def encrypt(clearMessage, key, isAutoKey):
  tabulaRecta = generate_tabula_recta()
  encryptedMessage = ""

  lenClearMessage = len(clearMessage)

  if isAutoKey:
    key = key + clearMessage
  
  repeatedKey = key

  if len(repeatedKey) < lenClearMessage:
    # If the key is smaller than the message we repeat it enough
    repeatedKey = repeatedKey * (lenClearMessage//len(key) + 1)
  
  # The key is trimmed to match the message size
  repeatedKey = repeatedKey[:lenClearMessage]

  for index, letter in enumerate(clearMessage):
    encryptedMessage += tabulaRecta[letter][repeatedKey[index]]
  return encryptedMessage

def decrypt(encryptedMessage, key, isAutoKey):
  tabulaRecta = generate_tabula_recta()
  decryptedMessage = ""
  workKey = key
  workEncryptedMessage = encryptedMessage
  if isAutoKey:
    # lenKey = len(key)

    # # We need to decrypt the first part of the encrypted message using the key
    # decryptedFirstPart = decrypt(encryptedMessage[:lenKey], key, False)
    # decryptedMessage = decryptedFirstPart
    while len(workEncryptedMessage) > 0:

      # We use the current work key to decrypt the next part
      decryptedPart = decrypt(workEncryptedMessage[:len(workKey)], workKey, False)
      decryptedMessage += decryptedPart

      # Our new workKey is the decrypted part
      workKey = decryptedPart

      # The new work encrypted message is shortened by the size of the step decrypted message
      workEncryptedMessage = workEncryptedMessage[len(decryptedPart):]
  else:
    # Not an autokey so we use the normal decrypting process
    lenEncryptedMessage = len(encryptedMessage)
    
    repeatedKey = key

    if len(repeatedKey) < lenEncryptedMessage:
      # If the key is smaller than the message we repeat it enough
      repeatedKey = repeatedKey * (lenEncryptedMessage//len(key) + 1)
    
    # The key is trimmed to match the message size
    repeatedKey = repeatedKey[:lenEncryptedMessage]

    for index, letter in enumerate(encryptedMessage):
      columnNumber = list(tabulaRecta[repeatedKey[index]].values()).index(letter)
      columnLetters = list(tabulaRecta[repeatedKey[index]].keys())
      decryptedMessage += columnLetters[columnNumber]
  return decryptedMessage


parser = argparse.ArgumentParser(
    usage="This script is used to encrypt and decrypt using the autokey method.")

# Arguments declaration
parser.add_argument("message", metavar="MESSAGE",
                    help="With no other flags, the message to encrypt. If the -d or --decrypt flag is provided, the message to decrypt")
parser.add_argument("key", metavar="KEY", help="The key used to encrypt or decrypt the message")
parser.add_argument("-d", "--decrypt", action="store_true", help="Enable the decrypt mode.")
parser.add_argument("-a", "--autokey", action="store_true", help="Enable the autokey mode.")

args = parser.parse_args()

# Processing the message and key to get rid of spaces and uppercase them
message = args.message.replace(" ", "").upper()
key = args.key.replace(" ", "").upper()

if args.decrypt:
  print("Decrypting:")
  print(decrypt(message, key, args.autokey))
else:
  print("Encrypting:")
  print(encrypt(message, key, args.autokey))