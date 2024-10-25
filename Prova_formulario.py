#[PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato.
#  O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem.
# Após o usuário preencher esses campos, deve haver um botão de envio. 
# Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, 
# indicando que o formulário foi enviado com sucesso.

import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ft.Text("Por Favor, preencha com os dados a seguir: ", size=20))

    nome_input = ft.TextField(label="Nome")
    email_input = ft.TextField(label="E-mail")
    mensagem_input = ft.TextField(label="Fale mais sobre você ...", multiline=True, min_lines=3)  # Usando TextField com multiline
    mensagem_confirmacao = ft.Text("", size=20, color=ft.colors.BLUE)

    def enviar(event):
        if nome_input.value and email_input.value and mensagem_input.value:
            mensagem_confirmacao.value = "Seu formulário foi enviado com sucesso =) ."
            nome_input.value = ""
            email_input.value = ""
            mensagem_input.value = ""
        else:
            mensagem_confirmacao.value = "Verifique se todos os dados a seguir estão preenchidos corretamente."
        page.update()

    enviar_button = ft.ElevatedButton("Enviar", on_click=enviar)

    page.add(nome_input, email_input, mensagem_input, enviar_button, mensagem_confirmacao)

ft.app(target=main)