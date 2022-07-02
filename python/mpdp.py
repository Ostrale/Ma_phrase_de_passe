import tkinter as tk
import random
import subprocess 

def copy2clip(txt): 
    cmd='echo '+txt.strip()+'|clip' 
    return subprocess.check_call(cmd, shell=True)

with open("liste_francais.txt", "r") as tf:
    mot = tf.read().split('\n')

def insertf():
    txt = ''
    nb='0123456789'
    TextChatA.configure(state='normal') #autorise l'écriture dans TextChatA
    mdp = generateur()
    for el in mdp: 
        if el in nb:
            TextChatA.insert(tk.END,el,'number')
        elif el == '-':
            TextChatA.insert(tk.END,el,'tiret')
        else:
            TextChatA.insert(tk.END,el.capitalize())
        txt += el
    copy2clip(txt)
    TextChatA.insert(tk.END,"\nCopié dans le presse papier\n",'clipboard')
    #TextChatA.insert(tk.END, "\n")
    TextChatA.configure(state='disabled') #interdit l'écriture dans TextChatA
    TextChatA.see("end") #permet de mettre la barre de défilement à la fin quand on recoit un message

def generateur():
    n = int(saisie.get())
    mdp = []
    position_chiffre = random.randint(0,n-1)
    for i in range(0,n):
        mdp.append(mot[random.randint(0,len(mot))])
        if i == position_chiffre :
            mdp.append(str(random.randint(0,9)))
        mdp.append('-')
    mdp = mdp[0:-1]
    return mdp

fenetre = tk.Tk()
fenetre.title("Générateur de phrase de passe")

"""message a afficher dans une zone avec defillement"""
scrollText = tk.Scrollbar(fenetre)
TextChatA = tk.Text(fenetre,font="Arial",state='disabled',height = 20, width = 40)

TextChatA.focus_set()
scrollText.grid(row=1, column=2, rowspan=2, sticky=tk.NS)
TextChatA.grid(row=1, column=1,rowspan=2)
scrollText.config(command=TextChatA.yview)
TextChatA.config(yscrollcommand=scrollText.set)
TextChatA.tag_config('tiret', foreground="red")
TextChatA.tag_config('number', foreground="blue")
TextChatA.tag_config('clipboard', foreground="grey",font=("Courier", 9))

bouton=tk.Button(fenetre, text="Générer", command=insertf,borderwidth=0.5)
bouton.grid(row=5, column=1,columnspan=2)

label = tk.Label(fenetre, text="Nombres de mot que comporte la phrase de passe :")
label.grid(row=3, column=1,columnspan=2)
saisie = tk.StringVar()
ligne_texte = tk.Entry(fenetre, textvariable=saisie, width=8)
ligne_texte.insert(tk.END,'3')
ligne_texte.grid(row=4, column=1,columnspan=2)

insertf()
fenetre.mainloop()