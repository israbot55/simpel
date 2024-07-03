import flet as ft
import telebot
import requests
import threading

TOKEN = '6891427112:AAGQvxx1lEO6v8TJAFuvM7rCFtY6zcHAHf8'  # Replace with your actual bot token

bot = telebot.TeleBot(TOKEN)


def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json().get('ip')


@bot.message_handler(commands=['start'])
def send_ip(message):
    ip_address = get_ip()
    bot.reply_to(message, f'Your IP address is: {ip_address}')


def run_bot():
    bot.polling()


def main(page: ft.Page):
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton("Minus", on_click=minus_click),
                txt_number,
                ft.ElevatedButton("Plus", on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)