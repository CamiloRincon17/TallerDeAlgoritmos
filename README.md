# Taller de Algoritmos

## Ejercicio 1: Dirección del giro de un robot

Un robot se desplaza dentro de una bodega y utiliza tres puntos para determinar hacia dónde debe girar:

- **A:** posición anterior.
- **B:** posición actual.
- **C:** posición de destino.

Para clasificar el giro se calcula el siguiente determinante:

$$
\det = (B_x-A_x)(C_y-A_y)-(B_y-A_y)(C_x-A_x)
$$

### Interpretación del resultado

| Determinante | Clasificación |
|---|---|
| Mayor que $0$ | Giro antihorario |
| Menor que $0$ | Giro horario |
| Igual a $0$ | Los puntos son colineales |

## Casos a evaluar

| Caso | A | B | C |
|---|---|---|---|
| Caso 1 | $(1,2)$ | $(5,3)$ | $(3,7)$ |
| Caso 2 | $(2,1)$ | $(6,5)$ | $(8,2)$ |
| Caso 3 | $(1,1)$ | $(3,3)$ | $(6,6)$ |
| Caso 4 | $(0,4)$ | $(5,4)$ | $(3,1)$ |

## Código en Python

```python
casos = [
    ("Caso 1", (1, 2), (5, 3), (3, 7)),
    ("Caso 2", (2, 1), (6, 5), (8, 2)),
    ("Caso 3", (1, 1), (3, 3), (6, 6)),
    ("Caso 4", (0, 4), (5, 4), (3, 1))
]

for nombre, A, B, C in casos:
    determinante = (
        (B[0] - A[0]) * (C[1] - A[1])
        - (B[1] - A[1]) * (C[0] - A[0])
    )

    if determinante > 0:
        giro = "Antihorario"
    elif determinante < 0:
        giro = "Horario"
    else:
        giro = "Colineal"

    print(f"{nombre}: determinante = {determinante} — {giro}")
```

## Resultados

| Caso | Determinante | Clasificación |
|---|---:|---|
| Caso 1 | $18$ | Antihorario |
| Caso 2 | $-20$ | Horario |
| Caso 3 | $0$ | Colineal |
| Caso 4 | $-15$ | Horario |

### Ejemplo de cálculo: Caso 1

Para $A=(1,2)$, $B=(5,3)$ y $C=(3,7)$:

$$
\begin{aligned}
\det
&=(5-1)(7-2)-(3-2)(3-1)\\
&=(4)(5)-(1)(2)\\
&=20-2\\
&=18
\end{aligned}
$$

Como $18>0$, el giro es **antihorario**.

## Complejidad del algoritmo

Sea $n$ la cantidad de casos a evaluar. Cada caso realiza un número constante de operaciones:

$$
T(n)=c_1n+c_2
$$

Por lo tanto:

- **Complejidad de tiempo:** $O(n)$.
- **Complejidad de tiempo con los 4 casos dados:** $O(1)$, porque $n=4$ es una constante.
- **Complejidad de espacio:** $O(n)$ si se almacenan todos los casos y resultados.

---

# Ejercicio 2: Intersección de segmentos

Una empresa de logística necesita saber si las rutas de dos vehículos autónomos se cruzan. Para ello, se comparan dos segmentos: $AB$ y $CD$.

## Fórmula de orientación

Para tres puntos $P$, $Q$ y $R$, la orientación es:

$$
\operatorname{orient}(P,Q,R)
=(Q_x-P_x)(R_y-P_y)-(Q_y-P_y)(R_x-P_x)
$$

| Resultado | Significado |
|---:|---|
| $>0$ | Giro antihorario |
| $<0$ | Giro horario |
| $=0$ | Los puntos son colineales |

Los segmentos tienen intersección si:

1. Las orientaciones de $ABC$ y $ABD$ tienen signos opuestos.
2. Las orientaciones de $CDA$ y $CDB$ tienen signos opuestos.

