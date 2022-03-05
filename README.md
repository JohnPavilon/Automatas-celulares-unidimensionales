# Autómatas celulares unidimensionales de Stephen Wolfram

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

Por ejemplo, consideremos una línea que contenga dos células en el medio de la
misma, es decir:

<div align="center">
    000...001100...000
</div>

La evolución de la siguiente generación pide revisar cada célula en la línea.
Cuando tenemos 000…000… no hay cambio alguno, pero llega un momento en
que tenemos 001 (recuérdese, sólo hay dos células en la línea del autómata).
Hallamos que tenemos que calcular el resultado cuando encontramos 001. Eso,
de acuerdo a la tabla da como resultado un 1. Se pone en la siguiente línea,
debajo de la célula que estamos analizando. Ahora movemos nuestro apuntador a
la siguiente célula y hallamos la configuración 011, la cual da como resultado un 1.
Pasamos a la siguiente célula y encontramos la configuración 110, lo cual vuelve a
darnos un 1. Seguimos con este procedimiento y hallamos los valores 100, lo cual
de nuevo, da un 1. Inmediatamente después todos los valores dan 0. El autómata
quedará entonces así en la segunda generación (la primera generación es la
inicial):

<div align="center">
    000...001100...000 [Generación inicial]
</div>

<div align="center">
    000...011110...000 [Segunda generación]
</div>

Este proceso se puede ejecutar un número n determinado de veces, lo cual conlleva
a la aparición de patrones complejos.

# 2. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Automatas-celulares-unidimensionales/ adjunto a su contenido. Además de lo anterior, deberá tener instalado las bibliotecas Numpy, Matplotlib y PyQt5, en caso de no tenerlos instalados consulte los siguientes enlaces: 

<div align="center">
    https://sites.google.com/site/clasesdesde0/python-plot (Instalación de Matplotlib y Numpy)
</div>
<div align="center">
    https://pythones.net/pyqt-instalacion-y-codigo-tutorial/ (Instalación de PyQt5)
</div>

Posteriormente, se ejecutará el archivo Autómata_Wolfram.py localizado en Automatas-celulares-unidimensionales/, este archivo se puede ejecutar dentro de una terminal (esto se puede realizar utilizando el comando "python3 Autómata_Wolfram.py", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "Autómata_Wolfram.py" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Con lo anterior realizado, usted verá que se iniciará el programa abriendo una ventana, mostrando en pantalla una interfaz en donde se mostrará una cuadrícula azul con la cual el usuario podrá interactuar.

# Menú de inicio
<p align="center">
  Cuando se ejecute el archivo Autómata_Wolfram.py, usted verá esta ventana.
</p>

<div align="center">
    <img src="https://i.postimg.cc/Cx1ytDQ1/imagen-2022-03-04-231024.png"</img> 
</div>

<p align="center">
  Para seleccionar la regla a ejecutar, use el siguiente recuadro. Igualmente puede modificar el número contenido directamente seleccionandolo y escribiendo el número deseado.
</p>

<div align="center">
    <img src="https://i.postimg.cc/KjRLw0Bf/imagen-2022-03-04-231345.png"</img> 
</div>

<p align="center">
  Para seleccionar el número de casillas iniciales y el número de generaciones a realizar, seleccione los siguientes recuadros. Viene con los valores predeterminados 600 y 800, estos valores se pueden modificar directamente.
</p>

<p align="center">
  <img src="https://i.postimg.cc/jdqShMyn/imagen-2022-03-04-232013.png"</img>
</p>

<p align="center">
  La primera generación consiste en una célula viva dado una posición de inicio, si se desea modificar la posición de inicio, utilize la barra deslizadora. Viene con el valor centro por defecto, deslize la barra con el cursor al valor deseado.
</p>

<p align="center">
  <img src="https://i.postimg.cc/fbD23SGs/imagen-2022-03-04-232247.png"</img>
</p>

<p align="center">
  Existe la opción de que la generación inicial se genere de manera aleatoria, este valor viene desmarcada por defecto.
</p>

<p align="center">
  <img src="https://i.postimg.cc/SsrJy3Wq/imagen-2022-03-04-232747.png"</img>
</p>

# 3. Patrones interesantes 

<p align="center">
  <img src="https://i.postimg.cc/fRcZnX7Q/imagen-2022-03-04-233010.png"</img>
</p>

# 4. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Automatas-celulares-unidimensionales junto a una somera descripción de los mismos:

Automatas-celulares-unidimensionales/

1. README.md: Es el archivo que está leyendo en este momento
2. Autómata_Wolfram.py: Ejecuta el programa descrito anteriormente
3. Cellular.py: Es el encargado de calcular el aútomata celular con los parámentros dados
4. GUI.py: Es la inteefaz de usuario primeramente vista por el usuario
5. View.py: Despliega en pantalla el resultado dado.
6. logo.ico: Una imagen que puede ser visualizada en la esquina superior izquierda de la ventana del programa.

<p align="center">
  <img src="https://i.postimg.cc/90b8YmZS/imagen-2022-03-04-233527.png"</img>
</p>
