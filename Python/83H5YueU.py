import tkinter


Var = "oi"

def LigaLED(i, myvar):
    i.configure(text=myvar.get())

def DesligaLED():
    ser.write(b'b')
    print("Exemplo de funcao")
    #return "oi"
    yield "oi"
    
def Exemplo():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)

    texto = tkinter.Label(root, text = Var)
    texto.pack()

    myvar = tkinter.StringVar()
    
    test = tkinter.Button(root, text="Liga LED")
    test['command'] = lambda: LigaLED(texto, myvar)
    test.pack()

    
    text_entry = tkinter.Entry(root, textvariable=myvar)
    text_entry.pack()
    
    test2 = tkinter.Button(root, text="Desliga LED")
    test2['command'] = DesligaLED
    test2.pack()
    
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs

if __name__ == '__main__':
    Exemplo()

