from tkinter import *
from ttkbootstrap import Style

# Configurações da interface de cadastro finalizado
def cadastrar_clientes():
    interface2 = Tk()
    interface2.title("Finalizando cadastro")
    width = 200
    height = 150
    altura_tela = interface2.winfo_screenwidth()
    largura_tela = interface2.winfo_screenheight()

    x = (altura_tela // 2) - (width // 2)
    y = (largura_tela // 2) - (height // 2)

    interface2.geometry(f"{width}x{height}+{x}+{y}")

    estilo2 = Style(theme="darkly")
    estilo2.master = interface2 

    # Texto e botão da interface de cadastro finalizado
    texto_cadastro = Label(interface2, text="Cadastro finalizado!", font=("Arial", 12, "bold"))
    texto_cadastro.grid(column=1, row=1, padx=20, pady=20)

    botao_interface2 = Button(interface2, text="OK", command=interface2.destroy, width=5, font=("Arial", 12))
    botao_interface2.grid(column=1, row=2, padx=20, pady=20)

    interface2.mainloop()  


# Criação da interface de cadastro
interface = Tk()
interface.title("Cadastro de clientes")
width = 693
height = 557
altura_tela = interface.winfo_screenwidth()
largura_tela = interface.winfo_screenheight()
x = (altura_tela // 2) - (width // 2)
y = (largura_tela // 2) - (height // 2)
interface.geometry(f"{width}x{height}+{x}+{y}")

estilo = Style(theme="darkly")
estilo.master = interface 

# Textos e campos para preencher na interface
texto_inicial = Label(interface, text="Cadastre os clientes abaixo:", font=("Arial", 22, "bold"))
texto_inicial.grid(column=2, row=1, pady=35)

id = Label(interface, text="ID:", font=("Arial", 12))
id.grid(column=1, row=2, padx=3, pady=15)
preencher_id = Entry(interface, width=60)
preencher_id.grid(column=2, row=2)

nome = Label(interface, text="Nome:", font=("Arial", 12))
nome.grid(column=1, row=3, padx=3, pady=15)
preencher_nome = Entry(interface, width=60)
preencher_nome.grid(column=2, row=3)

endereco = Label(interface, text="Endereço:", font=("Arial", 12))
endereco.grid(column=1, row=4, padx=3, pady=15)
preencher_endereco = Entry(interface, width=60)
preencher_endereco.grid(column=2, row=4)

cep = Label(interface, text="CEP:", font=("Arial", 12))
cep.grid(column=1, row=5, padx=3, pady=15)
preencher_cep = Entry(interface, width=60)
preencher_cep.grid(column=2, row=5)

uf = Label(interface, text="UF:", font=("Arial", 12))
uf.grid(column=1, row=6, padx=3, pady=15)
preencher_uf = Entry(interface, width=60)
preencher_uf.grid(column=2, row=6)

telefone = Label(interface, text="Telefone:", font=("Arial", 12))
telefone.grid(column=1, row=7, padx=3, pady=15)
preencher_telefone = Entry(interface, width=60)
preencher_telefone.grid(column=2, row=7)

email = Label(interface, text="E-mail:", font=("Arial", 12))
email.grid(column=1, row=8, padx=3, pady=15)
preencher_email = Entry(interface, width=60)
preencher_email.grid(column=2, row=8)

# Botão para cadastrar os clientes
botao = Button(interface, text="Cadastrar", command=cadastrar_clientes, width=12, height=2, font=("Arial", 12))
botao.grid(column=4, row=8, padx=70, pady=10)

interface.mainloop()
