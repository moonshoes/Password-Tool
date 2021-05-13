import tkinter as tk
from tkinter.font import BOLD, Font


class EmptyOptionsException(Exception):
    pass


class View():
    def __init__(self, master):
        self.intialFrame = tk.Frame(master, padx=10, pady=10)
        self.label = tk.Label(self.intialFrame, text="Hello, what would you like to do?")
        self.generationButton = tk.Button(self.intialFrame, text="Generate a password", padx=2, pady=2)
        self.validationButton = tk.Button(self.intialFrame, text="Validate a password", padx=2, pady=2)

        self.show()

        self.generationView = GenerationView(master)
        self.validationView = ValidationView(master)

    def show(self):
        self.intialFrame.pack()
        self.label.pack(ipadx=5, ipady=5)
        self.generationButton.pack(side="left", padx=[0, 10])
        self.validationButton.pack(side="right")

    def showInitialView(self):
        self.hideGenerationView()
        self.hideValidationView()
        self.show()
    
    def showGenerationView(self):
        self.generationView.show()

    def showValidationView(self):
        self.validationView.show()

    def hideInitialView(self):
        self.intialFrame.forget()

    def hideGenerationView(self):
        self.generationView.resetFields()
        self.generationView.frame.forget()

    def hideValidationView(self):
        self.validationView.resetFields()
        self.validationView.frame.forget()


class GenerationView():
    def __init__(self, master):
        self.frame = tk.Frame(master, padx=10, pady=10)

        self.font = Font(self.frame, size=15)
        self.title = tk.Label(self.frame, text="Generate Password", font=self.font)

        self.insertionFrame = tk.Frame(self.frame)
        self.generatedPassword = tk.Label(self.frame, text="", pady=10)
        self.lengthLabel = tk.Label(self.insertionFrame, text="Password length:")
        self.entry = tk.Entry(self.insertionFrame)
        self.options = OptionsMenu(self.frame)
        self.buttonFrame = tk.Frame(self.frame)
        self.button = tk.Button(self.buttonFrame, text="Generate", padx=2, pady=2)
        self.backButton = tk.Button(self.buttonFrame, text="Back", padx=2, pady=2)

    def show(self):
        self.frame.pack()
        self.title.pack()
        self.generatedPassword.pack()
        self.insertionFrame.pack()
        self.lengthLabel.pack(side="left", fill="both", padx=[0, 5])
        self.entry.pack(side="right", fill="both")
        self.options.frame.pack()
        self.options.place()
        self.buttonFrame.pack()
        self.button.pack(side="left", padx=[0, 10])
        self.backButton.pack(side="right")
    
    def setNewPassword(self, password):
        passwordVar = tk.StringVar()
        passwordVar.set(password)
        self.generatedPassword.config(textvariable=passwordVar, fg="green")

    def resetFields(self):
        passwordVar = tk.StringVar()
        passwordVar.set("")
        self.generatedPassword.config(textvariable=passwordVar)
        self.entry.delete(0, tk.END)
        self.options.reset()


class ValidationView():
    def __init__(self, master):
        self.frame = tk.Frame(master, padx=10, pady=10)

        self.font = Font(self.frame, size=15)
        self.title = tk.Label(self.frame, text="Validate Password", font=self.font)

        self.passwordFeedback = tk.Label(self.frame, text="", pady=10)
        self.insertionFrame = tk.Frame(self.frame)
        self.passwordLabel = tk.Label(self.insertionFrame, text="Password:")
        self.entry = tk.Entry(self.insertionFrame)
        self.options = OptionsMenu(self.frame)
        self.buttonFrame = tk.Frame(self.frame)
        self.button = tk.Button(self.buttonFrame, text="Validate", padx=2, pady=2)
        self.backButton = tk.Button(self.buttonFrame, text="Back", padx=2, pady=2)

    def show(self):
        self.frame.pack()
        self.title.pack()
        self.passwordFeedback.pack()
        self.insertionFrame.pack()
        self.passwordLabel.pack(side="left", padx=[0, 5])
        self.entry.pack(side="right")
        self.options.frame.pack()
        self.options.place()
        self.buttonFrame.pack()
        self.button.pack(side="left", padx=[0, 10])
        self.backButton.pack(side="right")

    def setFeedback(self, feedback):
        feedbackVar = tk.StringVar()
        if not feedback:
            feedbackVar.set("Password is valid!")
            self.passwordFeedback.config(textvariable=feedbackVar, fg="green")
        else:
            feedbackText = "Password is invalid:"
            for fb in feedback:
                feedbackText += "\n- {}".format(fb)

            feedbackVar.set(feedbackText)
            
            self.passwordFeedback.config(textvariable=feedbackVar, fg="red")
    
    def resetFeedback(self):
        feedbackVar = tk.StringVar()
        feedbackVar.set("")
        self.passwordFeedback.config(textvariable=feedbackVar)

    def resetFields(self):
        self.resetFeedback()
        self.entry.delete(0, tk.END)
        self.options.reset()


class OptionsMenu():
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.lowercaseCBVar = tk.IntVar()
        self.uppercaseCBVar = tk.IntVar()
        self.digitCBVar = tk.IntVar()
        self.specialCBVar = tk.IntVar()

        self.label = tk.Label(self.frame, text="Check all options that apply (please select at least 1 option):")
        self.lowercaseCheckButton = tk.Checkbutton(self.frame, text="Must contain at least one lowercase letter", variable=self.lowercaseCBVar)
        self.uppercaseCheckButton = tk.Checkbutton(self.frame, text="Must contain at least one uppercase letter", variable=self.uppercaseCBVar)
        self.digitCheckButton = tk.Checkbutton(self.frame, text="Must contain at least one digit", variable=self.digitCBVar)
        self.specialCheckButton = tk.Checkbutton(self.frame, text="Must contain at least one special character", variable=self.specialCBVar)
    
    def place(self):
        self.label.pack(anchor="w", pady=[10, 0])
        self.lowercaseCheckButton.pack(anchor="w")
        self.uppercaseCheckButton.pack(anchor="w")
        self.digitCheckButton.pack(anchor="w")
        self.specialCheckButton.pack(anchor="w")

    def retrieveCheckedOptions(self):
        options = []
        if self.lowercaseCBVar.get():
            options.append("lowercase")
        if self.uppercaseCBVar.get():
            options.append("uppercase")
        if self.digitCBVar.get():
            options.append("digit")
        if self.specialCBVar.get():
            options.append("special")

        if not options:
            raise EmptyOptionsException("No options selected. Please select at least 1 option.")

        return options

    def reset(self):
        self.lowercaseCBVar.set(0)
        self.uppercaseCBVar.set(0)
        self.digitCBVar.set(0)
        self.specialCBVar.set(0)