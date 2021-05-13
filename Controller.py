import tkinter as tk
from tkinter.messagebox import showerror
import Model as m
import View as v

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.model = m.Model()
        self.view = v.View(self.root)
        self.root.title("Password Tool")

        self.view.generationButton.config(command=self.showGenerationView)
        self.view.validationButton.config(command=self.showValidationView)

        self.view.generationView.button.config(command=self.generatePassword)
        self.view.generationView.backButton.config(command=self.showInitialView)

        self.view.validationView.button.config(command=self.validatePassword)
        self.view.validationView.backButton.config(command=self.showInitialView)
    
    def run(self):
        self.root.mainloop()

    def showGenerationView(self):
        self.view.hideInitialView()
        self.view.showGenerationView()
        self.root.title("Generate Password")
    
    def showValidationView(self):
        self.view.hideInitialView()
        self.view.showValidationView()
        self.root.title("Validate Password")
    
    def showInitialView(self):
        self.view.showInitialView()
        self.root.title("Password Tool")

    def generatePassword(self):
        try:
            self.model.setOptions(self.view.generationView.options.retrieveCheckedOptions())
            self.model.setLength(int(self.view.generationView.entry.get()))
            self.model.generateValidPassword()
            self.view.generationView.setNewPassword(self.model.getPassword())
        except ValueError:
            showerror("Error", message="Invalid length: please input a number.")
        except m.InvalidOptionException as e:
            showerror("Error", message=e)
        except v.EmptyOptionsException as e:
            showerror("Error", message=e)


    def validatePassword(self):
        try:
            password = self.view.validationView.entry.get()
            if password != "":
                self.model.setOptions(self.view.validationView.options.retrieveCheckedOptions())
                self.model.setPassword(password)
                self.model.validatePassword()
                self.view.validationView.setFeedback(self.model.getFeedback())
                self.model.resetFeedback()
            else:
                showerror("Error", message="Invalid password: please input a password.")
        except m.InvalidOptionException as e:
            showerror("Error", message=e)
        except v.EmptyOptionsException as e:
            showerror("Error", message=e)