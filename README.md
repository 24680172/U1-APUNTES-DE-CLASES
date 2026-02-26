# **UNIDAD 1**

## 1.1 Interfaz gráfica de usuario

  La Interfaz gráfica de usuario (GUI) es uno de los tipos de Interfaces de usuario (UI) que existen, por lo tanto, de general a particular, iremos viendo primero que es una UI para así poder posicionar y adentrarnos en la GUI. 

**¿Qué es una Interfaz de usuario (UI)?**

  La Interfaz del usuario es el diseño que los usuarios ven y con el que interactúan para poder navegar por un sitio web, app.… Incluye diseños intuitivos que hacen que los clientes queden contentos con la experiencia. En cambio, los sitios que no dan una experiencia positiva alejan a los clientes, porque sus plataformas son difíciles de entender o no cumplen sus necesidades. 

**Los 3 tipos de Interfaces de usuario que existen**

  Una interfaz de usuario consta de dos partes: el lenguaje de presentación, que se refiere a la transacción del ordenador hacia la persona, y el lenguaje deacción, que se caracteriza por ser la interacción de la persona hacia el ordenador. Existen 3 tipos de Interfaces: 

1. **Interfaz de lenguaje natural**

  Las interfaces de lenguaje natural permiten la comunicación entre humanos y máquinas en un lenguaje cotidiano y natural. Es decir, no se requieren habilidades especiales del usuario para controlarla. Un ejemplo es Alexa, que cuenta con un software basado en modelos acústicos y del lenguaje. 

2. **Interfaz de preguntas y respuestas**

  Una de las interfaces que más utilizan por los usuarios es la interfaz de preguntas y respuestas. En ella el ordenador muestra en la pantalla una pregunta al usuario. Para interactuar, el usuario ingresa una respuesta (a través de un golpe de teclado o un clic del mouse), y el ordenador actúa sobre esa información de una manera pre-programada, generalmente pasando a la siguiente pregunta. Los asistentes usados para instalar software son un ejemplo común de una Interfaz de pregunta y respuesta. El usuario responde las preguntas acerca del proceso de instalación, como por ejemplo: dónde instalar el software o sus características.  

3. **Interfaz gráfica de usuario**

  La Interfaz gráfica de usuario, conocida también como GUI (del inglés graphical user interface),utiliza imágenes, iconos y menús para mostrar las acciones disponibles en un dispositivo, entre las que el usuario puede escoger una o varias. 

**¿Qué es la Interfaz gráfica de usuario (IGU)?**

  La Interfaz gráfica de usuario, conocida también como GUI (Graphical user interface) es el entorno que utiliza un conjunto de imágenes y objetos gráficos para representar información y acciones disponibles en la interfaz mediante las cuales una máquina y el usuario interactúan. Surge como evolución de las Interfaces de línea de comandos que se usaban para operar los primeros sistemas operativos y es pieza fundamental de un entorno gráfico.Ejemplos: Windows, Linux o Mac OS. A mediados de los setenta las GUI comenzaron a sustituir a las Interfaces de línea de comando(CLI), y esto permitió que la interacción con las computadoras fuera más sencilla e intuitiva. Aquí podemos ver la diferencia entre una Interfaz de línea de comando y una Interfaz gráfica de usuario de manera sencilla:  

  Antes de que se desarrollaran y popularizaron las GUI, solo las personas con conocimientos profundos de informática podían usar un computador, pero las interfaces gráficas sustituyeron la complejidad de los comandos por acciones predeterminadas, simbolizadas por elementos visuales muy sencillos de comprender. Los precursores de la Interfaz gráfica de usuario fueron los investigadores de Stanford Research Institute liderados por Douglas Engelbart, desarrollaron una Interfaz de hipervínculos en modo de texto utilizada mediante un ratón en 1973. A mediados de los 80 Mac se convirtió en el referente de las Interfaces gráficas amigables con funciones muy complejas, pero: “tan fáciles de usar como una tostadora”. Este término fue ampliado, definiendo los conceptos de ventana, botones, menús y el puntero del ratón. Más tarde, se incluyeron los iconos, carpetas, la red Ethernet y el correo electrónico entre otros. Por último, con la aparición de nuevas tecnologías se han implementado en realidad virtual o pantallas táctiles. Una buena GUI no solo es importante para los programas, sistemas operativos y aplicaciones. Se estima que el 68% de los visitantes que abandonan un sitio web lo hacen debido a que la experiencia de usuario, incluyendo la Interfaz, no está optimizada para sus necesidades y expectativas. 

