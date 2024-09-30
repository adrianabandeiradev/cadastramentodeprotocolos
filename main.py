# importanto do tkinter
from cgitb import text
from tkinter import *
from tkinter import font

from tkinter import ttk
from tkinter import messagebox

#importando calendário
from tkcalendar import Calendar, DateEntry

#importando o views
from view import *


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


# criando janela
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


#divindo as janelas
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)


frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0 , pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#Label cima
app_nome = Label(frame_cima, text= 'Cadastro de Protocolo', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)


#funcao inserir
global tree

def inserir():
    cliente = e_cliente.get()
    protocolo = e_protocolo.get()
    tipo = e_tipo.get()
    dia = e_cal.get()
    status = e_status.get()
    observacao = e_observacao.get()

    lista = [cliente, protocolo, tipo, dia, status, observacao]

    if cliente == '':
        messagebox.showerror('Error', 'O campo cliente não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Dados cadastrados com sucesso')

        e_cliente.delete(0,'end')
        e_protocolo.delete(0,'end')
        e_tipo.delete(0,'end')
        e_cal.delete(0,'end')
        e_status.delete(0,'end')
        e_observacao.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()



#função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_cliente.delete(0,'end')
        e_protocolo.delete(0,'end')
        e_tipo.delete(0,'end')
        e_cal.delete(0,'end')
        e_status.delete(0,'end')
        e_observacao.delete(0,'end')

        e_cliente.insert(0,tree_lista[1])
        e_protocolo.insert(0,tree_lista[2])
        e_tipo.insert(0,tree_lista[3])
        e_cal.insert(0,tree_lista[4])
        e_status.insert(0,tree_lista[5])
        e_observacao.insert(0,tree_lista[6])
       


        def update():
            cliente = e_cliente.get()
            protocolo = e_protocolo.get()
            tipo = e_tipo.get()
            dia = e_cal.get()
            status = e_status.get()
            observacao = e_observacao.get()

            lista = [cliente, protocolo, tipo, dia, status, observacao, valor_id]

            if cliente == '':
                messagebox.showerror('Error', 'O campo cliente não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso')

                e_cliente.delete(0,'end')
                e_protocolo.delete(0,'end')
                e_tipo.delete(0,'end')
                e_cal.delete(0,'end')
                e_status.delete(0,'end')
                e_observacao.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

                #criando botão atualizar
        b_confirmar = Button (frame_baixo, command=update, text= 'Confirmar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)

        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')   


# funçao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Informações deletadas com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela') 


# label baixo
# Cliente
l_cliente = Label(frame_baixo, text= 'Cliente *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cliente.place(x=15, y=10)
e_cliente = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_cliente.place(x=15, y=40)

# Protocolo
l_protocolo = Label(frame_baixo, text= 'Nº Protocolo *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_protocolo.place(x=15, y=70)
e_protocolo = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_protocolo.place(x=15, y=100)

# Tipo do Protocolo
l_tipo = Label(frame_baixo, text= 'Tipo do Protocolo *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tipo.place(x=15, y=130)
e_tipo = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tipo.place(x=15, y=160)

# Data
l_cal = Label(frame_baixo, text= 'Data *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cal.place(x=15, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal.place(x=15, y=220)

# Status
l_status = Label(frame_baixo, text= 'Status *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_status.place(x=160, y=190)
e_status = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_status.place(x=160, y=220)

# Observação
l_observacao = Label(frame_baixo, text= 'Observação *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_observacao.place(x=15, y=260)
e_observacao = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_observacao.place(x=15, y=290)


#criando botão inserir
b_inserir = Button (frame_baixo, command=inserir, text= 'Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)


#criando botão atualizar
b_atualizar = Button (frame_baixo, command=atualizar,  text= 'Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

#criando botão excluir
b_deletar = Button (frame_baixo, command=deletar, text= 'Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=340)

# treeview

def mostrar():

    global tree

    lista = mostrar_info()


    #lista para cabeçalho
    tabela_head = ['ID', 'Cliente', 'Protocolo', 'Tipo', 'Data', 'Status', 'Observacao']

    #criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # scrollbar vertical
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # scrollbar horizontal
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item) 



# chamando a função mostrar
mostrar()
janela.mainloop()
