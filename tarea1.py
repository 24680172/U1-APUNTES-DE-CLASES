import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estatica - TAP"
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False
    page.padding = 20

    numero_actual = ""
    expresion = ""

    # DISPLAY
    display = ft.Text("0", size=30, weight=ft.FontWeight.BOLD)

    seccion_display = ft.Container(
        content=display,
        bgcolor=ft.Colors.BLACK12,
        height=80,
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(2, ft.Colors.RED)
    )

    # -------- FUNCION NUMEROS --------
    def numero_click(e):
        nonlocal numero_actual, expresion

        numero_actual += e.control.data
        display.value = expresion + numero_actual
        page.update()

    # -------- FUNCION OPERACIONES --------
    def operacion_click(e):
        nonlocal numero_actual, expresion

        simbolo = e.control.data

        if simbolo == "=":
            if numero_actual != "":
                expresion += numero_actual

            try:
                resultado = eval(expresion)
                display.value = str(resultado)

                # Permite seguir operando con el resultado
                expresion = ""
                numero_actual = str(resultado)

            except:
                display.value = "Error"
                expresion = ""
                numero_actual = ""

        else:  # operador +
            if numero_actual != "":
                expresion += numero_actual + " " + simbolo + " "
                numero_actual = ""

            display.value = expresion

        page.update()

    # -------- BOTONES --------
    def boton_numero(numero):
        return ft.Container(
            content=ft.Text(
                str(numero),
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            alignment=ft.alignment.Alignment(0, 0),
            expand=1,
            height=70,
            bgcolor=ft.Colors.BLUE_600,
            border_radius=10,
            data=str(numero),
            on_click=numero_click
        )

    def boton_operacion(simbolo):
        return ft.Container(
            content=ft.Text(
                simbolo,
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            alignment=ft.alignment.Alignment(0, 0),
            expand=1,
            height=60,
            bgcolor=ft.Colors.GREEN_600,
            border_radius=10,
            data=simbolo,
            on_click=operacion_click
        )

    # -------- SECCIONES --------
    seccion_numeros = ft.Column(
        controls=[
            ft.Row([boton_numero(7), boton_numero(8), boton_numero(9)]),
            ft.Row([boton_numero(4), boton_numero(5), boton_numero(6)]),
            ft.Row([boton_numero(1), boton_numero(2), boton_numero(3)]),
        ],
        spacing=10
    )

    seccion_operaciones = ft.Row(
        controls=[
            boton_operacion("+"),
            boton_operacion("="),
        ],
        spacing=10
    )

    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:"),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:"),
                seccion_operaciones,
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)