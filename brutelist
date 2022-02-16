#!/usr/bin/python3

import argparse
import itertools
import os
import sys
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class BruteList:
    def __init__(self,
                 inluce_int: bool = None,
                 include_alphabet: bool = None,
                 include_ALPHABET: bool = None,
                 include_punctuation: bool = None,
                 verbose: bool = None,
                 filename: str = None,
                 length: int = None
                 ):

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
        self.inluce_int = inluce_int
        self.include_alphabet = include_alphabet
        self.include_ALPHABET = include_ALPHABET
        self.include_punctuation = include_punctuation
        self.verbose = verbose
        self.filename = filename
        self.length = length

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

    def makeFileIfNotExist(self):
        if not(str(self.filename) in os.listdir(os.getcwd())):
            with open(os.path.join(os.getcwd(), self.filename), "w", encoding="utf-8") as fmake:
                fmake.write("\n")
        return

    def saveToFile(self):
        if not(self.filename is None):
            self.makeFileIfNotExist()
            with open(os.path.join(os.getcwd(), self.filename), "a", encoding="utf-8") as fapnd:
                for line in self.PASSWORD:
                    fapnd.write(line + "\n")

    def displayPasswords(self):
        for password in self.PASSWORD:
            print(password)

    def startOutput(self):
        if not(self.filename is None):
            self.saveToFile()

        if not(self.verbose == False):
            self.displayPasswords()

    def runStandalone(self):
        self.getArgs()
        self.parseArgs()
        self.generateCharacterSet()
        self.generateList()
        self.startOutput()


if __name__ == "__main__":
    obj = BruteList()
    obj.runStandalone()
