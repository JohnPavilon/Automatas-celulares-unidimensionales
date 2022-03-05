import numpy as np
from matplotlib import pyplot as plt

powers_of_two = np.array([[4], [2], [1]])

"Muestra en pantalla el arreglo dado por la regla"
#def main():
    #print_image(rule_number, size, steps)
    

def print_image(rule_number, size, steps, cond, pos):
    data = cellular_automaton(rule_number, size, steps, init_cond= cond, impulse_pos=pos)
    plt.title('Autómata celular unidimensional \n Regla {}'.format(rule_number), fontweight ="bold")
    plt.imshow(data, cmap='bone_r')
    plt.axis('off')
    plt.show()

"Realiza las operaciones requeridas para generar la siguiente generación"
def step(x, rule_binary):
    
    x_shift_right = np.roll(x, 1)
    x_shift_left = np.roll(x, -1)
    y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)
    z = np.sum(powers_of_two * y, axis=0).astype(np.int8)

    #Da la siguiente generación
    return rule_binary[7 - z]

def cellular_automaton(rule_number, size, steps,
                       init_cond='random', impulse_pos='center'):
    #Verifica que la regla dada sea un número entre 0 y 255
    assert 0 <= rule_number <= 255
    #Sirve para inicializar las células de manera única o aleatoria
    assert init_cond in ['random', 'impulse']
    #Localiza las células iniciales
    assert impulse_pos in ['left', 'center', 'right']
    
    #Obtiene la cadena de la regla en binario
    rule_binary_str = np.binary_repr(rule_number, width=8)
    rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.int8)
    #Inicializa un arreglo dada las dimensiones
    x = np.zeros((steps, size), dtype=np.int8)
    
    if init_cond == 'random':  # Asigna de manera aleatoria las células iniciales
        x[0, :] = np.array(np.random.rand(size) < 0.5, dtype=np.int8)

    if init_cond == 'impulse':  # Asigna la célula inicial en la posición 0
        if impulse_pos == 'left':
            x[0, 0] = 1
        elif impulse_pos == 'right':
            x[0, size - 1] = 1
        else:
            x[0, size // 2] = 1
    
        #Aplica la regla dada en cada iteración para cada célula en el arreglo
    for i in range(steps - 1):
        x[i + 1, :] = step(x[i, :], rule_binary)
    
    return x

#Inicia main
#main()
#print_image(90, 300, 300, 'impulse', 'left')