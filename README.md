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