Cuando una orientación es cero, se debe comprobar si el punto está dentro del segmento correspondiente. Esta condición detecta colinealidad, contactos y superposiciones.

## Plano cartesiano

```text
 y
 7  |                          C?     D?
 6  |                       C●
 5  |       B●                      ········· Colineales
 4  |      /                              Caso 2
 3  |     /                            ·
 2  |    /   Horizontal de Caso 3 ───────
 1  |  A●                         D●
    +-------------------------------------- x
      1  2  3  4  5  6  7  8
```

> **Nota:** los segmentos principales tienen la forma $AB$ y $CD$. La representación anterior es esquemática. El código permite una visualización exacta en un plano.

## Casos

### Caso principal

| Segmento | Punto inicial | Punto final |
|---|---|---|
| $AB$ | $A(1,1)$ | $B(7,5)$ |
| $CD$ | $C(2,6)$ | $D(8,1)$ |

Las cuatro orientaciones son:

$$
\begin{aligned}
\operatorname{orient}(A,B,C)&=(7-1)(6-1)-(5-1)(2-1)=26\\
\operatorname{orient}(A,B,D)&=(7-1)(1-1)-(5-1)(8-1)=-28\\
\operatorname{orient}(C,D,A)&=(8-2)(1-6)-(1-6)(1-2)=-35\\
\operatorname{orient}(C,D,B)&=(8-2)(5-6)-(1-6)(7-2)=19
\end{aligned}
$$

Las primeras dos orientaciones tienen signos opuestos y las otras dos también. Por esta razón, los segmentos **sí se cruzan**.

### Caso 2

Segmentos colineales:

- $A(1,1)$, $B(3,3)$.
- $C(5,5)$, $D(7,7)$.

$$
\begin{aligned}
\operatorname{orient}(A,B,C)&=0\\
\operatorname{orient}(A,B,D)&=0\\
\operatorname{orient}(C,D,A)&=0\\
\operatorname{orient}(C,D,B)&=0
\end{aligned}
$$

Como todos los puntos están sobre la misma línea $y=x$, podría existir superposición. Sin embargo:

- $AB$ ocupa aproximadamente $x\in[1,3]$.
- $CD$ ocupa aproximadamente $x\in[5,7]$.

Los intervalos no se tocan, por lo que **no existe intersección**.

### Caso 3

Los datos proporcionados son:

$$
A(0,2),\quad B(6,2)
$$

Solo se conoce un segmento. Para determinar si existe intersección debe proporcionarse el segundo segmento $CD$, por ejemplo $C(?,?)$ y $D(?,?)$.

## Implementación en Python

```python
# Devuelve el resultado de la orientación: 1, -1 o 0
def orientacion(P, Q, R):
    valor = (
        (Q[0] - P[0]) * (R[1] - P[1])
        - (Q[1] - P[1]) * (R[0] - P[0])
    )

    if valor > 0:
        return 1
    if valor < 0:
        return -1
    return 0


# Comprueba si el punto está dentro de un segmento colineal
def sobre_segmento(P, Q, R):
    return (
        min(P[0], R[0]) <= Q[0] <= max(P[0], R[0])
        and min(P[1], R[1]) <= Q[1] <= max(P[1], R[1])
    )


# Devuelve True si los segmentos se cruzan, se tocan o se superponen
def intersección(A, B, C, D):
    o1 = orientacion(A, B, C)
    o2 = orientacion(A, B, D)
    o3 = orientacion(C, D, A)
    o4 = orientacion(C, D, B)

    # Cruce propiamente dicho
    if o1 != o2 and o3 != o4:
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True

    # Contacto o punto colineal
    if o1 == 0 and sobre_segmento(A, C, B):
        return True
    if o2 == 0 and sobre_segmento(A, D, B):
        return True
    if o3 == 0 and sobre_segmento(C, A, D):
        return True
    if o4 == 0 and sobre_segmento(C, B, D):
        return True

    return False


casos = [
    ("Caso principal", (1, 1), (7, 5), (2, 6), (8, 1)),
    ("Caso 2", (1, 1), (3, 3), (5, 5), (7, 7))
]

for nombre, A, B, C, D in casos:
    resultado = intersección(A, B, C, D)
    print(f"{nombre}: {resultado}")
```

