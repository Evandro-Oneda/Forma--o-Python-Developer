import flet as ft

def main (pagina):
    titulo = ft.Text("Hshzap")
    pagina.add(titulo)

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""        
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)

    ft.Column
    linha_enviar =ft.Row([campo_enviar_mensagem, botao_enviar])

    chat= ft.Column()

    
    def entrar_chat(evento):
        popup.open= False     #fechar update
        pagina.remove(titulo)  #remover titulo
        pagina.remove(botao)  # remover botao
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario}: entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()  # atualiza pagina



    #criando pop up

    titulo_popup = ft.Text("Bem vindo")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup,content=caixa_nome,actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(botao)



ft.app(target=main, view=ft.AppView.WEB_BROWSER)

