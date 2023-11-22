from tkinter import *
import controle as co
import time

root = Tk()


def adicionar_restricao():
    nova_restricao_left = Entry(Restricoes_frame, width=30)
    nova_restricao_left.grid(row=len(restricoes_lista), column=0, padx=5, pady=5)
    nova_restricao_middle = Entry(Restricoes_frame, width=10)
    nova_restricao_middle.grid(row=len(restricoes_lista), column=1, padx=5, pady=5)
    nova_restricao_right = Entry(Restricoes_frame, width=30)
    nova_restricao_right.grid(row=len(restricoes_lista), column=2, padx=5, pady=5)

    nova_restricao = [nova_restricao_left,nova_restricao_middle,nova_restricao_right]
    restricoes_lista.append(nova_restricao)

def salvar():
    for entry_list in restricoes_lista:
        value = [entry.get() for entry in entry_list]
        co.restricoes.append(value)
    co.funcao = str(z_entry.get())
    co.opcao = var.get()
    import main as m
    time.sleep(3)
    report()

def report():
    window = Tk()
    window.geometry("500x500")
    window.title("Report")

    report_label = Label(window, text="Report", font=("Arial, 32"))
    report_label.pack(side='top', pady=10)
    
    data = Frame(window, width=400, height=400, borderwidth=3, highlightcolor='black')
    data.pack(side='top', pady=40)

    data_lucro = Label(data, text="Lucro", font=("Arial, 12"))
    data_lucro.grid(row=0, column=0, padx=5, pady=5)

    equal = Label(data, text="=", font=("Arial, 12"))
    equal.grid(row=0, column=1, padx=5, pady=5)

    data_lucro_value = Label(data, text=co.lucro_maximo, font=("Arial, 12"))
    data_lucro_value.grid(row=0, column=2, padx=5, pady=5)

    data_sombra = Label(data, text="Preço-sombra", font=("Arial, 12"))
    data_sombra.grid(row=1, column=0, padx=5, pady=5)

    equal = Label(data, text="=", font=("Arial, 12"))
    equal.grid(row=1, column=1, padx=5, pady=5)

    data_sombra_value = Label(data, text=co.preco_sombra, font=("Arial, 12"))
    data_sombra_value.grid(row=1 , column=2, padx=5, pady=5)

    data_melhor_ponto = Label(data, text="Ponto ótimo", font=("Arial, 12"))
    data_melhor_ponto.grid(row=2, column=0, padx=5, pady=5)

    equal = Label(data, text="=", font=("Arial, 12"))
    equal.grid(row=2, column=1, padx=5, pady=5)

    data_melhor_ponto_value = Label(data, text=co.melhor_pontos, font=("Arial, 12"))
    data_melhor_ponto_value.grid(row=2, column=2, padx=5, pady=5)

    



root.geometry("600x600")
root.title("Trabalho de Otimização")

titulo = Label(root, text="Otimização", font=("Arial, 32") )
titulo.pack(side='top', pady=10)

titulo_funcao = Label(root, text="Função Objetiva", font=("Arial, 12"))
titulo_funcao.pack(side='top', pady=10)

choice_frame = Frame(root, height=400, width=600)
choice_frame.pack(side='top', pady=20)

var = StringVar()
maximize = Radiobutton(choice_frame, text="Maximize", variable=var, value="Maximize")
minimize = Radiobutton(choice_frame, text="Minimize", variable=var, value="Minimize")

maximize.grid(row=1, column=0)
minimize.grid(row=1, column=1)

z_frame = Frame(root, height=400, width=600)
z_frame.pack(side='top')
z_label = Label(z_frame, text="Z = ", font=("Arial, 12"))
z_label.grid(row=2, column=0)
z_entry = Entry(z_frame, width=30)
z_entry.grid(row=2, column=1)


Restricoes_title = Label(root, text="Restrições", font=("Arial, 12"))
Restricoes_title.pack(side='top', pady=20)

Restricoes_add_button = Button(root, text="Adicionar Restrição", command=adicionar_restricao)
Restricoes_add_button.pack(side='top')

restricoes_lista = []

Restricoes_frame = Frame(root, height=400, width=600)
Restricoes_frame.pack(side='top')

salvar = Button(root, text="Salvar e Executar", command=salvar)
salvar.pack(side='bottom', pady=10)

root.mainloop()