**¿Quiénes son los responsables de una IGU?**

 Detrás de cualquier Interfaz gráfica de usuario existe un programa, sistema operativo o aplicación. Por eso, la GUI suele ser un trabajo en conjunto entre desarrolladores y diseñadores. Sin embargo, quienes suelen dedicarse a esta tarea son los expertos en User Interface que buscan la mejor manera de que el usuario pueda interactuar con el programa, mediante elementos visuales fáciles de comprender. 

 ## **1.1 Creación de interfaz gráfica para usuarios**
La creación de una interfaz gráfica para usuarios (GUI) en Python permite desarrollar aplicaciones visuales con botones, ventanas, campos de texto, menús, etc.

Las librerías más utilizadas son:

- Tkinter (incluida en Python, ideal para principiantes)

- PyQt / PySide (más profesional y potente)

- Kivy (para aplicaciones multitáctiles y móviles)

- CustomTkinter (versión moderna de Tkinter)

### 1. Crear una interfaz gráfica básica con Tkinter

Tkinter viene instalada por defecto en Python.

Ejemplo: Ventana con botón
```python
import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Saludo", "¡Hola, usuario!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi primera interfaz")
ventana.geometry("300x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a la aplicación")
etiqueta.pack(pady=10)

# Crear botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
```

### 2. Interfaz con campo de texto
```python
import tkinter as tk
from tkinter import messagebox

def mostrar_nombre():
    nombre = entrada.get()
    messagebox.showinfo("Nombre", f"Hola {nombre}")

ventana = tk.Tk()
ventana.title("Ingreso de datos")
ventana.geometry("300x200")

tk.Label(ventana, text="Ingresa tu nombre:").pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Enviar", command=mostrar_nombre).pack(pady=10)

ventana.mainloop()
```
### 3. Interfaz moderna con CustomTkinter (opcional)

Instalar primero:
```
pip install customtkinter
```
Ejemplo:
```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("300x200")
app.title("Interfaz Moderna")

label = ctk.CTkLabel(app, text="Hola Usuario")
label.pack(pady=20)

button = ctk.CTkButton(app, text="Salir", command=app.quit)
button.pack(pady=10)

app.mainloop()
```

| Componente | Función             |
|------------|---------------------|
| Label      | Mostrar texto       |
| Button     | Botón interactivo   |
| Entry      | Campo de texto      |
| Frame      | Contenedor          |
| Menu       | Barra de menú       |
| MessageBox | Ventanas emergentes |

Estructura básica de una GUI

- Crear ventana principal

- Configurar tamaño y título

- Agregar widgets (componentes)

- Definir funciones

- Ejecutar mainloop()

Ejemplo práctico: Calculadora simple en FLET:
``` python
import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )


    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=200,
        expand=False
    )


    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.PRIMARY, border_radius=8))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.SECONDARY, border_radius=8))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.TERTIARY, border_radius=8))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.ERROR, border_radius=8))


    layout_principal = ft.Column(
        controls=[
            display,
            grid
        ],
        tight=True,
    )

    page.add(layout_principal)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
```
Visualización:

<img width="666" height="490" alt="image" src="https://github.com/user-attachments/assets/ad6ceeb0-a65e-4d25-a976-4dd3d8e1fb14" />

 ## **1.2 Tipos de eventos**
 En Flet, los eventos son acciones que ocurren en la interfaz de usuario (como hacer clic en un botón o escribir en un campo de texto) y que activan funciones específicas llamadas Event Handlers. 
A continuación se presentan los tipos principales de eventos clasificados por su origen y comportamiento:
1. Eventos de Interacción Comunes

Son los que se encuentran en la mayoría de los controles básicos:

- on_click: Se dispara cuando el usuario hace clic o toca un control (botones, iconos, contenedores).

- on_change: Ocurre cuando el valor de un control cambia, como al escribir en un TextField o seleccionar una opción en un Dropdown.

- on_submit: Específico de campos de texto (TextField), se activa cuando el usuario presiona la tecla Enter. 

2. Eventos de Ratón y Puntero
Permiten detectar interacciones más precisas con el mouse:

