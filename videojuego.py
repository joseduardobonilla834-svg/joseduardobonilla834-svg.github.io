import tkinter as tk
import time
import threading
from datetime import datetime

# Fecha desde que empezó el amor
inicio_amor = datetime(2024, 6, 17, 0, 0, 0)

# Corazón dibujado
corazon_dibujo = [
    "       ❤     ❤     ❤     ❤       ",
    "     ❤❤❤   ❤❤❤   ❤❤❤   ❤❤❤     ",
    "    ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤    ",
    "   ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤   ",
    "    ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤    ",
    "     ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤     ",
    "      ❤❤❤❤❤❤❤❤❤❤❤❤❤      ",
    "       ❤❤❤❤❤❤❤❤❤❤❤       ",
    "        ❤❤❤❤❤❤❤❤❤        ",
    "         ❤❤❤❤❤❤❤         ",
    "          ❤❤❤❤❤          ",
    "           ❤❤❤           ",
    "            ❤            "
]

mensajes = [
    "Hola... 💌",
    "Solo quería decirte algo muy especial...",
    "Desde que te conocí, mi mundo cambió por completo. 🌍❤",
    "Eres como ese error en mi código que no quiero arreglar... porque me encanta. 🧠💘",
    "¿Me permites ser la variable constante en tu vida?",
    "print('Te amo ❤')"
]

# Crear ventana
ventana = tk.Tk()
ventana.title("💘 Declaración de Amor")
ventana.geometry("700x750")
ventana.configure(bg="#fff0f5")

# Widgets principales
texto = tk.Label(ventana, text="", font=("Courier New", 16), bg="#fff0f5", wraplength=650, justify="center")
texto.pack(pady=20)

contador_label = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#fff0f5", fg="red")
contador_label.pack(pady=10)
contador_label.pack_forget()

pregunta_label = tk.Label(ventana, text="", font=("Arial", 16), bg="#fff0f5", fg="#333")
pregunta_label.pack(pady=15)

botones_frame = tk.Frame(ventana, bg="#fff0f5")
botones_frame.pack()
botones_frame.pack_forget()

corazon_label = tk.Label(ventana, text="", font=("Arial", 48), bg="#fff0f5", fg="red")
corazon_label.pack(pady=30)
corazon_label.pack_forget()

mensaje_final = tk.Label(ventana, text="", font=("Arial", 20, "bold"), bg="#fff0f5", fg="hotpink")
mensaje_final.pack(pady=20)
mensaje_final.pack_forget()

# Botón de inicio
def comenzar():
    boton_inicio.config(state="disabled")
    boton_inicio.pack_forget()
    threading.Thread(target=mostrar_mensaje_romantico, daemon=True).start()

boton_inicio = tk.Button(ventana, text="Haz clic para leer 💌", font=("Arial", 14), bg="#ff69b4", fg="white", command=comenzar)
boton_inicio.pack(pady=10)

# Función del contador
def actualizar_contador():
    while True:
        ahora = datetime.now()
        delta = ahora - inicio_amor
        dias = delta.days
        horas, resto = divmod(delta.seconds, 3600)
        minutos, segundos = divmod(resto, 60)
        contador_label.config(
            text=f"💖 Te amo desde hace: {dias} días, {horas} horas, {minutos} minutos, {segundos} segundos")
        time.sleep(1)

# Función para escribir letra por letra
def escribir_lento(mensaje):
    texto.config(text="")
    for letra in mensaje:
        texto["text"] += letra
        time.sleep(0.05)

# Mostrar secuencia romántica
def mostrar_mensaje_romantico():
    for msg in mensajes:
        escribir_lento(msg)
        time.sleep(1.5)

    escribir_lento("\n".join(corazon_dibujo))
    time.sleep(1.5)

    contador_label.pack()
    threading.Thread(target=actualizar_contador, daemon=True).start()

    pregunta_label.config(text="¿Aceptas compilar esta historia conmigo? 💍")
    botones_frame.pack()

# Respuesta "Sí"
def respuesta_si():
    boton_inicio.pack_forget()
    texto.pack_forget()
    pregunta_label.pack_forget()
    botones_frame.pack_forget()
    contador_label.pack_forget()
    mensaje_final.pack_forget()

    corazon_label.pack()

    def animar():
        for _ in range(6):
            corazon_label.config(text="❤", font=("Arial", 40))
            time.sleep(0.3)
            corazon_label.config(text="💖", font=("Arial", 48))
            time.sleep(0.3)
        corazon_label.config(text="")
        corazon_label.pack_forget()
        mensaje_final.config(text="Te amo mi vida", fg="hotpink")
        mensaje_final.pack()

    threading.Thread(target=animar, daemon=True).start()

# Respuesta "No"
def respuesta_no():
    boton_inicio.pack_forget()
    texto.pack_forget()
    pregunta_label.pack_forget()
    botones_frame.pack_forget()
    contador_label.pack_forget()
    mensaje_final.config(text="No te preocupes, acepto tu decisión", fg="#444")
    mensaje_final.pack()

# Botones de respuesta
btn_si = tk.Button(botones_frame, text="Sí 💘", font=("Arial", 14), bg="#32cd32", fg="white", command=respuesta_si)
btn_si.pack(side="left", padx=20)

btn_no = tk.Button(botones_frame, text="No 💔", font=("Arial", 14), bg="#ff4444", fg="white", command=respuesta_no)
btn_no.pack(side="right", padx=20)

# Iniciar ventana principal
ventana.mainloop()