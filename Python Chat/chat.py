import flet as ft

def main(pagina):
    titulo = ft.Text("Python Chat")
    pagina.add(titulo)

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)

        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao_inicial)
        pagina.add(chat)
        pagina.add(linha_enviar)

        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        

    # popup
    titulo_popup = ft.Text("Bem vindo(a) ao Python Chat!")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_inicial = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    pagina.add(botao_inicial)

ft.app(main, view=ft.WEB_BROWSER)