- on_hover: Se activa cuando el puntero del ratón entra o sale del área de un control (disponible en Container).

- on_long_press: Se dispara tras mantener presionado un control por un tiempo prolongado. 

3. Eventos de Ciclo de Vida y Aplicación

Gestionan el estado global de la aplicación o de la página:
- on_route_change: Se activa cuando la URL o la ruta de la aplicación cambia (fundamental para navegación).

- on_view_pop: Ocurre cuando el usuario intenta retroceder en la navegación (ej. botón "atrás" del navegador).

- on_keyboard_event: Detecta pulsaciones de teclas globales en la página, útil para atajos de teclado.

- on_resize: Se dispara cuando el usuario cambia el tamaño de la ventana de la aplicación.

- on_close: Útil para ejecutar acciones justo antes de que se cierre una ventana o diálogo. 

4. Eventos Especializados

- Drag & Drop: Eventos como on_will_accept, on_accept y on_leave para gestionar el arrastre de elementos entre controles Draggable y DragTarget.

- Animaciones: Eventos que se activan al finalizar una animación de control.

Para implementar cualquier evento, debes asignar una función al atributo correspondiente del control:


```python
import flet as ft

def main(page: ft.Page):
    def al_hacer_clic(e):
        page.add(ft.Text("¡Botón presionado!"))

    page.add(ft.ElevatedButton("Haz clic aquí", on_click=al_hacer_clic))

ft.app(target=main)
```

ejemplo Práctico: Calculadora.py
```python
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
```
 ## **1.3 Manejo de eventos**
 El manejo de eventos es el núcleo de la interactividad en Flet. A diferencia de otros frameworks que requieren configuraciones complejas, Flet utiliza un modelo basado en callbacks donde los controles de la interfaz "notifican" al código Python cuando ocurre una acción del usuario. 

**La Anatomía de un Evento en Flet**

Cuando un usuario interactúa con un control (por ejemplo, al pulsar un ElevatedButton), Flet genera un objeto de tipo ControlEvent. Este objeto es enviado automáticamente como argumento a la función que hayamos definido como manejador (event handler). 

El objeto ControlEvent contiene propiedades críticas:

- control: Una referencia al control exacto que disparó el evento.

- data: Información adicional sobre el evento (como el texto ingresado en un buscador o las coordenadas de un clic).

- name: El nombre del evento (por ejemplo, "click" o "change").

- page: Una referencia a la página donde reside el control. 

**Estrategias de Implementación**

Existen tres formas principales de conectar eventos con lógica en Python:

1.Funciones Nombradas (Recomendado): Se define una función estándar y se asigna al atributo del control. Es la forma más limpia y legible.
```python
def al_hacer_clic(e):
    e.control.text = "¡Clickeado!"
    page.update()

boton = ft.ElevatedButton("Púlsame", on_click=al_hacer_clic)
```

2. Funciones Lambda: Útiles para pasar parámetros adicionales que no están presentes en el objeto del evento original.
```python
on_click=lambda e: mi_funcion(e, "parámetro_extra")
```

3.Métodos de Clase: Cuando se crean controles personalizados heredando de clases de Flet, los manejadores suelen ser métodos internos. 

**El Ciclo de Vida: Captura y Actualización**

Un error común es olvidar que Flet requiere una actualización explícita. Cuando un evento modifica el estado de un control (cambia su color, texto o visibilidad), los cambios no se reflejan en la pantalla del usuario hasta que se llama a page.update() o control.update(). Este diseño optimiza el rendimiento al agrupar múltiples cambios en un solo envío de datos a la interfaz. 

**Gestión de Eventos Globales y de Página**

No todos los eventos nacen de botones. La clase Page permite manejar situaciones que afectan a toda la aplicación:

- Atajos de Teclado: Mediante page.on_keyboard_event, se pueden capturar combinaciones como Ctrl+S para guardar datos globalmente.

- Cambios de Ruta: on_route_change es esencial para aplicaciones de varias páginas, permitiendo cargar diferentes vistas según la URL.

- Redimensionamiento: on_resize permite adaptar el diseño de forma dinámica cuando el usuario cambia el tamaño de la ventana. 

**Manejo Asíncrono**

Flet brilla en el manejo de eventos asíncronos (async/await). Esto es vital para aplicaciones que realizan peticiones web o procesos pesados sin "congelar" la interfaz. Al usar async def main(page: ft.Page), los manejadores de eventos también pueden ser funciones async, permitiendo una fluidez total mientras se espera una respuesta del servidor o una base de datos. 

