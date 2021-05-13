import string
import random

class InvalidOptionException(Exception):
    pass

class Model():
    def __init__(self):
        self.password = ""
        self.length = 0
        self.options = []
        self.feedback = []

    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password

    def setLength(self, length):
        self.length = length
    
    def setOptions(self, options):
        self.options = options
    
    def getFeedback(self):
        return self.feedback

    def resetFeedback(self):
        self.feedback = []

    def generateValidPassword(self):
        self.generatePassword()
        while(self.validatePassword()):
            self.resetFeedback()
            self.generatePassword()
        return self.password

    def generatePassword(self):
        population = []

        for option in self.options:
            if option == "uppercase":
                population += string.ascii_uppercase
            elif option == "lowercase":
                population += string.ascii_lowercase
            elif option == "digit":
                population += string.digits
            elif option == "special":
                population += string.punctuation
            else:
                raise InvalidOptionException("Invalid option.")

        self.password = ''.join(random.choices(population, k=self.length))
    
    def validatePassword(self):
        for option in self.options:
            if option == "uppercase":
                if not self.passwordContains(string.ascii_uppercase):
                    self.feedback.append("Password does not contain an uppercase letter")
            elif option == "lowercase":
                if not self.passwordContains(string.ascii_lowercase):
                    self.feedback.append("Password does not contain a lowercase letter")
            elif option == "digit":
                if not self.passwordContains(string.digits):
                    self.feedback.append("Password does not contain a digit")
            elif option == "special":
                if not self.passwordContains(string.punctuation):
                    self.feedback.append("Password does not contain a special character")
            else:
                raise InvalidOptionException("Invalid option.")
            
        return self.feedback
    
    def passwordContains(self, list):
        contains = False
        i = 0

        while(not contains and i < len(self.password)):
            if self.password[i] in list:
                contains = True
            i += 1
        
        return contains