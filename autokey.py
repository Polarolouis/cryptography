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

import argparse # For the script to be able to parse arguments
import string # To get the list of ASCII letters


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
    dictTabulaRecta = {rowLetter:{} for rowLetter in alphabetLetters}
    for index, rowLetter in enumerate(alphabetLetters):

      # Adding the shifted letters at the beginning of the sequence
      currentLettersSequence = alphabetLetters[index:] + alphabetLetters[:index-26]
      dictTabulaRecta[rowLetter] = {columnLetter:currentLetter for columnLetter, currentLetter in zip(alphabetLetters, currentLettersSequence)}
    return dictTabulaRecta

def pretty_tabula_display():
  tabulaRecta = generate_tabula_recta()
  print(" "*4 + ' '.join(string.ascii_uppercase))
  print(" "*3 + "-"*2*26)
  for rowLetter, columnLetter in tabulaRecta.items():
    print(f"{rowLetter} | {' '.join(columnLetter.values())}")

parser = argparse.ArgumentParser(usage="This script is used to encrypt and decrypt using the autokey method.")

# Arguments declaration
parser.add_argument("message", metavar="MESSAGE", help="With no other flags, the message to encrypt. If the -d or --decrypt flag is provided, the message to decrytp")
parser.add_argument("-d", "--decrypt",help="Enable the decrypt flag")


parser.parse_args()