import flet as ft

class Cliente:
    def __init__(self,nome,email):
        self. nome = nome
        self.email = email

class Quarto:
    def __init__(self,numero,tipo,preco_por_noite):
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite
        self.disponivel = True


class Reserva:
    def __init__(self,cliente: Cliente,quarto:Quarto,data: str):
        self.cliente = cliente
        self.quarto = quarto 
        self.data = data 
        self.confirmada = False 

    def confirmar_reserva(self):
        self.confirmada = True
        self.quarto.disponivel = False


class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []
        self.reservas= []


    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)


    def listar_quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.quartos:
            if quarto.disponivel == True:
                quartos_disponiveis.append(quarto)
            return quartos_disponiveis 

    def criar_reserva (self, cliente: Cliente,numero_quarto: int,data: str):
        quarto_reservado = None

        for quarto in self.quartos:
            if quarto.disponivel == True and quarto.numero == numero_quarto:
                quarto_reservado = quarto

        if quarto_reservado != None:
            reserva_do_quarto = Reserva(cliente,quarto,data)
            self.reservas.append(reserva_do_quarto)
            reserva_do_quarto.confirmar_reserva()
            return reserva_do_quarto 
        else:
            return None




cliente_1 = Cliente('Neitan','neitan@email.com')





def principal(pagina: ft.Page):
    gerenciador_hotel = GerenciadorDeReservas()
    quarto_padrao = Quarto(101, 'Padrão', 100)
    quarto_deluxe = Quarto(102, 'deluxe', 500)
    suite_master = Quarto(105, 'Suíter MAster',800)


    gerenciador_hotel.adicionar_quarto(quarto_padrao)
    gerenciador_hotel.adicionar_quarto(quarto_deluxe)
    gerenciador_hotel.adicionar_quarto(suite_master)


    def atualizar_lista_quartos():
        lista_quartos.controls.clear()
        



    def reservar_quarto(evento):
        print(txt_field_cliente.value)
        print(txt_field_email.value)
        cliente_informado = Cliente(txt_field_cliente.value,txt_field_email.value)
        numero_quarto = txt_field_data.value
        data_informada = txt_field_data.value
        reserva = gerenciador_hotel.criar_reserva(cliente_informado,numero_quarto, data_informada)


        if reserva != None:
            texto_status.value = 'Reservado !'
        else:
            texto_status.value = 'Erro na Reserva'


        pagina.update()







 #parte Visual de entrada

    txt_field_cliente = ft.TextField(label=' Nome do cliente', width=300, bgcolor="LIGHTWHITE")
    txt_field_email = ft.TextField(label=' Email do cliente', width=300, bgcolor="LIGHTWHITE")
    txt_field_numero_quarto = ft.TextField(label=' Numero do quarto', width=300, bgcolor="LIGHTWHITE")
    txt_field_data = ft.TextField(label=' AAAA-MM-DD', width=300, bgcolor="LIGHTWHITE")


    lista_quartos = ft.Column()
    texto_status = ft.Text()

    pagina.add(
        ft.Column([
            ft.Text('Sistemas de reservas do hotel', size=46.5, color='#4169E1'),
            lista_quartos,
            ft.Row([txt_field_cliente,txt_field_email]),
            ft.Row([txt_field_numero_quarto, txt_field_data]),
            ft.ElevatedButton('Reservar quarto', on_click= reservar_quarto),
            texto_status
        ])

    )



ft.app (target=principal)







