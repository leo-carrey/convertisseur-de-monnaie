from tkinter import Tk, ttk
from tkinter import *


# crée une fenetre
window = Tk()
window.title("convertisseur-de-monnaie")
window.geometry("350x400")
window.resizable(height=False, width=False)


# ajout du titre 'currency converter'
title = Label(window, text="currency converter", font=("courrier", 15), fg='black')
title.pack()


# ajout d'un text nommée 'amount'
amount = Label(window, text="amount :", font=("courrier", 10), fg='black', pady=10)
amount.place(x=50, y=28)        


# ajout d'un text nommée 'from currency'
from_currency = Label(window, text="from currency :", font=("courrier", 10), fg='black', pady=5)
from_currency.place(x=50, y=97)


# ajout d'un text nommée 'to currency'
to_currency = Label(window, text="to currency :", font=("courrier", 10), fg='black', pady=5)
to_currency.place(x=50, y=67)


# ajout d'un text nommée 'converted amount'
converted_amount = Label(window, text="converted amount :", font=("courrier", 10), fg='black')
converted_amount.place(x=50, y=200)


# ajout d'un emplacement pour renseigner l'argent à convertir
amount_before = Entry(window, relief="solid", justify=CENTER, width=10)
amount_before.place(x=180, y=40)


# ajout d'un emplacement pour ecrire les erreur
fail = Label(window, text="", justify=CENTER, width=25, fg="red")
fail.place(x=170, y=250)


# afficher le resultat
result = Label(window, text="", relief="solid", width=20, height=1, bg='white')
result.place(x=180, y=200)
 

# ajout d'une valeur à une devise
currency_rate={
    "EUR":1,
    "USD":1.08,
    "CAD":1.45,
    "BRL":5.56,
    "INR":88.47,
    "DZD":146.72,
    "MGA ar":4755.00,
    "PHP ₱":59.46,
    "PLN zł":4.69,
    "XAF Fr":656.63,
    "CNY ¥":7.35,
    "JPY ¥":139.47,
}

# liste des devise
currency = ['BRL', 'CAD', 'CNY ¥', 'DZD', 'EUR', 'INR', 'JPY ¥', 'MGA ar', 'PHP ₱', 'PLN zł', 'USD', 'XAF Fr']


# ajout d'une fonction qui permet de calculer la valeur à convertir
def convert_amount():
    try:
        amount = float(amount_before.get())
        if type(amount) == float:
            fail.config(text="")
    except:
        fail.config(text="Please enter a number", fg="red")
    try:
        if combo1.get() == "" or combo2.get() == "":
            fail.config(text="Please select a currency", fg="red")
    except:
        fail.config(text="")
    try:
        if combo1.get() not in currency_rate or combo2.get() not in currency_rate:
            fail.config(text="Please select currency", fg="red")
    except:
        fail.config(text="")
    output = float(amount)*(float(currency_rate[combo2.get()])/float(currency_rate[combo1.get()]))  
    result.config(text=output)
    historical_box.insert(END ,(amount, combo1.get(), "=", round(output, 2), combo2.get()))


# la devise avant convertion
combo1 = ttk.Combobox(window, width=8, justify=CENTER, font="courrier")
combo1['values'] = (currency)
combo1.place(x=180, y=70)


# la devise apres convertion
combo2 = ttk.Combobox(window, width=8, justify=CENTER, font="courrier")
combo2['values'] = (currency)
combo2.place(x=180, y=100)


# ajout du bouton de convertion
convert = Button(window, text="convert", font=("courrier", 10), fg='black', command=convert_amount)
convert.place(x=150, y=150)


# ajout d'un emplacement ou mettre l'historique
historical_box= Listbox(window, relief=SOLID, width=30)
historical_box.place(x=10 ,y=230)


# afficher la fenetre
window.mainloop()