Salida esperada:

```text
Caso principal: True
Caso 2: False
```

## Visualización con Matplotlib

```python
import matplotlib.pyplot as plt

segmentos = [
    ((1, 1), (7, 5), "AB", "royalblue"),
    ((2, 6), (8, 1), "CD", "orange"),
]

plt.figure(figsize=(8, 6))

for inicio, fin, nombre, color in segmentos:
    x = [inicio[0], fin[0]]
    y = [inicio[1], fin[1]]

    plt.plot(x, y, marker="o", linewidth=3,
             markersize=9, color=color, label=nombre)

    plt.text(inicio[0] - 0.3, inicio[1] - 0.4,
             nombre[0], fontsize=12, fontweight="bold")
    plt.text(fin[0] + 0.1, fin[1] - 0.4,
             nombre[1], fontsize=12, fontweight="bold")

plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.5)
plt.axis("equal")
plt.xlim(0, 9)
plt.ylim(0, 7)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Intersección de segmentos")
plt.legend()
plt.show()
```

## Complejidad $O(1)$

La detección de intersección realiza:

- Cuatro cálculos de orientación.
- A lo sumo cuatro comprobaciones de pertenencia al segmento.
- Comparaciones constantes.

El número de operaciones no depende de la cantidad de segmentos ni de la longitud de los segmentos:

$$
T(n)=c
$$

Por lo tanto, en función de una sola comparación entre dos segmentos:

$$
T(n)=O(1)
$$

El uso de memoria también es constante:

$$
S(n)=O(1)
$$

Si hubiera que comprobar una lista de $n$ segmentos contra otros $m$, la complejidad sería $O(nm)$, aunque la comparación individual siga siendo $O(1).

---

# Ejercicio 3: Comprobaciones entre tuberías

Para determinar cuántos pares de tuberías se pueden interceptar se revisan dos tuberías a la vez. La comparación $i$ con $j$ debe realizarse una sola vez.

## 1. ¿Por qué el segundo ciclo debe usar $j=i+1$?

Cada tubería se compara con las tuberías que vienen después de ella.

```python
for i in range(n):
    for j in range(i + 1, n):
        print("Comprobación:", i, j)
```

Por ejemplo, si $i=1$, comenzar desde $j=2$ evita comparar:

- El par consigo mismo: $(1,1)$.
- Un par que ya fue comprobado: $(1,0)$, si $j<i$.
- La tubería $1$ con la tubería $0$, que corresponde a $(0,1)$ y ya fue procesado.

Si se usa $j=0$, se repetían pares y cada tubo podría compararse consigo mismo.

## 2. Tabla de iteraciones

### Para $N=5$

| $i$ | Valores de $j$ | Comprobaciones |
|---:|---|---:|
| 0 | 1, 2, 3, 4 | 4 |
| 1 | 2, 3, 4 | 3 |
| 2 | 3, 4 | 2 |
| 3 | 4 | 1 |
| 4 | Ninguno | 0 |
|  | **Total** | **10** |

### Para $N=8$

| $i$ | Valores de $j$ | Comprobaciones |
|---:|---|---:|
| 0 | 1, 2, 3, 4, 5, 6, 7 | 7 |
| 1 | 2, 3, 4, 5, 6, 7 | 6 |
| 2 | 3, 4, 5, 6, 7 | 5 |
| 3 | 4, 5, 6, 7 | 4 |
| 4 | 5, 6, 7 | 3 |
| 5 | 6, 7 | 2 |
| 6 | 7 | 1 |
| 7 | Ninguno | 0 |
|  | **Total** | **28** |