Consideraciones de Depuración
Es fundamental evitar ejecutar la función al asignarla. Un error frecuente en la comunidad es escribir on_click=mi_funcion() (con paréntesis), lo que ejecuta la lógica al iniciar la app en lugar de esperar al clic. La asignación correcta siempre debe ser la referencia a la función: on_click=mi_funcion.

## **1.4 Manejo de componentes gráficos de control**

En Flet, el Manejo de Componentes Gráficos de Control se refiere a la gestión de los elementos visuales (llamados Controls) que permiten construir la interfaz de usuario. A diferencia de otros frameworks, Flet no dibuja píxeles manualmente, sino que utiliza controles de Flutter de alto nivel para renderizar la interfaz de forma profesional y nativa.

**1. Categorización de los Componentes**
Para un manejo eficiente, los componentes se dividen según su propósito:

- Controles de Entrada (Input): Permiten capturar datos del usuario. Ejemplos: TextField (texto), Checkbox (booleano), Dropdown (selección) y Slider (rango numérico).

- Controles de Visualización: Muestran información sin interacción directa o con interacción limitada. Ejemplos: Text, Image, Icon, Markdown y CircleAvatar.

- Controles de Diseño (Layout): Son esenciales para organizar el espacio.
  - Lineales: Row (horizontal) y Column (vertical).
  - Contenedores: Container (permite bordes, sombras y márgenes) y Stack (superpone elementos).
  - Listas: ListView y GridView para manejar grandes volúmenes de datos con desplazamiento.

**2. Jerarquía y Propiedades del Control**

Cada componente en Flet es un objeto Python. El manejo técnico implica manipular sus propiedades clave:

- ref: El uso de ft.Ref() permite acceder a un componente después de haberlo definido sin necesidad de variables globales.

- visible y disabled: Propiedades booleanas que controlan si el usuario puede ver o interactuar con el componente.

- expand: Determina si un componente debe ocupar todo el espacio disponible dentro de un contenedor flexible.

**3. Actualización de la Interfaz (The State)**

El manejo gráfico no es estático. Flet utiliza un modelo donde el estado del componente reside en el servidor (o script de Python) y se sincroniza con el cliente (la ventana):
1.Se modifica una propiedad (ej. mi_texto.value = "Nuevo Texto").
2.Se llama a page.update() o mi_texto.update().
3.Flet envía solo el "delta" (el cambio) para optimizar el rendimiento.

## Practica 1: calculadora mejorada
```python
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
```
este código implementa una calculadora funcional con lógica aritmética.

- Creación de interfaz: Organiza la calculadora en secciones visuales bien definidas: seccion_display, seccion_numeros y seccion_operaciones.

- Tipos de eventos: Utiliza el evento on_click para capturar tanto números como operadores.

- Manejo de eventos: * Implementa funciones de manejo de datos (numero_click y operacion_click) que modifican variables locales (numero_actual, expresion).
  - Al presionar "=", utiliza la función eval() de Python para procesar la cadena de texto de la expresión y mostrar el resultado en el control display.

- Manejo de componentes: Emplea contenedores dinámicos (ft.Container) creados mediante funciones para asignarles una propiedad data única a cada botón, facilitando la identificación del botón presionado durante el evento.

<img width="1552" height="806" alt="image" src="https://github.com/user-attachments/assets/c01b72c5-110e-4c22-b25d-5b57d4a34302" />


## Practica 2:  CHAT
```python
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
```
Este archivo es el más complejo en cuanto a la interacción y el manejo de estados de usuario.

- Creación de interfaz: Utiliza un ft.AlertDialog (ventana emergente) para forzar al usuario a registrarse antes de ver el contenido principal.

- Tipos de eventos: * on_submit: El evento ocurre cuando el usuario presiona "Enter" en los campos de texto del nombre o del mensaje.
  - on_click: El botón de enviar (ft.IconButton) dispara la lógica de envío al hacer clic.

- Manejo de eventos: Define funciones asíncronas como enviar_mensaje(e) para procesar la entrada de datos. Además, implementa page.pubsub.subscribe, un manejador de eventos especial que permite que todos los usuarios conectados reciban los mensajes en tiempo real.

