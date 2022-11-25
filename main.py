from tkinter import *
from langdetect import detect
from langcodes import *

master = Tk()
master.title("Quelle langue parles tu ?")
master.geometry("1900x1040")


def Detect_Langue():
    # pour vérifier que le champ de texte n'est pas vide
    if mon_text.compare("end-1c", "==", "1.0"):
        my_lable.config(text="Je peux rien faire ! t'as rien écris.. ")
    else:
        # prendre la valeur du champ du texte d'es premier caractere au dernier
        code = detect(mon_text.get(1.0, END))

        # il faut installé langcodes[data] pour avoir le nom de la langue en mode complet
        resultat = Language.make(language=code).display_name()
        my_lable.config(text=f"Votre langue est: {resultat}")


zone_texte = Tk.Label(text="zone de texte")

mon_text = Text(master, height=10, width=150)
mon_text.pack(pady=20)

button = Button(master, text="Detecter", command=Detect_Langue)
button.pack(pady=20)

my_lable = Label(master, text="", width=100, font=(
    "times new roman", 15, "bold"), height=0, bg="white")
my_lable.pack(pady=20)


master.mainloop()