## 3. Expresión exacta de las llamadas

La función `interceptan` se llama una vez por cada par distinto de tuberías:

$$
T(n)=\sum_{i=0}^{n-1}\sum_{j=i+1}^{n-1}1
$$

Esta sumatoria representa todas las combinaciones posibles de dos tuberías tomadas de un conjunto de $n$ elementos:

$$
T(n)=\binom{n}{2}=\frac{n(n-1)}{2}
$$

También puede escribirse como:

$$
T(n)=1+2+3+\cdots+(n-1)
$$

## 4. Desarrollo y complejidad

La cantidad de comprobaciones es:

$$
\begin{aligned}
T(n)
&=\sum_{i=0}^{n-1}(n-i-1)\\
&=(n-1)+(n-2)+\cdots+1\\
&=\frac{(n-1)n}{2}\\
&=\frac{n^2-n}{2}
\end{aligned}
$$

Al simplificar el término dominante:

$$
T(n)=\frac{1}{2}n^2-\frac{1}{2}n
$$

Por lo tanto:

- **Complejidad temporal:** $O(n^2)$.
- **Complejidad temporal aproximada:** $\Theta(n^2)$.
- **Complejidad de espacio:** $O(1)$ si solo se realizan contadores y comparaciones.

## 5. Comprobaciones para grandes cantidades

Usando:

$$
T(n)=\frac{n(n-1)}{2}
$$

| Tuberías $n$ | Operaciones exactas |
|---:|---:|
| 100 | $100\cdot99/2=4.950$ |
| 1.000 | $1.000\cdot999/2=499.500$ |
| 10.000 | $10.000\cdot9.999/2=49.995.000$ |

Para $100$ tuberías se realizan $4.950$ llamadas. Para $1.000$, $499.500$. Para $10.000$, $49.995.000$.

```python
import itertools


def numero_comprobaciones(n):
    """Calcula llamadas a interseccion para cada par distinto."""
    return n * (n - 1) // 2


for tuberias in (5, 8, 100, 1000, 10000):
    print(tuberias, numero_comprobaciones(tuberias))
```

---

# Ejercicio 4: Triangulación de un terreno irregular

## Datos del terreno

Los vértices se encuentran conectados en el siguiente orden:

$$
A(0,0),\ B(8,0),\ C(8,6),\ D(4,3),\ E(0,6)
$$

La lista del polígono es:

```text
A → B → C → D → E → A
```

## 1. Vértices convexos y cóncavos

Se utiliza el determinante entre cada vértice y sus dos vecinos:

$$
\operatorname{orient}(P,Q,R)
=(Q_x-P_x)(R_y-P_y)-(Q_y-P_y)(R_x-P_x)
$$

### Tabla de orientaciones

| Vértice | Vecinos | Determinante | Clasificación |
|---|---|---:|---|
| $A$ | $E,A,B$ | $48$ | Convexo |
| $B$ | $A,B,C$ | $48$ | Convexo |
| $C$ | $B,C,D$ | $24$ | Convexo |
| $D$ | $C,D,E$ | $-24$ | Cóncavo |
| $E$ | $D,E,A$ | $24$ | Convexo |

> Si todos los giros mantienen el mismo sentido positivo, el vértice es convexo. Un giro negativo indica un vértice cóncavo.

## Ejemplos de cálculo

En $D$:

$$
\begin{aligned}
\operatorname{orient}(C,D,E)
&=(4-8)(6-3)-(3-6)(0-4)\\
&=(-4)(3)-(-3)(-4)\\
&=-12-12\\
&=-24
\end{aligned}
$$

Como el determinante es negativo, $D$ es una **concavidad**.

En $C$:

$$
\begin{aligned}
\operatorname{orient}(B,C,D)
&=(8-8)(3-6)-(6-0)(4-8)\\
&=0-6(-4)\\
&=24
\end{aligned}
$$

Como el determinante es positivo, $C$ es convexo.

