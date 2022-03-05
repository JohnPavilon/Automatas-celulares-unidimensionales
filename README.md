# Autómata celular unidimensional

# 1. Introducción

Hay un juego de computadora fascinante, llamado Juego de la Vida, el cual fue
diseñado en 1970 por el matemático británico John Horton Conway 8, de la
Universidad de Cambridge, Inglaterra (en ese tiempo). Se hizo muy popular desde
que Martin Gardner, en su columna de octubre de ese año en la revista Scientific
American hablara de las ideas de dicho matemático. Pero más allá de ser un
interesante pasatiempo, podríamos decir que el juego de la vida contiene las ideas
que originalmente von Neumann intentó plasmar en su autómata celular. Lo
importante aquí es que Conway halló una serie de reglas simples, para su
autómata celular en dos dimensiones, que permitió superar las dificultades que
von Neumann tuvo en su momento para crear máquinas que se auto-replicaran.

El juego de la vida ocurre en un tablero cuadriculado, en donde cada casilla o
escaque puede haber una célula o estar vacío. La idea es acomodar una serie de 
células en la malla cuadriculada y observando las vecindades de cada célula, cada
cuadro pues, utilizando las reglas de Conway (ver más abajo), ir calculando las
nuevas configuraciones de células que aparecerán en la siguiente generación.

Tomemos un plano cuadriculado de dimensiones infinitas. Cada sitio, cuadro o
casilla, tiene 8 casillas vecinas: cuatro ortogonalmente adyacentes, en diagonal, 2 
en vertical y 2 en horizontal. En cada sitio es posible poner un valor binario (hay
célula o no hay en esa casilla). Las reglas son:

1. Supervivencia: cada célula o ficha, que tenga dos o tres fichas vecinas
sobrevive y pasa a la generación siguiente.

2. Fallecimiento: cada ficha que tenga cuatro o más vecinas muere y es
retirada del tablero, por sobrepoblación. Las fichas con una vecina o solas
fallecen por aislamiento

3. Nacimientos: cada casilla vacía, adyacente a exactamente tres cifras
vecinas -tres, ni más ni menos- es casilla generatriz. Es decir, en la
siguiente generación habrá de colocarse una ficha en esa casilla

Es importante hacer notar que todos los natalicios y fallecimientos ocurren
simultáneamente, y constituyen en su conjunto una generación en particular, al
paso del tiempo t, también llamado tic del reloj.

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
