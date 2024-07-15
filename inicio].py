import flet as ft
import pyautogui as auto
import time

numero = 0
#def mãe, dentro daqui tudo estara dentro do app
def principal(page):
    #configurações da pagina 
    page.title = "BOTÃO DE TAREFAS"
    page.window_width = 180
    page.window_height = 440
    page.window_resizable = True
    #pause entre cada comando do pyautogui
    auto.PAUSE = 0.5

    #funcão chamada ao clicar o botao vscode_button
    def abrir_vscode(evento):
        auto.press('win')
        auto.write('vscode')
        auto.press('enter')

    #funcão chamada ao clicar o botao gravartela_button
    def gravartela(evento):
        auto.hotkey('win', 'g')
        time.sleep(1)
        auto.click(x=258, y=53)

    #funcão chamada ao clicar o botao screnshoot_button
    def screnshoot(evento):
        global numero
        screenshot = auto.screenshot()
        #para não salvar todo vez em cima de um só arquivo, essa variavel muda o nome do arquivo toda vez que essa 
        #função for chamada /obs: ao encerrar o arquivo e iniciar dnv, a contagem inicia do 1 novamente
        numero += 1
        screenshot.save(f"screenshot{numero}.png")  

    #funcão chamada ao clicar o botao whatsapp_button
    def whatsapp(evento):
        auto.press('win')
        auto.write('whatsapp')
        auto.press('enter')

    #funcão chamada ao clicar o botao discord_button
    def discord(evento):
        auto.press('win')
        auto.write('discord')
        auto.press('enter')

    #funcão chamada ao clicar o botao youtube_button
    def youtube(evento):
        auto.press('win')
        auto.write('opera')
        auto.press('enter')
        time.sleep(3)
        auto.click(x=1291, y=338)

    #funcão chamada ao clicar o botao deboa_button
    def deboa(evento):
        auto.press('win')
        auto.write('opera')
        time.sleep(1)
        auto.press('enter')
        time.sleep(1)
        auto.click(x=31, y=487)
        time.sleep(2)
        auto.click(x=16, y=610)
        time.sleep(2)
        auto.click(x=1291, y=338)

    #funcão chamada ao clicar o botao estudar_button
    def estudar(evento):
        auto.press('win')
        auto.write('opera')
        time.sleep(1)
        auto.press('enter')
        time.sleep(1)
        auto.click(x=31, y=487)
        time.sleep(2)
        auto.click(x=31, y=487)
        auto.click(x=631, y=514)
        time.sleep(2)
        auto.click(x=1416, y=595)
        auto.write('-----------')
        auto.press('tab')
        auto.press('enter')

    #funcão chamada ao clicar o botao codar_button
    def codar(evento):
        auto.press('win')
        auto.write('vscode')
        time.sleep(1)
        auto.press('enter')
        time.sleep(2)
        auto.press('win')
        auto.write('opera')
        time.sleep(1)
        auto.press('enter')
        time.sleep(1)
        auto.click(x=16, y=610)
        time.sleep(2)
        auto.click(x=31, y=487)

    #botões que apareceram na tela, aonde cada um deles puxa uma função
    codar_button = ft.Container(
        content=ft.ElevatedButton(text="CODAR", width=150, on_click=codar)
    )
    estudar_button = ft.Container(
        content=ft.ElevatedButton(text="ESTUDAR", width=150, on_click=estudar)
    )
    deboa_button = ft.Container(
        content=ft.ElevatedButton(text="DE BOA", width=150, on_click=deboa)
    )
    youtube_button = ft.Container(
        content=ft.ElevatedButton(text="YOUTUBE", width=150, on_click=youtube)
    )
    discord_button = ft.Container(
        content=ft.ElevatedButton(text="DISCORD", width=150, on_click=discord)
    )
    whatsapp_button = ft.Container(
        content=ft.ElevatedButton(
            text="WHATSAPP", width=150, on_click=whatsapp)
    )
    gravartela_button = ft.Container(
        content=ft.ElevatedButton(
            text="GRAVAR TELA", width=150, on_click=gravartela)
    )
    vscode_button = ft.Container(
        content=ft.ElevatedButton(
            text="VSCODE", width=150, on_click=abrir_vscode)
    )
    screnshoot_button = ft.Container(
        content=ft.ElevatedButton(
            text="SCRENSHOOT", width=150, on_click=screnshoot)
    )

    #adicionando os botões na tela
    page.add(codar_button, estudar_button, deboa_button, youtube_button, discord_button,
             whatsapp_button, gravartela_button, vscode_button, screnshoot_button)

#informando que o app ira rodar com base na funcao principal
ft.app(principal)
