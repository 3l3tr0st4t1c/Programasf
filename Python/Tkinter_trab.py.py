import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def selec_arq():
    tipo_de_arq = (
        ("Arquivo de texto", "*.txt"),
        ("Documentos PDF", "*.pdf"),
        ("Todos os Arquivos", "*.")
    )
    caminho_do_arq = filedialog.askopenfilename(
        title="Selecione um arquivo",
        initialdir="/",
        filetypes=tipo_de_arq
    )

    entry_cam.delete(0, tk.END)

    if caminho_do_arq:
        entry_cam.insert(0, caminho_do_arq)
    else:
        entry_cam.insert(0, "Nenhum Arquivo Selecionado.")

root = tk.Tk()
root.title("Selecionador de Arquivo Qualquer")
root.geometry("500x200")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

botao_selec = tk.Button(
    frame,
    text="Clique para Selecionar um Arquivo",
    command=selec_arq,
    font=("Arial", 12),
    bg="#e0e0e0"
)
botao_selec.pack(pady=20)

entry_cam = tk.Entry(
    frame,
    font=("Arial", 10),
    width=70
)
entry_cam.pack(pady=10, fill='x', expand=True)

root.mainloop()
