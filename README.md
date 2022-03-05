# Autómata celular unidimensional

# 1. Introducción

Los autómatas celulares de von Neumann y de Conway sin duda hicieron
despertar la imaginación de otros investigadores. Una idea sensata es quitar una
dimensión a los autómatas bidimensionales, como los del juego de la vida, y ver
qué pasa si ponemos a trabajar a los autómatas en una sola dimensión. Esto, en
principio, podrías sugerir una simplicidad mayor que al trabajar con autómatas
como en el juego de la vida, que ocurren en dos dimensiones. Sin embargo, esta
simplificación es aparente, pues en una dimensión, los autómatas hallan
desarrollos emergentes complejos.

Consideremos una línea recta de células, de casillas, las cuales pueden estar
ocupadas o vacías. Pueden pues tener células o no tenerlas. Aquí, las reglas del
autómata, también ciegas, se basan simplemente en la vecindad de cada célula
con la que se está trabajando en cada generación. De acuerdo a las reglas que se
definen, podremos ver lo que pasa en la línea de células, generación tras
generación. Además, para darnos una mejor idea, podemos colocar la primera
generación (la configuración inicial), y ver el comportamiento, pintando la segunda
generación debajo de la primera. Podemos hacer esto para cada ciclo t en el
tiempo y en un momento determinado tendremos decenas, centenas o miles de
generaciones desplegadas. Con ello podremos hacer un análisis de lo que está
pasando.

Formalmente podríamos decir que los autómatas, las células, tienen valor 1 si
están en alguna casilla de la línea de cuadros disponibles o bien contienen un
valor 0 (cero), es decir, no hay nada en una casilla. Las reglas de evolución se
presentan solamente analizando la vecindad de cada casilla de interés, una por
una.

Uno de los primeros científicos en estudiar cuidadosamente este tipo de
autómatas fue Stephen Wolfram. Wolfram habla de reglas locales de evolución, que no son otra cosa que las reglas
ciegas que descubrió Conway en el juego de la vida o las reglas en la hormiga de
Langton, como veremos más adelante. Estas reglas son las que definen el
comportamiento en la evolución del autómata. Por ejemplo, consideremos una
línea de células y las siguientes reglas locales:

<div align="center">
    <img src="https://i.postimg.cc/Pqt3Lk1R/imagen-2022-03-04-225453.png"</img> 
</div>


# 2. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Juego-de-la-Vida/ adjunto a su contenido. Además de lo anterior, deberá tener instalado la biblioteca PyGame, en caso de no tenerlo instalado consulte el siguiente enlace: https://www.pygame.org/wiki/GettingStarted

Posteriormente, se ejecutará el archivo game-of-life.py localizado en Juego-de-la-Vida/, este archivo se puede ejecutar dentro de una terminal (esto se puede realizar utilizando el comando "python3 game-of-life.py", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "game-of-life.py" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Con lo anterior realizado, usted verá que se iniciará el programa abriendo una ventana, mostrando en pantalla una interfaz en donde se mostrará una cuadrícula azul con la cual el usuario podrá interactuar.

# Controles
<p align="center">
  Presione click izquierdo del mouse para asignar el estado "vivo" a la celula
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155262708-6b663a10-2466-48db-ad6f-1c181b1704a7.gif" alt="animated" />
</p>

<p align="center">
  En caso de querer "matar" a la celula, presione click derecho
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155408321-839f8d28-6151-462c-8056-b46a3f6b5818.gif" alt="animated" />
</p>

<p align="center">
  Una vez establecido la configuración inicial, para proceder a la siguiente generación presione la tecla Enter
</p>


<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155263660-8eab2da0-f783-4f92-b1d6-d128ee6bdd6e.gif" alt="animated" />
</p>

<p align="center">
  Si se desea dejar corriendo "el juego de la vida", presione la tecla Space. Presione nuevamente la tecla si se desea pausar.
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155414472-ce985a3f-465c-4fc0-923d-d147094fcc68.gif" alt="animated" />
</p>

<p align="center">
  En caso de querer reiniciar el juego, presione la tecla Backspace (Esta se localiza encima de la tecla Enter)
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155264886-3f42fb4e-8b6f-4c92-84b2-9c9d4822f9e5.gif" alt="animated" />
</p>

# 3. Patrones "Pentóminos" interesantes 

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155421052-315738b9-4d84-4867-8641-22624860a260.gif" alt="animated" />
</p>

# 4. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Shamir-s-Secret-Sharing-Scheme junto a una somera descripción de los mismos:

Juego-de-la-Vida/

1. README.md: Es el archivo que está leyendo en este momento
2. game-of-life.py: Ejecuta una simulación del juego de la vida
