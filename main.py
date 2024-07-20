from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    translator = Translator()
    translated = translator.translate(text_var.get(), src=src_lang.get(), dest=dest_lang.get())
    translated_text.set(translated.text)

root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
try:
    root.iconbitmap('logo_simple.ico')  # Ensure the icon file name is correct and in the same directory
except:
    pass
root['bg'] = 'skyblue'

root.title('Language Translator by Muhammad Mohsin')

Label(root, text='Language Translator', font='Arial 20 bold', bg='skyblue').pack()

Label(root, text="Enter Text Here", font='arial 13 bold', bg='white smoke').place(x=165, y=65)

text_var = StringVar()
Entry(root, textvariable=text_var, width=60).place(x=160, y=100)

Label(root, text="From Language", font='arial 13 bold', bg='white smoke').place(x=160, y=140)
src_lang = StringVar()
src_lang.set('en')  # default value
src_lang_menu = OptionMenu(root, src_lang, *LANGUAGES.keys())
src_lang_menu.place(x=300, y=140)

Label(root, text="To Language", font='arial 13 bold', bg='white smoke').place(x=160, y=180)
dest_lang = StringVar()
dest_lang.set('es')  # default value
dest_lang_menu = OptionMenu(root, dest_lang, *LANGUAGES.keys())
dest_lang_menu.place(x=300, y=180)

Button(root, text='Translate', command=translate_text).place(x=160, y=220)

translated_text = StringVar()
Label(root, textvariable=translated_text, font='arial 13 bold', bg='white smoke').place(x=160, y=260)

root.mainloop()
