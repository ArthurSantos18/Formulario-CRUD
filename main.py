from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from crud import *
from database import *

# Criar Banco de Dados
create_database()

# Cores
color1 = "#216B80" 
color2 = "#BFFFFF" 
color3 = "#D7FFFF" 
color4 = "#000000" 
color5 = "#DCFFFF" 

# Funções
global table

def read_table():
    global table

    list = read_data()

    # Criação da table
    table_header = ['ID', 'Nome','Email', 'Data de nascimento','gender']

    table = ttk.Treeview(frame2_right, selectmode="extended", columns=table_header, show="headings")

    # Barra de Scroll
    scrollvert = ttk.Scrollbar(frame2_right, orient="vertical", command=table.yview)
    scrollhori = ttk.Scrollbar(frame2_right, orient="horizontal", command=table.xview)
    table.configure(yscrollcommand=scrollvert.set, xscrollcommand=scrollhori.set)

    # Posicionamento da tabela
    table.place(x=2, y=2, width=678, height=368)
    scrollvert.place(x=680, y=0, height=370)
    scrollhori.place(x=2, y=370, width=694)

    h = [20, 200, 200, 100, 40]
    cont = 0

    # Elementos das colunas
    for columns in table_header:
        table.heading(columns, text=columns.title())
        table.column(columns, width=h[cont])
        cont += 1

    for data in list:
        table.insert('', 'end', values=data)

def insert_table():
    name = entry_name.get()
    email = entry_email.get()
    data = entry_date.get()
    s = var_gender.get()
    if s == 0:
        gender = 'M'
    elif s == 1:
        gender = 'F'

    list = [name, email, data, gender]

    if name == '':
        messagebox.showerror('Erro!','Por favor, preencha o nome')
    elif email == '':
        messagebox.showerror('Erro!','Por favor, preencha o email')
    else:
        create_data(list)
        messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso')
        
    for data in frame2_right.winfo_children():
        data.destroy()
    
    read_table()

def update_table():
    try:
        table_element = table.focus()
        table_dictionary = table.item(table_element)
        table_list = table_dictionary['values']
        valor_id = table_list[0]

        def confirm():
            name = entry_name.get()
            email = entry_email.get()
            data = entry_date.get()
            s = var_gender.get()
            if s == 0:
                gender = 'M'
            elif s == 1:
                gender = 'F'

            list = [name, email, data, gender, valor_id]

            if name == '':
                messagebox.showerror('Erro!','Por favor, preencha o nome')
            elif email == '':
                messagebox.showerror('Erro!','Por favor, preencha o email')
            else:
                update_data(list)
                messagebox.showinfo('Sucesso!', 'Dados atualizados com sucesso')
            
            for data in frame2_right.winfo_children():
                data.destroy()      
            bt_confirm.destroy()
            read_table()
        # Botão confirmar
        bt_confirm= Button(frame2_left, command=confirm ,text='Confirmar', width=13, height=1, bg="green", font=("Ivy 10"), fg=color5)
        bt_confirm.place(x=10, y=320)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um cadastro')

def delete_table():
    try:
        table_element = table.focus()
        table_dictionary = table.item(table_element)
        table_list = table_dictionary['values']
        valor_id = [table_list[0]]

        delete_data(valor_id)
        messagebox.showinfo('Sucesso!', 'Dados deletados com sucesso')

        for data in frame2_right.winfo_children():
            data.destroy()
        
        read_table()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um cadastro')

########## CRIANDO janela ###########
# Criando a janela
root = Tk()
root.title("Formulário")
root.geometry('1020x440')
root.configure(background=color5)
root.resizable(width=False, height=False)

# Desenho da tela
frame1 = Frame(root, bg=color1, highlightbackground="black", highlightthickness=1)
frame1.place(relx=0, rely=0, width=1020, height= 50)

frame2_left = Frame(root, bg=color2, highlightbackground="black", highlightthickness=1)
frame2_left.place(relx=0, rely=0.113, width=320, height=390)

frame2_right = Frame(root, bg=color3, highlightbackground="black", highlightthickness=1)
frame2_right.place(relx=0.314, rely=0.113, width=700, height=390)


# Texto da tela
label_form = Label(frame1, text='Formulário CRUD', font=("Ivy 22 bold"), bg=color1, fg=color5)
label_form.place(relx=0.41, rely=0.1)

########## FRAME ESQUERDA ###########
# Nome
label_name = Label(frame2_left, text='Nome *', font=("Ivy 12 bold"), bg=color2)
label_name.place(x=10, y=30)
entry_name = Entry(frame2_left, width=32, justify="left",font=("Ivy 12"), relief="solid")
entry_name.place(x=10, y=60)

# E-mail
label_email = Label(frame2_left, text='E-mail *', font=("Ivy 12 bold"), bg=color2)
label_email.place(x=10, y=100)
entry_email = Entry(frame2_left, width=32, justify="left",font=("Ivy 12"), relief="solid")
entry_email.place(x=10, y=130)

# Data
label_date = Label(frame2_left, text='Data de nascimento *', font=("Ivy 12 bold"), bg=color2)
label_date.place(x=10, y=170)
entry_date = DateEntry(frame2_left, width=14, height=2 ,background=color1, foreground=color5, borderwidth= 2) 
entry_date.place(x=10, y=200)

# gender
var_gender = IntVar()
label_gender = Label(frame2_left, text='gender *',font=("Ivy 12 bold"), bg=color2)
label_gender.place(x=190, y=170)
check_gender = Radiobutton(frame2_left, text='M', value=0, variable=var_gender, font=("Ivy 10"), bg=color2, activebackground=color2)
check_gender.place(x=190, y=200)
check_gender = Radiobutton(frame2_left, text='F', value=1, variable=var_gender, font=("Ivy 10"), bg=color2, activebackground=color2)
check_gender.place(x=240, y=200)

# Botão Enviar
bt_send= Button(frame2_left, command=insert_table, text='Enviar', width=27, height=1, bg=color1, font=("Ivy 10"), fg=color5)
bt_send.place(x=40, y=260)

# Botão Atualizar
bt_update= Button(frame2_left, command=update_table ,text='Atualizar', width=13, height=1, bg="green", font=("Ivy 10"), fg=color5)
bt_update.place(x=10, y=320)

# Botão Deletar
bt_delete= Button(frame2_left, command=delete_table, text='Deletar', width=13, height=1, bg="red", font=("Ivy 10"), fg=color5)
bt_delete.place(x=190, y=320)

########## FRAME DIREITA ###########
read_table()

# Loop da tela
root.mainloop()
