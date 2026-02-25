from dataclasses import dataclass

import flet as ft


@dataclass
class Message:  # noqa: B903
    user_name: str
    text: str
    message_type: str


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(
                    self.get_initials(self.message.user_name),
                    weight=ft.FontWeight.BOLD,
                    size=13,
                ),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user_name),
                radius=20,
            ),
            ft.Column(
                tight=True,
                spacing=3,
                controls=[
                    ft.Text(self.message.user_name, weight=ft.FontWeight.BOLD, size=13),
                    ft.Container(
                        content=ft.Text(self.message.text, selectable=True, size=14, color=ft.Colors.BLACK87),
                        bgcolor="#DDEEFF",
                        border_radius=ft.border_radius.only(top_left=2, top_right=12, bottom_left=12, bottom_right=12),
                        padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        border=ft.Border.all(1, "#B0CDE8"),
                    ),
                ],
            ),
        ]

    def get_initials(self, user_name: str):
        # Devuelve la inicial del nombre en mayúscula
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "?"

    def get_avatar_color(self, user_name: str):
        # Asigna un color de avatar según el nombre del usuario
        colores = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colores[hash(user_name) % len(colores)]


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Chat"
    page.bgcolor = ft.Colors.GREY_100

    def unirse_al_chat(e):
        if not nombre_usuario.value:
            nombre_usuario.error_text = "¡El nombre no puede estar en blanco!"
            nombre_usuario.update()
        else:
            page.session.store.set("user_name", nombre_usuario.value)
            dialogo_bienvenida.open = False
            nuevo_mensaje.prefix = ft.Text(f"{nombre_usuario.value}: ")
            page.pubsub.send_all(
                Message(
                    user_name=nombre_usuario.value,
                    text=f"{nombre_usuario.value} se ha unido al chat.",
                    message_type="login_message",
                )
            )

    async def enviar_mensaje(e):
        if nuevo_mensaje.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.store.get("user_name"),
                    nuevo_mensaje.value,
                    message_type="chat_message",
                )
            )
            nuevo_mensaje.value = ""
            await nuevo_mensaje.focus()

    def al_recibir_mensaje(message: Message):
        # Muestra el mensaje según su tipo
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK_45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(al_recibir_mensaje)

    # Campo para ingresar el nombre al unirse
    nombre_usuario = ft.TextField(
        label="Ingresa tu nombre para unirte al chat",
        autofocus=True,
        on_submit=unirse_al_chat,
        border_radius=8,
    )

    # Diálogo de bienvenida
    dialogo_bienvenida = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("¡Bienvenido! "),
        content=ft.Column([nombre_usuario], width=300, height=70, tight=True),
        actions=[ft.Button(content="Unirse al chat", on_click=unirse_al_chat)],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=12),
    )

    page.overlay.append(dialogo_bienvenida)

    # Lista de mensajes del chat
    chat = ft.ListView(
        expand=True,
        spacing=12,
        padding=ft.padding.symmetric(horizontal=8, vertical=10),
        auto_scroll=True,
    )

    # Campo para escribir un nuevo mensaje
    nuevo_mensaje = ft.TextField(
        hint_text="Escribe un mensaje...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        border_radius=20,
        on_submit=enviar_mensaje,
    )

    # Layout principal
    page.add(
        ft.Container(
            content=chat,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=10,
            padding=10,
            expand=True,
            bgcolor=ft.Colors.BLACK,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    nuevo_mensaje,
                    ft.IconButton(
                        icon=ft.Icons.SEND_ROUNDED,
                        tooltip="Enviar mensaje",
                        icon_color=ft.Colors.GREEN,
                        on_click=enviar_mensaje,
                    ),
                ]
            ),
            padding=ft.padding.symmetric(vertical=6),
        ),
    )
ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    host="0.0.0.0",
    port=8000,
)