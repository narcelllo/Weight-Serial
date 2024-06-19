import tkinter as tk
from tkinter import filedialog

def selecionar_diretorio():
    # Abre a janela de diálogo para selecionar um diretório
    diretorio_selecionado = filedialog.askdirectory()
    # Verifica se um diretório foi selecionado
    if diretorio_selecionado:
        # Exibe o diretório selecionado em uma etiqueta
        label_diretorio.config(text=f"Diretório selecionado: {diretorio_selecionado}")
    else:
        # Se nenhum diretório foi selecionado, mostra uma mensagem padrão
        label_diretorio.config(text="Nenhum diretório selecionado.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Seleção de Diretório")

# Cria um botão que chama a função 'selecionar_diretorio' quando clicado
botao_selecionar = tk.Button(janela, text="Selecionar Diretório", command=selecionar_diretorio)
botao_selecionar.pack(pady=20)

# Cria uma etiqueta para exibir o diretório selecionado
label_diretorio = tk.Label(janela, text="Nenhum diretório selecionado.")
label_diretorio.pack(pady=20)

# Executa a janela principal
janela.mainloop()
