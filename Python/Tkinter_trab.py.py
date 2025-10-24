import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def selec_arq():
    tipo_de_arq = (
        ("Documentos PDF", "*.pdf"),
        ("Todos os Arquivos", "*.")
    )
    caminho_do_arq = filedialog.askopenfilename(
        title="Selecione um arquivo",
        initialdir="/",
        filetypes=tipo_de_arq
    )

    if caminho_do_arq:
        entry_cam.delete(0, tk.END)
        entry_cam.insert(0, caminho_do_arq)

        atualizar_texto_result("Arquivo selecionado. Clique me 'Processar'.")

def atualizar_texto_result(texto_string):
    text_result.config(state=tk.NORMAL)
    text_result.delete('1.0', tk.END)
    text_result.insert(tk.END, texto_string)
    text_result.config(state=tk.DISABLED)

def iniciar_processamento_simulado():
    caminho_do_arq = entry_cam.get()

    if not caminho_do_arq:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo primero.")
        return

    if not caminho_do_arq.endswith("pdf"):
        messagebox.showerror("Erro", "O arquivo não parece ser um PDF.")
        return

root = tk.Tk()
root.title("Processador de Datas")
root.geometry("500x200")
root.minsize(500,400)

style = ttk.Style()
style.theme_use('clam')

frame_principal = tk.Frame(root, padx=10, pady=10)
frame_principal.pack(fill=tk.BOTH,expand=True)

frame_principal.rowconfigure(3, weight=1)
frame_principal.columnconfigure(0, weight=1)

frame_input = ttk.Frame(frame_principal)
frame_input.grid(row=0, column=0, sticky="ew", pady=5)
frame_input.columnconfigure(0, weight=1)

label_arq = ttk.Entry(frame_input, width=60)
label_arq.grid(row=0, column=0, columnspan=2, sticky="w")

entry_cam = ttk.Label(frame_input, width=60)
entry_cam.grid(row=1, column=0, sticky="ew", padx=(0, 10))

botao_selec = ttk.Button(
    frame_input,
    text="Clique para Selecionar um Arquivo",
    command=selec_arq,
)
botao_selec.grid(row=1, column=1, sticky="e")

botao_proce = ttk.Button(
    frame_principal,
    text="Processar Arquivo e Mostrar Datas.",
    command=iniciar_processamento_simulado,
    style='Accent.TButton'
)
style.configure('Accent.TButton', font=('Arial', 10, 'bold'))
botao_proce.grid(row=1, column=0, sticky="ew", pady=10)

label_result = ttk.Label(
    frame_principal,
    text="Informações Pós-Processamento (String):",
    font=('Arial', 11, 'bold')
)
label_result.grid(row=2, column=0, sticky="w", pady=(10, 0))

frame_texto = ttk.Frame(frame_principal)
frame_texto.grid(row=3, column=0, sticky="nsew", pady=5)
frame_texto.rowconfigure(0, weight=1)
frame_texto.columnconfigure(0, weight=1)

text_result = tk.Text(
    frame_texto,
    height=15,
    wrap=tk.WORD,
    state=tk.DISABLED,
    font=("Courier New", 10)
)
text_result.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(
    frame_texto,
    orient=tk.VERTICAL,
    command=text_result.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")
text_result.config(yscrollcommand=scrollbar.set)

root.mainloop()