## 2. Triángulos y diagonales internas

Para un polígono simple de $n$ vértices:

$$
T=n-2
$$

$$
D=n-3
$$

Como $n=5$:

- **Número de triángulos:** $5-2=3$.
- **Número de diagonales internas:** $5-3=2$.

Una triangulación válida es:

```text
A---B
|  /| \
| / |  \
|/  D   C
E    \ /
  \___/
```

Una representación más útil sería dividirlo con las diagonales $AD$ y $BD$, obteniendo:

- Triángulo $ABD$.
- Triángulo $BCD$.
- Triángulo $ADE$.

Las diagonales internas son:

```text
AD
BD
```

## 3. Triangulación válida

```text
 y
 6 | E●──────────●C
   | |          /|
   | |         / |
   | |        D  |
   | |       ●   |
   | |      /|   |
   | |     / |   |
   | |    /  |   |
 0 | A●──●───●───●B
   +--------------- x
     0          8
```

Esta representación muestra una separación conceptual. Los triángulos pueden describirse por vértices:

```text
ABD, BCD y ADE
```

Las diagonales que separan dichos triángulos son:

```text
AD y BD
```

## 4. Primera oreja para Ear Clipping

El vértice $C$ es convexo y su triángulo de oreja es:

$$
\triangle BCD
$$

El vértice $C$ puede recortarse porque:

- $B$, $C$ y $D$ forman una orientación positiva.
- Ningún otro vértice se encuentra dentro del triángulo $BCD$.
- Al eliminar $C$, el polígono continúa siendo simple.

Una vez retirado $C$, queda el polígono:

```text
A → B → D → E → A
```

Los triángulos restantes pueden obtenerse mediante otros recortes o usando la diagonal $BD$.

## 5. Condiciones antes de retirar un vértice

Antes de eliminar un vértice $P$ se deben verificar:

1. **Convexidad:** el vértice debe formar una orientación convexa.
2. **Oreja vacía:** ningún otro vértice debe estar estrictamente dentro del triángulo formado por sus vecinos.
3. **No intersección:** la diagonal entre sus vecinos no debe cruzar el polígono.
4. **Polígono simple:** retirar el triángulo no puede dividir ni generar puntos de autointersección.
5. **Al menos tres vértices:** el proceso termina al llegar a un triángulo.

El vértice cóncavo $D$ no puede seleccionarse inicialmente como oreja.

## 6. Implementación en Python

```python
# Recibe el número de vértices y calcula triángulos y diagonales
def triangulacion(n):
    if n < 3:
        return {
            "triangulos": 0,
            "diagonales_internas": 0
        }

    return {
        "triangulos": n - 2,
        "diagonales_internas": n - 3
    }


# Orientación de tres puntos
def orientacion(P, Q, R):
    valor = (
        (Q[0] - P[0]) * (R[1] - P[1])
        - (Q[1] - P[1]) * (R[0] - P[0])
    )

    if valor > 0:
        return "convexo"
    if valor < 0:
        return "concavo"
    return "colineal"


vertices = [
    ("A", (0, 0)),
    ("B", (8, 0)),
    ("C", (8, 6)),
    ("D", (4, 3)),
    ("E", (0, 6))
]

n = len(vertices)

for i in range(n):
    anterior = vertices[(i - 1) % n][1]
    actual = vertices[i][1]
    siguiente = vertices[(i + 1) % n][1]

    nombre = vertices[i][0]
    tipo = orientacion(anterior, actual, siguiente)

    print(f"Vértice {nombre}: {tipo}")

resultado = triangulacion(n)
print("Triángulos:", resultado["triangulos"])
print("Diagonales internas:", resultado["diagonales_internas"])
```

Salida esperada:

```text
Vértice A: convexo
Vértice B: convexo
Vértice C: convexo
Vértice D: concavo
Vértice E: convexo
Triángulos: 3
Diagonales internas: 2
```