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