- Manejo de componentes: Se crean componentes personalizados mediante Programación Orientada a Objetos (class ChatMessage) para encapsular el diseño de cada burbuja de chat, incluyendo avatares con colores dinámicos.
<img width="1908" height="952" alt="image" src="https://github.com/user-attachments/assets/3c3b8c1c-3c3f-429a-a8fe-dbcfc3eb5b7c" />

## Practica 3: Formulario
```python
import flet as ft

def main(page: ft.Page):
    # ---------------- CONFIGURACIÓN ----------------
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#000000"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # ---------------- CONTROLES ----------------
    txt_nombre = ft.TextField(label="Nombre", border_color="#F200FF", expand=True)
    txt_control = ft.TextField(label="Número de control", border_color="#F200FF", expand=True)
    txt_email = ft.TextField(label="Email", border_color="#F200FF")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#F200FF",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#F200FF",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # ---------------- RADIO BUTTON GÉNERO ----------------
    genero_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro"),
        ])
    )

    # ---------------- MENSAJE DE RESULTADO ----------------
    txt_resultado = ft.Text("", color="green", weight=ft.FontWeight.BOLD)

    # ---------------- FUNCIÓN ENVIAR ----------------
# ---------------- FUNCIÓN ENVIAR ----------------
    def enviar_click(e):
        # 1. Validación de campos vacíos
        if (
            not txt_nombre.value or
            not txt_control.value or
            not txt_email.value or
            not dd_carrera.value or
            not dd_semestre.value or
            not genero_group.value
        ):
            txt_resultado.value = " ¡¡Por favor completa todos los campos!!"
            txt_resultado.color = "red"
        
        # 2. NUEVA VALIDACIÓN: Verificar si contiene el '@'
        elif "@" not in txt_email.value:
            txt_resultado.value = " El email no es válido (falta el '@')"
            txt_resultado.color = "red"
            
        else:
            # Si pasa todas las validaciones
            txt_resultado.value = (
                f"Registro exitoso\n"
                f"Nombre: {txt_nombre.value}\n"
                f"Control: {txt_control.value}\n"
                f"Email: {txt_email.value}\n"
                f"Carrera: {dd_carrera.value}\n"
                f"Semestre: {dd_semestre.value}\n"
                f"Género: {genero_group.value}"
            )
            txt_resultado.color = "white"

            # Limpiar campos
            txt_nombre.value = ""
            txt_control.value = ""
            txt_email.value = ""
            txt_nombre.value = ""
            dd_carrera.value = None
            dd_semestre.value = None
            genero_group.value = None

        page.update()

    # ---------------- BOTÓN ----------------
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=400,
        on_click=enviar_click
    )

    # ---------------- INTERFAZ ----------------
    page.add(
        ft.Column([
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            ft.Text("Género:", color="#4D2A32", weight=ft.FontWeight.BOLD),
            genero_group,
            btn_enviar,
            txt_resultado
        ], spacing=15)
    )

# Ejecutar en navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
Este código se centra en la captura de datos y la validación de formularios.

- Creación de interfaz: La disposición se basa en una ft.Column con un espaciado de 15 píxeles entre controles para mantener la limpieza visual.

- Tipos de eventos: El evento principal es el on_click del botón btn_enviar.

- Manejo de eventos: La función enviar_click(e) contiene lógica condicional (validación). Verifica si los campos están vacíos o si el email tiene el formato correcto (presencia de "@") antes de mostrar el resultado.

- Manejo de componentes: * TextField: Para entrada de texto libre.
  - Dropdown: Para selección limitada (carreras y semestres).
  - RadioGroup: Para opciones excluyentes donde solo se puede seleccionar un género a la vez.

<img width="1919" height="996" alt="image" src="https://github.com/user-attachments/assets/cbf95f51-8de3-4654-9158-c6d74599d7b4" />

# BIBLIOGRAFÍAS

Flet Team. (2025). Event - Flet docs. Recuperado de la documentación oficial de Flet.

Flet Team. (2025). Async apps - Flet docs. Recuperado de la sección de recetas avanzadas de Flet.

Flet Team. (2024). Introducing Declarative UI in Flet. Blog oficial de Flet.

The Bridge. (s. f.). Consejos para el diseño de interfaz de usuario. Recuperado el 25 de febrero de 2026, de Interfaz de usuario – The Bridge
