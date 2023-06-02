import TXTtoMIDI
import tkinter as tk
from tkinter import filedialog
import os

"""UwU"""

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.__file = None
        self.ressource_directory = os.getcwd() + "\Ressources"
        self.geometry("403x403")
        self.title("Mid'Py - By EISE3")
        self.resizable(False, False)
        self.creer_style()
        self.ecran_accueil()

    def creer_style(self):
        bg = tk.PhotoImage(file=self.ressource_directory + "\image_background.png")
        self.bg_label = tk.Label(self, image=bg)
        self.bg_label.place(x=0, y=0)
        self.bg_label.image = bg

        self.iconbitmap(self.ressource_directory + "\image_favicon.ico")

    def ecran_accueil(self):

        self.label_bienvenue = tk.Label(self, text="Bienvenue", font=("Robotto", 35, "bold"), fg="white", bg="#ffcccc", borderwidth=5, relief="flat")
        self.bouton_convertir_txt = tk.Button(self, command=self.interface_conversion_txt,text="Convertir\nMatLab vers Midi", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_tuto = tk.Button(self, command=self.interface_tuto,text="Guide\nUtiliser le convertisseur", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)


        self.label_bienvenue.place(x=80, y=60)
        self.bouton_convertir_txt.place(x=100, y=190)
        self.bouton_tuto.place(x=100, y=270);

        self.bouton_convertir_txt.bind("<Enter>", func=lambda e: self.bouton_convertir_txt.config(
            background="#ffcccc"))
        self.bouton_convertir_txt.bind("<Leave>", func=lambda e: self.bouton_convertir_txt.config(
            background="#ff9999"))
        self.bouton_tuto.bind("<Enter>", func=lambda e: self.bouton_tuto.config(
            background="#ffcccc"))
        self.bouton_tuto.bind("<Leave>", func=lambda e: self.bouton_tuto.config(
            background="#ff9999"))

    def interface_conversion_txt(self):
        self.label_bienvenue.destroy()
        self.bouton_convertir_txt.destroy()
        self.bouton_tuto.destroy()

        self.bouton_fichier = tk.Button(self, command=self.choisir_file, text="Choisir le fichier\nà convertir", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_fichier.place(x=100, y=200);
        self.bouton_retour = tk.Button(self, command=self.detruire_txt,text="Retourner à l'accueil", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_retour.place(x=100, y=270);
        self.label_fichier = tk.Label(self, text="Aucun fichier sélectionné", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=4)
        self.label_fichier.place(x=100, y=80);

        self.bouton_retour.bind("<Enter>", func=lambda e: self.bouton_retour.config(
            background="#ffcccc"))
        self.bouton_retour.bind("<Leave>", func=lambda e: self.bouton_retour.config(
            background="#ff9999"))


    def detruire_txt(self):
        try:
            self.bouton_fichier.destroy()
        except AttributeError:
            None
        self.label_fichier.destroy()
        try:
            self.bouton_convertir.destroy()
        except AttributeError:
            None
        try:
            self.supp_convertion()
        except AttributeError:
            None
        self.ecran_accueil()

    def detruire_tuto(self):
        try:
            self.label_tuto.destroy()
        except AttributeError:
            None
        self.ecran_accueil()

    def interface_tuto(self):
        self.label_bienvenue.destroy()
        self.bouton_convertir_txt.destroy()
        self.bouton_tuto.destroy()

        self.bouton_retour = tk.Button(self, command=self.detruire_tuto, text="Retourner à l'accueil", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_retour.place(x=100, y=270);
        self.bouton_retour.bind("<Enter>", func=lambda e: self.bouton_retour.config(
            background="#ffcccc"))
        self.bouton_retour.bind("<Leave>", func=lambda e: self.bouton_retour.config(
            background="#ff9999"))

        self.label_tuto = tk.Label(self, text="Les fichiers TXT sont\ndonnés après un traitement\nde fichier WAW sur Matlab\nLes notes sont assemblées\nligne par ligne selon le\nformat suivant:\n\nNote Intensité Durée", fg="white", font=("Robotto", 11, "bold"), bg="#ff9999", width=23, height=10)
        self.label_tuto.place(x=100, y=40);

    def choisir_file(self):
        self.__file = filedialog.askopenfilename()
        if self.__file:
            self.traiter_fichier()

    def traiter_fichier(self):
        self.bouton_fichier.destroy()
        self.label_fichier.config(text=self.__file.split("/")[-1] + " sélectionné")
        self.bouton_convertir = tk.Button(self, command=self.convertir_fichier, text="Convertir le fichier", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_convertir.place(x=100, y=200);

    def convertir_fichier(self):
        TXTtoMIDI.generate_midi(self.__file)
        self.bouton_convertir.destroy()
        self.label_fichier.config(text="Fichier converti !")
        self.bouton_recommencer = tk.Button(self, command=self.interface_conversion_txt, text="Convertir un autre fichier", fg="white", font=("Robotto", 13, "bold"), bg="#ff9999", width=20, height=2)
        self.bouton_recommencer.place(x=100, y=200);

    def supp_convertion(self):
        self.bouton_recommencer.destroy()
        self.label_fichier.destroy()


app = Application()
app.mainloop()