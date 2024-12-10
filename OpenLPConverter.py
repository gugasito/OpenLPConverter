import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def convertir_xml_a_txt_con_verse_order(xml_file, output_folder, progress_callback, total_files, current_file):
    with open(xml_file, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Extraer el título de la etiqueta <title>
    if '<title>' in contenido and '</title>' in contenido:
        titulo = contenido.split('<title>')[1].split('</title>')[0]
    else:
        titulo = "Untitled"  # Si no se encuentra la etiqueta <title>, usar un título por defecto

    # Verificar si existe la etiqueta <verseOrder> y tiene contenido
    if '<verseOrder>' in contenido and '</verseOrder>' in contenido:
        verse_order_raw = contenido.split('<verseOrder>')[1].split('</verseOrder>')[0]
        verse_order = verse_order_raw.split() if verse_order_raw.strip() else []
    else:
        # Si no existe <verseOrder>, seguir el orden que está en el XML
        verse_order = []

    # Extraer versos y reemplazar etiquetas <br/> por saltos de línea
    versos_raw = contenido.split('<lyrics>')[1].split('</lyrics>')[0]
    versos = {}
    for verso in versos_raw.split('<verse name='):
        if '<lines>' in verso:
            nombre = verso.split('"')[1]  # Extraer el nombre del verso (e.g., i1, v1a)
            texto = verso.split('<lines>')[1].split('</lines>')[0].replace('<br/>', '\n')  # Reemplazar <br/>
            base_name = nombre.rstrip('abcdefghijklmnopqrstuvwxyz')  # Agrupar versos con sufijos (e.g., v1a, v1b)
            if base_name not in versos:
                versos[base_name] = texto
            else:
                versos[base_name] += f'\n\n{texto}'

    # Si no hay verseOrder, usar el orden en el que aparecen los versos
    if not verse_order:
        verse_order = list(versos.keys())  # Usar las claves de 'versos' como el orden

    # Generar contenido del archivo TXT basado en verseOrder
    contenido_txt = f"Title: {titulo}\n\n"  # Incluir el título en el archivo TXT
    for nombre in verse_order:
        if nombre in versos:
            contenido_txt += versos[nombre] + '\n\n'

    # Usar el nombre del archivo XML para el archivo TXT
    base_name = os.path.basename(xml_file)
    txt_name = os.path.splitext(base_name)[0] + ".txt"
    output_file = os.path.join(output_folder, txt_name)

    # Guardar el archivo TXT en la carpeta de destino
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(contenido_txt.strip())

    # Actualizar la barra de progreso
    progress_callback(current_file, total_files)
    print(f"Archivo generado: {output_file}")

def actualizar_progreso(current, total, progress_bar, label):
    # Calcular el porcentaje de progreso
    progreso = (current / total) * 100
    progress_bar['value'] = progreso
    label.config(text=f"Procesando... {int(progreso)}%")
    # Actualizar la interfaz de usuario
    progress_bar.update()

def iniciar_proceso():
    # Seleccionar archivos XML
    archivos = filedialog.askopenfilenames(
        title="Selecciona los archivos XML",
        filetypes=[("Archivos XML", "*.xml")])
    if not archivos:
        messagebox.showwarning("Advertencia", "No se seleccionaron archivos.")
        return

    # Seleccionar carpeta de destino
    carpeta_destino = filedialog.askdirectory(title="Selecciona la carpeta de destino")
    if not carpeta_destino:
        messagebox.showwarning("Advertencia", "No se seleccionó una carpeta de destino.")
        return

    # Crear ventana para la barra de progreso
    progress_window = tk.Toplevel()
    progress_window.title("Progreso de Conversión")
    progress_window.geometry("400x150")
    centrar_ventana(progress_window)

    # Establecer el icono de la ventana de progreso (opcional)
    progress_window.iconbitmap("logo.ico")  # Reemplaza "icono.ico" con la ruta a tu ícono

    # Etiqueta y barra de progreso
    label = tk.Label(progress_window, text="Procesando... 0%", font=("Arial", 14))
    label.pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate", maximum=100)
    progress_bar.pack(pady=20)

    # Procesar archivos
    total_files = len(archivos)
    for i, archivo in enumerate(archivos, 1):
        convertir_xml_a_txt_con_verse_order(archivo, carpeta_destino, lambda current, total: actualizar_progreso(current, total, progress_bar, label), total_files, i)

    progress_window.destroy()  # Cerrar la ventana de progreso después de terminar
    messagebox.showinfo("Éxito", "Todos los archivos han sido procesados.")

def centrar_ventana(ventana):
    # Centrar la ventana en la pantalla
    ventana.update_idletasks()  # Actualizar la ventana para obtener sus dimensiones
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    posicion_x = (ancho_pantalla - ancho_ventana) // 2
    posicion_y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}')

def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Conversor de Canciones XML a TXT")
    root.geometry("800x800")
    root.resizable(False, False)

    # Centrar la ventana principal
    centrar_ventana(root)

    # Cargar y mostrar una imagen (asegúrate de tener el archivo en la misma carpeta)
    imagen = tk.PhotoImage(file="logo.png")  # Ruta a la imagen (asegúrate de tener el archivo de imagen)
    label_imagen = tk.Label(root, image=imagen)
    label_imagen.image = imagen  # Necesario para evitar que la imagen sea recolectada por el garbage collector
    label_imagen.pack(pady=20)

    # Etiqueta de bienvenida
    label_bienvenida = tk.Label(root, text="¡Bienvenido a OpenLPConverter!", font=("Arial", 24), pady=20)
    label_bienvenida.pack()

    # Botón para iniciar el proceso
    boton_iniciar = tk.Button(root, text="Seleccionar Canciones", font=("Arial", 14), command=iniciar_proceso, pady=10, padx=20)
    boton_iniciar.pack(pady=50)

    root.iconbitmap('logo.ico')  # Cambia 'icono.ico' por la ruta a tu archivo .ico

    # Ejecutar ventana principal
    root.mainloop()

if __name__ == "__main__":
    main()
