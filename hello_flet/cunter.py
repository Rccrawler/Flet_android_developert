import flet as ft
import time

def mian(page: ft.Page):

    number = 0

    page.title = "Contador con flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value =f"0", text_align=ft.TextAlign.CENTER, width = 100)

    def minus(e):
        #number -= 1
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus(e):
        #number += 1
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus),
                #ft.TextField(value = "0", text_align=ft.TextAlign.CENTER, width = 100),  manera de escribir texto
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    for i in range(5):
        txt_number.value = f"Step {i}"	# Cambia el valor del TextField
        page.update()	# Actualiza la página
        time.sleep(1)	# Espera 1 segundo

ft.app(mian)