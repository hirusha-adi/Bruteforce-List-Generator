#!/usr/bin/python3

import argparse
import itertools
import sys
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class BruteList:
    def __init__(self):
        self.__HELP__ = r"""usage: brutelist [-h] [-i] [-a] [-A] [-p] [-v] [-f FILE] [-l LENGTH]

options:
-h, --help            show this help message and exit
-i, --int             Use numbers (0-9)
-a, --alphabet        Use letters (a-z)
-A, --ALPHABET        Use letters (A-Z)
-p, --punctuation     32 special characters
-v, --verbose         Print every combination on screen
-f FILE, --file FILE  output to file
-l LEN, --length LEN  length of the password
        """

        self.PASSWORD = []
        self.CHARACTERS = ""
        self.inluce_int = None
        self.include_alphabet = None
        self.include_ALPHABET = None
        self.include_punctuation = None
        self.verbose = None
        self.filename = None
        self.length = None

    def getArgs(self):
        parser = argparse.ArgumentParser()

        # What to include
        parser.add_argument("-i", "--int",
                            help="Use numbers (0-9)",
                            action="store_true")
        parser.add_argument("-a", "--alphabet",
                            help="Use letters (a-z)",
                            action="store_true")
        parser.add_argument("-A", "--ALPHABET",
                            help="Use letters (A-Z)",
                            action="store_true")
        parser.add_argument("-p", "--punctuation",
                            help="32 special characters",
                            action="store_true")

        # Output methods
        parser.add_argument("-v", "--verbose",
                            help="Print every combination on screen",
                            action="store_true")
        parser.add_argument("-f", "--file",
                            help="output to file")
        parser.add_argument("-l", "--length",
                            help="length of the password")

        args = parser.parse_args()

        # Characters to include
        self.inluce_int = args.int
        self.include_alphabet = args.alphabet
        self.include_ALPHABET = args.ALPHABET
        self.include_punctuation = args.punctuation

        # Output method
        self.verbose = args.verbose
        self.filename = args.file

        # Length
        self.length = args.length

    def parseArgs(self):
        # Length check
        if self.length is None:
            print("\nerror: password length is not mentioned")
            sys.exit(self.__HELP__)

        # Output method check
        if (self.filename is None) and (self.verbose == False):
            print("\nerror: enter the output method")
            sys.exit(self.__HELP__)

        # Characters to include
        if (self.inluce_int == False) and (self.include_alphabet == False) and (self.include_ALPHABET == False) and (self.include_punctuation == False):
            print("\nerror: enter the characters you want to include")
            sys.exit(self.__HELP__)

        return True

    def generateCharacterSet(self):
        if self.inluce_int:
            self.CHARACTERS += digits
        if self.include_alphabet:
            self.CHARACTERS += ascii_lowercase
        if self.include_ALPHABET:
            self.CHARACTERS += ascii_uppercase
        if self.include_punctuation:
            self.CHARACTERS += punctuation

    def generateList(self):
        try:
            self.PASSWORD = [
                ''.join(i) for i in itertools.product(str(self.CHARACTERS), repeat=int(self.length))
            ]
        except Exception as e:
            sys.exit(e)

    def run(self):
        self.getArgs()
        self.parseArgs()
        self.generateList()
        print(self.PASSWORD)
        print(len(self.PASSWORD))


x = BruteList()
x.run()
