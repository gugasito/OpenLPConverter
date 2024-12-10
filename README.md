# OpenLPConverter
OpenLPConverter es una herramienta diseñada para facilitar la conversión de canciones escritas en formato XML, utilizado por el software OpenLP, a un formato de texto plano (TXT). Este proyecto tiene como objetivo permitir que los usuarios conviertan archivos de canciones desde una estructura XML estructurada y compleja, a un formato simple y accesible que puede ser usado en otros sistemas, aplicaciones o presentaciones. A través de una interfaz gráfica intuitiva, el proceso de conversión se simplifica, permitiendo que tanto usuarios novatos como experimentados utilicen la herramienta sin dificultad.

Características Clave:
Conversión de Archivos XML a TXT: OpenLPConverter toma archivos XML estructurados, extrae la letra de las canciones y la convierte a un archivo de texto. Esto es especialmente útil para aquellos que trabajan con software de presentación de letras y necesitan los textos en un formato más sencillo.

Interfaz Gráfica de Usuario (GUI): A través de una interfaz visual construida con Tkinter, el usuario puede seleccionar fácilmente los archivos XML que desea convertir, y elegir la carpeta de destino para los archivos generados. No es necesario tener conocimientos técnicos de programación para utilizar la herramienta.

Barra de Progreso: Durante el proceso de conversión, el usuario puede ver el avance en tiempo real a través de una barra de progreso. Esta barra indica el porcentaje de archivos procesados, lo que permite al usuario seguir el estado de la conversión sin tener que esperar en silencio.

Personalización del Título de las Canciones: Al generar los archivos TXT, el título de la canción se extrae directamente de la etiqueta <title> del archivo XML y se agrega al principio del archivo de texto generado, seguido de la letra de la canción. Esto ayuda a mantener la estructura y el formato de presentación de cada canción.

Soporte para Versos con Sufijos: OpenLPConverter es capaz de manejar versos con sufijos (como v1a, v1b, etc.), agrupándolos correctamente bajo el nombre del verso principal (v1), asegurando que el formato final sea coherente y organizado.

Cómo Funciona:
Selección de Archivos XML: El usuario abre la aplicación y selecciona uno o más archivos XML que contienen las letras de las canciones. Estos archivos están estructurados con las etiquetas necesarias (<title>, <verse>, <verseOrder>) que contienen la información que OpenLPConverter necesita para realizar la conversión.

Conversión al Formato TXT: Una vez que los archivos XML han sido seleccionados, OpenLPConverter procesa cada uno, extrayendo la letra de las canciones y generando un archivo TXT para cada canción. El título extraído de la etiqueta <title> se coloca al principio del archivo, seguido de los versos en el orden indicado por la etiqueta <verseOrder>. Si la etiqueta <verseOrder> no está presente, el programa sigue el orden en que los versos aparecen en el archivo XML.

Visualización del Progreso: Durante la conversión, el usuario puede ver una ventana de progreso que indica el porcentaje de avance, lo que proporciona una experiencia más fluida y menos incierta durante la ejecución de la tarea.

Generación del Archivo de Salida: Finalmente, los archivos TXT generados son guardados en la carpeta de destino seleccionada por el usuario, con un nombre correspondiente al título de la canción y la extensión .txt. Esto facilita la organización de las canciones y su uso posterior.

¿Por Qué Este Proyecto?:
Este proyecto surge de la necesidad de transformar los archivos XML utilizados en OpenLP a un formato más accesible y fácil de manejar. Los archivos XML de OpenLP, aunque son adecuados para la estructura interna del software, pueden resultar difíciles de usar fuera de este entorno. Con OpenLPConverter, los usuarios pueden convertir fácilmente sus archivos de canciones a un formato estándar de texto, compatible con otras aplicaciones, sistemas y herramientas de presentación.

Además, la interfaz gráfica proporciona una forma sencilla y directa de interactuar con el programa, sin necesidad de realizar configuraciones o programaciones complejas. La inclusión de una barra de progreso hace que el proceso sea más transparente y fácil de seguir.

Este proyecto es ideal para usuarios que trabajan con presentaciones de canciones, software de karaoke o sistemas similares, donde el uso de archivos de texto es más común que el uso de XML.

Posibles Usos:
Transición entre sistemas: Si estás migrando de OpenLP a otro sistema que requiere archivos de texto en lugar de XML, esta herramienta te ayudará a hacer la conversión de manera sencilla.
Presentaciones en vivo: Si necesitas presentar letras de canciones en formato texto, puedes convertir fácilmente las letras de OpenLP a un archivo de texto plano.
Integración con otros programas: Esta herramienta es útil para usuarios que desean integrar las canciones de OpenLP en programas que no soportan XML, pero sí archivos de texto.
Tecnologías Utilizadas:
Python 3: El lenguaje principal utilizado para desarrollar el proyecto.
Tkinter: Librería para crear la interfaz gráfica de usuario (GUI).
ttk (Themed Tkinter Widgets): Utilizado para la barra de progreso.
os: Para manejar archivos y directorios.
Este proyecto no solo es una herramienta útil para la conversión de archivos, sino que también sirve como una base para futuras mejoras y funcionalidades adicionales. ¡Contribuciones y mejoras son siempre bienvenidas!
