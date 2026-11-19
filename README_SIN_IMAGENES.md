# Taller de Algoritmos: Geometría Computacional (Versión Texto / Sin Imágenes)

> **Documento 100% autocontenido en Markdown puro:** Solución analítica, deducciones matemáticas paso a paso, representaciones cartesianas en diagramas de texto/ASCII, análisis de complejidad $T(n)$ y código en Python.

---

## Tabla de Contenidos
1. [Fundamentos Teóricos: Orientación en el Plano](#fundamentos-teóricos-orientación-en-el-plano)
2. [Ejercicio 1: Dirección del Giro del Robot Autónomo](#ejercicio-1-dirección-del-giro-del-robot-autónomo)
   - [1. Cálculo del determinante para cada caso](#1-cálculo-del-determinante-para-cada-caso)
   - [2. Clasificación y código en Python](#2-clasificación-y-código-en-python)
   - [3. Análisis de complejidad temporal $T(n)$](#3-análisis-de-complejidad-temporal-tn)
3. [Ejercicio 2: Intersección de Rutas de Autos Autónomos](#ejercicio-2-intersección-de-rutas-de-autos-autónomos)
   - [1. Representación en el plano cartesiano (Diagramas ASCII)](#1-representación-en-el-plano-cartesiano)
   - [2. Cálculo de las 4 orientaciones necesarias](#2-cálculo-de-las-4-orientaciones-necesarias)
   - [3. Determinación de intersección (Cruce, contacto y superposiciones)](#3-determinación-de-intersección)
   - [4. Implementación en Python: función `interseccion`](#4-implementación-en-python-función-interseccion)
   - [5. Demostración de complejidad $O(1)$](#5-demostración-de-complejidad-o1)
4. [Ejercicio 3: Comprobaciones entre $N$ Tuberías](#ejercicio-3-comprobaciones-entre-n-tuberías)
5. [Ejercicio 4: Triangulación de un Terreno (Ear Clipping)](#ejercicio-4-triangulación-de-un-terreno-ear-clipping)
6. [Ejercicio 5: Comparación de algoritmos de triangulación](Ejercicio-5:-Comparación-de-algoritmos-de-triangulación)

---

## Fundamentos Teóricos: Orientación en el Plano

La herramienta matemática central de la geometría computacional bidimensional es la **función de orientación** o **producto cruz 2D** entre vectores.

Dados tres puntos $P(x_P, y_P)$, $Q(x_Q, y_Q)$ y $R(x_R, y_R)$, el determinante de la matriz homogénea 2D corresponde al doble del área signada del triángulo $\triangle PQR$:

$$
\operatorname{orient}(P, Q, R) = \det \begin{pmatrix} x_P & y_P & 1 \\ x_Q & y_Q & 1 \\ x_R & y_R & 1 \end{pmatrix} = (x_Q - x_P)(y_R - y_P) - (y_Q - y_P)(x_R - x_P)
$$

### Criterio de Decisión

| Signo del Determinante | Orientación Geométrica | Decisión del Móvil |
| :---: | :---: | :--- |
| $\Delta > 0$ | **Antihorario (CCW)** | El punto $R$ queda a la **izquierda** de la trayectoria $\vec{PQ}$ (giro a la izquierda). |
| $\Delta < 0$ | **Horario (CW)** | El punto $R$ queda a la **derecha** de la trayectoria $\vec{PQ}$ (giro a la derecha). |
| $\Delta = 0$ | **Colineal** | Los tres puntos yacen sobre la **misma línea recta** (continúa recto o da reversa). |

---

## Ejercicio 1: Dirección del Giro del Robot Autónomo

Un robot autónomo se desplaza dentro de una bodega. Para determinar si debe girar a la izquierda, a la derecha o continuar recto, analiza tres posiciones consecutivas:
* $A$: Posición anterior
* $B$: Posición actual
* $C$: Posición de destino

---

### 1. Cálculo del determinante para cada caso

Fórmula aplicada:
$$\Delta = (x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A)$$

#### **Caso 1: $A(1,2)$, $B(5,3)$, $C(3,7)$**
* Vector $\vec{AB} = (5 - 1, 3 - 2) = (4, 1)$
* Vector $\vec{AC} = (3 - 1, 7 - 2) = (2, 5)$
* Desarrollo:
  $$\Delta_1 = (4)(5) - (1)(2) = 20 - 2 = \mathbf{+18}$$
* **Conclusión:** Como $\Delta_1 > 0$, el robot realiza un **Giro Antihorario (a la izquierda)**.

#### **Caso 2: $A(2,1)$, $B(6,5)$, $C(8,2)$**
* Vector $\vec{AB} = (6 - 2, 5 - 1) = (4, 4)$
* Vector $\vec{AC} = (8 - 2, 2 - 1) = (6, 1)$
* Desarrollo:
  $$\Delta_2 = (4)(1) - (4)(6) = 4 - 24 = \mathbf{-20}$$
* **Conclusión:** Como $\Delta_2 < 0$, el robot realiza un **Giro Horario (a la derecha)**.

#### **Caso 3: $A(1,1)$, $B(3,3)$, $C(6,6)$**
* Vector $\vec{AB} = (3 - 1, 3 - 1) = (2, 2)$
* Vector $\vec{AC} = (6 - 1, 6 - 1) = (5, 5)$
* Desarrollo:
  $$\Delta_3 = (2)(5) - (2)(5) = 10 - 10 = \mathbf{0}$$
* **Conclusión:** Como $\Delta_3 = 0$, los puntos son **Colineales (continúa en línea recta)**.

#### **Caso 4: $A(0,4)$, $B(5,4)$, $C(3,1)$**
* Vector $\vec{AB} = (5 - 0, 4 - 4) = (5, 0)$
* Vector $\vec{AC} = (3 - 0, 1 - 4) = (3, -3)$
* Desarrollo:
  $$\Delta_4 = (5)(-3) - (0)(3) = -15 - 0 = \mathbf{-15}$$
* **Conclusión:** Como $\Delta_4 < 0$, el robot realiza un **Giro Horario (a la derecha)**.

---

### Tabla Resumen del Ejercicio 1

| Caso | Punto Anterior $A$ | Punto Actual $B$ | Punto Destino $C$ | Determinante $\Delta$ | Clasificación del Giro |
|:---:|:---:|:---:|:---:|:---:|:---|
| **Caso 1** | $(1, 2)$ | $(5, 3)$ | $(3, 7)$ | **$+18$** | **Antihorario (Izquierda)** |
| **Caso 2** | $(2, 1)$ | $(6, 5)$ | $(8, 2)$ | **$-20$** | **Horario (Derecha)**       |
| **Caso 3** | $(1, 1)$ | $(3, 3)$ | $(6, 6)$ | **$0$**   | **Colineal (Sin giro)**     |
| **Caso 4** | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ | **$-15$** | **Horario (Derecha)**       |

---

### 2. Clasificación y código en Python

```python
def orientacion(A, B, C):
    """
    Calcula el determinante del producto cruz 2D entre los vectores AB y AC.
    Retorna > 0 si es antihorario, < 0 si es horario, == 0 si son colineales.
    """
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def clasificar_giro(det):
    """Clasifica el valor del determinante en tipo de giro."""
    if det > 0:
        return "Giro Antihorario (Izquierda)"
    elif det < 0:
        return "Giro Horario (Derecha)"
    else:
        return "Colineal (Sin giro / Línea recta)"

casos = {
    "Caso 1": ((1, 2), (5, 3), (3, 7)),
    "Caso 2": ((2, 1), (6, 5), (8, 2)),
    "Caso 3": ((1, 1), (3, 3), (6, 6)),
    "Caso 4": ((0, 4), (5, 4), (3, 1))
}

for nombre, (A, B, C) in casos.items():
    d = orientacion(A, B, C)
    print(f"{nombre}: det = {d:>3} -> {clasificar_giro(d)}")
```

---

### 3. Análisis de complejidad temporal $T(n)$

#### A. Para una sola terna (un giro)
1. **Resta de coordenadas:** $4$ operaciones ($(x_B - x_A)$, $(y_C - y_A)$, $(y_B - y_A)$, $(x_C - x_A)$).
2. **Multiplicaciones:** $2$ operaciones.
3. **Sustracción final:** $1$ operación.
4. **Condicionales de signo:** $2$ comparaciones a lo sumo.

Cada paso es una operación básica de costo constante $c_1$:
$$T_{\text{caso}} = c_1 = \mathbf{O(1)}$$

#### B. Para una ruta de $n$ puntos
Si el robot navega a través de una ruta completa de $n$ puntos $(P_1, P_2, \dots, P_n)$, se evalúan $(n - 2)$ ternas consecutivas:

$$T(n) = \sum_{i=1}^{n-2} c_1 = c_1 \cdot (n - 2) + c_2 = c_1 n - 2c_1 + c_2$$

$$\mathbf{T(n) = \Theta(n) \quad \text{o} \quad O(n)}$$

* **Complejidad Temporal:** **Lineal** respecto a la cantidad de waypoints de la ruta.
* **Complejidad Espacial:** $\mathbf{O(1)}$ (memoria auxiliar constante).

---

## Ejercicio 2: Intersección de Rutas de Autos Autónomos

---

### 1. Representación en el plano cartesiano

#### **Caso 1: Cruce transversal propio**
* Segmento $AB$: $A(1, 1)$ a $B(7, 5)$
* Segmento $CD$: $C(2, 6)$ a $D(8, 1)$

```text
  Y ^
  7 |
  6 |         C(2,6) \
  5 |                 \              B(7,5)
  4 |                  \      * P(4.89, 3.56)  [INTERSECCIÓN]
  3 |                   \    /
  2 |                    \  /
  1 |       A(1,1) -------\/-------------- D(8,1)
  0 +--------------------------------------------> X
    0   1   2   3   4   5   6   7   8   9
```

---

#### **Caso 2: Colineales disjuntos**
* Segmento $AB$: $A(1, 1)$ a $B(3, 3)$  (Rango en X: $[1, 3]$)
* Segmento $CD$: $C(5, 5)$ a $D(7, 7)$  (Rango en X: $[5, 7]$)

```text
  Y ^
  7 |                                  D(7,7)
  6 |                              /
  5 |                          C(5,5)
  4 |                          (Hueco: x entre 3 y 5)
  3 |                  B(3,3)
  2 |              /
  1 |          A(1,1)
  0 +--------------------------------------------> X
    0   1   2   3   4   5   6   7   8   9
    [--- AB ---]            [--- CD ---]   <-- Intervalos disjuntos (NO se tocan)
```

---

#### **Caso 3: Variantes para $A(0,2)$, $B(6,2)$**
El segmento $AB$ es horizontal a la altura $y = 2$ entre $x = 0$ y $x = 6$:

* **Variante 3a (Cruce vertical transversal):** $C(3,0)$ a $D(3,5)$
```text
  Y ^
  5 |             D(3,5)
  4 |               |
  3 |               |
  2 |   A(0,2) ---- * P(3,2) ---- B(6,2)   [Cruce en el punto interior (3,2)]
  1 |               |
  0 |             C(3,0)
    +------------------------------------> X
```

* **Variante 3b (Contacto en el extremo $B$):** $C(6,2)$ a $D(9,5)$
```text
  Y ^
  5 |                                     D(9,5)
  4 |                                   /
  3 |                                 /
  2 |   A(0,2) ============= B(6,2)=C(6,2)   [Contacto: el punto B coincide con C]
    +------------------------------------> X
```

* **Variante 3c (Superposición / Traslape colineal):** $C(4,2)$ a $D(9,2)$
```text
  Y ^
  2 |   A(0,2) ====== C(4,2) ===== B(6,2) ===== D(9,2)
        [----- AB -----]
              [------------ CD ------------]
              [ Solape: x in [4, 6] ]        [SÍ hay intersección (infinitos puntos)]
    +--------------------------------------------------> X
```

---

### 2. Cálculo de las 4 orientaciones necesarias

Para verificar si dos segmentos se cruzan, se calculan las cuatro orientaciones relativas:
* $\mathcal{O}_1 = \operatorname{orient}(A, B, C)$: signo de $C$ respecto a la recta $AB$.
* $\mathcal{O}_2 = \operatorname{orient}(A, B, D)$: signo de $D$ respecto a la recta $AB$.
* $\mathcal{O}_3 = \operatorname{orient}(C, D, A)$: signo de $A$ respecto a la recta $CD$.
* $\mathcal{O}_4 = \operatorname{orient}(C, D, B)$: signo de $B$ respecto a la recta $CD$.

---

#### **Cálculo Caso 1:** $A(1,1), B(7,5)$ y $C(2,6), D(8,1)$

1. **$\mathcal{O}_1 = \operatorname{orient}(A, B, C)$:**
   $$\vec{AB} = (6, 4), \quad \vec{AC} = (1, 5) \implies \mathcal{O}_1 = (6)(5) - (4)(1) = 30 - 4 = \mathbf{+26} \quad (> 0)$$
2. **$\mathcal{O}_2 = \operatorname{orient}(A, B, D)$:**
   $$\vec{AB} = (6, 4), \quad \vec{AD} = (7, 0) \implies \mathcal{O}_2 = (6)(0) - (4)(7) = 0 - 28 = \mathbf{-28} \quad (< 0)$$
3. **$\mathcal{O}_3 = \operatorname{orient}(C, D, A)$:**
   $$\vec{CD} = (6, -5), \quad \vec{CA} = (-1, -5) \implies \mathcal{O}_3 = (6)(-5) - (-5)(-1) = -30 - 5 = \mathbf{-35} \quad (< 0)$$
4. **$\mathcal{O}_4 = \operatorname{orient}(C, D, B)$:**
   $$\vec{CD} = (6, -5), \quad \vec{CB} = (5, -1) \implies \mathcal{O}_4 = (6)(-1) - (-5)(5) = -6 - (-25) = \mathbf{+19} \quad (> 0)$$

---

#### **Cálculo Caso 2:** $A(1,1), B(3,3)$ y $C(5,5), D(7,7)$
Todos los puntos pertenecen a la recta $y = x$:
1. $\mathcal{O}_1 = \operatorname{orient}(A, B, C) = (2)(4) - (2)(4) = \mathbf{0}$
2. $\mathcal{O}_2 = \operatorname{orient}(A, B, D) = (2)(6) - (2)(6) = \mathbf{0}$
3. $\mathcal{O}_3 = \operatorname{orient}(C, D, A) = (2)(-4) - (2)(-4) = \mathbf{0}$
4. $\mathcal{O}_4 = \operatorname{orient}(C, D, B) = (2)(-2) - (2)(-2) = \mathbf{0}$

---

#### **Cálculo Caso 3:** $A(0,2), B(6,2)$ frente a tres variantes

| Variante | $C$ | $D$ | $\mathcal{O}_1 (ABC)$ | $\mathcal{O}_2 (ABD)$ | $\mathcal{O}_3 (CDA)$ | $\mathcal{O}_4 (CDB)$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **3a: Cruce transversal** | $(3, 0)$ | $(3, 5)$ | **$-12$** | **$+18$** | **$+15$** | **$-15$** |
| **3b: Contacto en $B$** | $(6, 2)$ | $(9, 5)$ | **$0$** | **$+18$** | **$+18$** | **$0$** |
| **3c: Superposición** | $(4, 2)$ | $(9, 2)$ | **$0$** | **$0$** | **$0$** | **$0$** |

---

### 3. Determinación de intersección

1. **Cruce propio (Caso General):**
   Los segmentos se cruzan si y solo si los extremos de cada segmento quedan en lados opuestos respecto a la recta del otro:
   $$(\mathcal{O}_1 \cdot \mathcal{O}_2 < 0) \quad \text{y} \quad (\mathcal{O}_3 \cdot \mathcal{O}_4 < 0)$$
   * **Caso 1:** $\mathcal{O}_1 = +26$ y $\mathcal{O}_2 = -28$ (signos opuestos); $\mathcal{O}_3 = -35$ y $\mathcal{O}_4 = +19$ (signos opuestos).
     $$\implies \mathbf{\text{SÍ existe intersección propia en }} P \approx (4.89, 3.56)$$

2. **Casos especiales (Colinealidad, contacto y superposiciones):**
   Si alguna orientación es 0, el punto es colineal. Se intersectan si el punto colineal cae dentro de la caja delimitadora (`Bounding Box`) del segmento opuesto:
   $$\min(x_P, x_R) \le x_Q \le \max(x_P, x_R) \quad \land \quad \min(y_P, y_R) \le y_Q \le \max(y_P, y_R)$$
   * **Caso 2:** Los 4 determinantes valen 0. Pero las proyecciones en $X$ son $[1, 3]$ y $[5, 7]$. Como están separados por una brecha, **NO existe intersección**.
   * **Caso 3a:** Signos opuestos $\implies$ **SÍ existe intersección** en $(3, 2)$.
   * **Caso 3b:** $\mathcal{O}_1 = 0$ y $C(6,2)$ coincide con el extremo $B(6,2)$ $\implies$ **SÍ existe intersección por contacto**.
   * **Caso 3c:** Colineales con traslape en $X$ en el intervalo $[4, 6]$ $\implies$ **SÍ existe intersección por superposición**.

---

### 4. Implementación en Python: función `interseccion`

```python
def signo(val):
    """Retorna +1 si es positivo, -1 si es negativo y 0 si es cero."""
    if val > 0:
        return 1
    elif val < 0:
        return -1
    return 0

def orientacion(P, Q, R):
    """Calcula el determinante del producto cruz 2D para P -> Q -> R."""
    return (Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])

def en_segmento(P, Q, R):
    """
    Verifica si el punto Q (colineal con el segmento PR)
    se encuentra geométricamente dentro del segmento PR.
    """
    return (min(P[0], R[0]) <= Q[0] <= max(P[0], R[0]) and
            min(P[1], R[1]) <= Q[1] <= max(P[1], R[1]))

def interseccion(A, B, C, D):
    """
    Determina si el segmento AB y el segmento CD se cruzan o tocan,
    cubriendo cruce propio, contactos en extremos y superposiciones colineales.
    """
    # 1. Calculamos las cuatro orientaciones
    o1 = signo(orientacion(A, B, C))
    o2 = signo(orientacion(A, B, D))
    o3 = signo(orientacion(C, D, A))
    o4 = signo(orientacion(C, D, B))

    # 2. Cruce propio (Caso General)
    if o1 != o2 and o3 != o4 and (o1 != 0 and o2 != 0 and o3 != 0 and o4 != 0):
        return True

    # 3. Casos de colinealidad o contacto
    if o1 == 0 and en_segmento(A, C, B):
        return True
    if o2 == 0 and en_segmento(A, D, B):
        return True
    if o3 == 0 and en_segmento(C, A, D):
        return True
    if o4 == 0 and en_segmento(C, B, D):
        return True

    return False


if __name__ == "__main__":
    print("=== RESULTADOS EJERCICIO 2 ===")
    print("Caso 1 (Cruce Propio)     :", interseccion((1,1), (7,5), (2,6), (8,1)))  # True
    print("Caso 2 (Colineal Disjunto):", interseccion((1,1), (3,3), (5,5), (7,7)))  # False
    print("Caso 3a (Cruce Transversal):", interseccion((0,2), (6,2), (3,0), (3,5))) # True
    print("Caso 3b (Contacto Extremo) :", interseccion((0,2), (6,2), (6,2), (9,5))) # True
    print("Caso 3c (Superposición)    :", interseccion((0,2), (6,2), (4,2), (9,2))) # True
```

---

### 5. Demostración de complejidad $O(1)$

> **Pregunta:** *¿Por qué la detección de una intersección entre dos segmentos de recta tiene complejidad $O(1)$?*

1. **Número finito y acotado de operaciones:**
   * La rutina calcula exactamente **4 llamadas a `orientacion`**.
   * Cada llamada a `orientacion` realiza un número constante de operaciones algebraicas elementales: 4 restas, 2 multiplicaciones y 1 resta final (total = 7 operaciones por orientación $\times 4 = 28$ operaciones).
   * La verificación de pertenencia (`en_segmento`) realiza un número constante de comparaciones de cota (`min`, `max`, `<=`), como máximo 4 veces.
2. **Independencia del tamaño o coordenadas:**
   * El algoritmo opera de manera directa y cerrada sobre las 8 coordenadas escalares de entrada $(x_A, y_A, x_B, y_B, x_C, y_C, x_D, y_D)$.
   * No existe ningún bucle (`while`, `for`), no hay recursión ni aproximación iterativa.
3. **Conclusión formal:**
   $$T = k \cdot c = \mathbf{O(1)}, \qquad S = \mathbf{O(1)}$$
   Tanto el tiempo de cómputo como el espacio en memoria son **estrictamente constantes**.

---

## Ejercicio 3: Comprobaciones entre $N$ Tuberías

Para verificar todos los pares posibles de una lista de $n$ tuberías:
```python
for i in range(n):
    for j in range(i + 1, n):
        interseccion(tubos[i], tubos[j])
```

### 1. ¿Por qué `j = i + 1`?
* Evita comparar una tubería consigo misma ($i = j$).
* Evita comparar pares dos veces: `interseccion(tubo_A, tubo_B)` es idéntico a `interseccion(tubo_B, tubo_A)`.

### 2. Tabla de iteraciones

#### Para $N = 5$:
* $i = 0 \implies j \in \{1, 2, 3, 4\} \implies 4$ comparaciones
* $i = 1 \implies j \in \{2, 3, 4\} \implies 3$ comparaciones
* $i = 2 \implies j \in \{3, 4\} \implies 2$ comparaciones
* $i = 3 \implies j \in \{4\} \implies 1$ comparación
* $i = 4 \implies$ Ninguna $\implies 0$ comparaciones
* **Total:** $4 + 3 + 2 + 1 + 0 = \mathbf{10 \text{ comprobaciones}}$

#### Para $N = 8$:
* **Total:** $7 + 6 + 5 + 4 + 3 + 2 + 1 + 0 = \mathbf{28 \text{ comprobaciones}}$

### 3. Expresión matemática exacta de $T(n)$
$$T(n) = \sum_{i=0}^{n-1} \sum_{j=i+1}^{n-1} 1 = \sum_{i=0}^{n-1} (n - 1 - i) = \frac{n(n - 1)}{2} = \binom{n}{2}$$

### 4. Orden de complejidad
$$T(n) = \frac{1}{2}n^2 - \frac{1}{2}n \implies \mathbf{T(n) = \Theta(n^2)}$$

### 5. Valores para grandes cantidades

| $n$ (Tuberías) | Cálculo exacto $\frac{n(n-1)}{2}$ | Total de comprobaciones |
|:---:|:---:|:---:|
| **$100$** | $\frac{100 \times 99}{2}$ | **$4,950$** |
| **$1,000$** | $\frac{1000 \times 999}{2}$ | **$499,500$** |
| **$10,000$** | $\frac{10000 \times 9999}{2}$ | **$49,995,000$** |

---

## Ejercicio 4: Triangulación de un Terreno (Ear Clipping)

Polígono simple recorrido en sentido antihorario:
$$A(0,0) \to B(8,0) \to C(8,6) \to D(4,3) \to E(0,6) \to A$$

### 1. Clasificación de Vértices

| Vértice | Vecino Anterior | Vecino Siguiente | Determinante $\Delta$ | Clasificación | ¿Es oreja válida? |
|:---:|:---:|:---:|:---:|:---:|:---|
| **$A(0,0)$** | $E(0,6)$ | $B(8,0)$ | $+48$ | Convexo | No ($D$ cae en la diagonal $EB$) |
| **$B(8,0)$** | $A(0,0)$ | $C(8,6)$ | $+48$ | Convexo | No ($D$ cae en la diagonal $AC$) |
| **$C(8,6)$** | $B(8,0)$ | $D(4,3)$ | $+24$ | Convexo | **Sí (Oreja inicial válida)** |
| **$D(4,3)$** | $C(8,6)$ | $E(0,6)$ | $\mathbf{-24}$ | **Cóncavo** | **No** (vértice reflejo) |
| **$E(0,6)$** | $D(4,3)$ | $A(0,0)$ | $+24$ | Convexo | **Sí (Oreja válida)** |

### 2. Cantidad de Triángulos y Diagonales ($n=5$)
* **Número de triángulos:** $n - 2 = 5 - 2 = \mathbf{3 \text{ triángulos}}$.
* **Número de diagonales internas:** $n - 3 = 5 - 3 = \mathbf{2 \text{ diagonales}}$.

### 3. Triangulación final
Con diagonales $BD$ y $AD$, se obtienen los 3 triángulos:
1. $\triangle BCD$ (Área = $12$)
2. $\triangle ABD$ (Área = $12$)
3. $\triangle ADE$ (Área = $12$)
* **Área Total:** $12 + 12 + 12 = \mathbf{36 \text{ u}^2}$.

### 4. Condiciones para recortar una Oreja
1. **Convexidad:** El vértice debe tener un ángulo interior menor a $180^\circ$ ($\Delta > 0$).
2. **Triángulo vacío:** Ningún otro vértice del polígono puede quedar en el interior o sobre el borde del triángulo formado.
3. **Diagonal interna estricta:** La diagonal que une a sus dos vecinos debe quedar completamente dentro del polígono sin cortar aristas.

---

##  Ejercicio 5: Comparación de algoritmos de triangulación

> **Análisis de complejidad temporal:** comparación entre un algoritmo cúbico `O(n³)` y uno cuadrático `O(n²)`.

---

## 1. Comprensión y planteamiento del problema

Una empresa de videojuegos necesita dividir polígonos que representan terrenos, edificios y obstáculos en regiones triangulares (**triangulación**), porque los motores gráficos y de colisiones trabajan de forma eficiente con triángulos. Dos equipos proponen implementaciones distintas y, como analizadores de algoritmos, debemos responder: 

**¿qué algoritmo conviene utilizar?**

| Propuesta       | Descripción                                            | Modelo de complejidad |
|-----------------|--------------------------------------------------------|-----------------------|
| **Algoritmo A** | Implementación sencilla con verificaciones repetidas.  | Cúbica: `n³`          |
| **Algoritmo B** | Implementación mucho más eficiente.                    | Cuadrática: `n²`      |

El propósito de este trabajo no es probar cuál de las dos produce una triangulación correcta, sino comparar el costo teórico de las dos propuestas a medida que aumenta el tamaño del polígono.

---

## 2. Identificación de la variable de entrada

La variable de entrada se define como:

`n` = número de vértices del polígono

Los tamaños de entrada que exige el enunciado son:

- `n = 10`
- `n = 100`
- `n = 1.000`

Se aclara que `n` es la cantidad de vértices que recibe el algoritmo, no el número de triángulos que se obtienen al final. Un polígono simple de `n` vértices siempre produce `n − 2` triángulos.

```text
             V2
          /   |  \
         /    |   \
       V3-----|----V1
        \ \   |   / 
         \  \ |  /
          \   X
         /  / |  \
       V4----|----V0
         \   |   /
          \  |  /
           V5---V6
              V7
```

**Figura 1.** Ejemplo de triangulación: un polígono de `n = 8` vértices se divide en `n − 2 = 6` triángulos.

---

## 3. Planteamiento de las funciones de tiempo

A partir de las complejidades dadas por el enunciado, y con coeficiente constante igual a uno, se establecen las siguientes funciones:

- **Algoritmo A (cúbico):** `T_A(n) = n^3`
- **Algoritmo B (cuadrático):** `T_B(n) = n^2`

> **Supuesto del modelo:** como el enunciado no entrega coeficientes ni costos adicionales, se comparan directamente `n³` y `n²`. Los valores son unidades teóricas de operación, no segundos de ejecución medidos.

---

## 4. Cálculo de las funciones

Se sustituyen los tres tamaños de entrada en las funciones de cada algoritmo.

### Caso 1: `n = 10`

| Algoritmo | Desarrollo                                          |
|-----------|----------------------------------------------------:|
| A         | `T_A(10) = 10^3 = 10 × 10 × 10 = 1.000`             |
| B         | `T_B(10) = 10^2 = 10 × 10 = 100`                    |

### Caso 2: `n = 100`

| Algoritmo | Desarrollo                                          |
|-----------|----------------------------------------------------:|
| A         | `T_A(100) = 100^3 = 100 × 100 × 100 = 1.000.000`    |
| B         | `T_B(100) = 100^2 = 100 × 100 = 10.000`             |

### Caso 3: `n = 1.000`

| Algoritmo | Desarrollo                                                     |
|-----------|---------------------------------------------------------------:|
| A         | `T_A(1.000) = 1.000^3 = 1.000 × 1.000 × 1.000 = 1.000.000.000` |
| B         | `T_B(1.000) = 1.000^2 = 1.000 × 1.000 = 1.000.000`             |

---

## 5. Tabla comparativa

La siguiente tabla reúne los resultados obtenidos para ambos algoritmos:

| Tamaño `n` | `T_A(n) = n^3` | `T_B(n) = n^2` | `Big O de A` | `Big O de B` |
|-----------:|---------------:|---------------:|-------------:|-------------:|
| 10         | 1.000          | 100            | `O(n³)`      | `O(n²)`      |
| 100        | 1.000.000      | 10.000         | `O(n³)`      | `O(n²)`      |
| 1.000      | 1.000.000.000  | 1.000.000      | `O(n³)`      | `O(n²)`      |

### Observaciones

- El algoritmo A realiza más operaciones que el B en los tres tamaños de entrada.
- La diferencia absoluta crece muy rápido: 900 operaciones de diferencia con `n = 10`, 990.000 con `n = 100` y 999.000.000 con `n = 1.000`.
- La tendencia es clara: cada vez que `n` se multiplica por 10, A se multiplica por 1.000 y B solo por 100.

---

## 6. Determinación de la complejidad Big O

Las dos funciones tienen un único término, así que la clase de crecimiento se identifica directamente:

```text
T_A(n) = n^3  =>  O(n^3)
```

```text
T_B(n) = n^2  =>  O(n^2)
```

La función cúbica crece más rápidamente que la cuadrática cuando `n` aumenta, por lo que `n^2 = O(n^3)`, pero `n^3` no es `O(n^2)`. La notación Big O describe la tendencia de crecimiento del costo respecto al tamaño de entrada, no el tiempo exacto en segundos.

---

## 7. Cálculo de la razón entre los algoritmos

Se divide el costo teórico del algoritmo A entre el costo teórico del algoritmo B:

```text
T_A(n) / T_B(n) = n^3 / n^2 = n
```

| Tamaño `n` | Sustitución                         | Resultado de la razón |
|-----------:|-------------------------------------|----------------------:|
| 10         | `10^3 / 10^2 = 1.000 / 100`         | **10**                |
| 100        | `100^3 / 100^2 = 1.000.000 / 10.000`| **100**               |
| 1.000      | `1.000^3 / 1.000^2 = 10^9 / 10^6`   | **1.000**             |

**Interpretación:** la razón indica cuántas veces es mayor el costo teórico de A frente al de B. Con 10 vértices A cuesta 10 veces más; con 100 vértices, 100 veces más; y con 1.000 vértices, 1.000 veces más. La ventaja de B no es constante: crece de forma lineal con `n`.

---

## 8. Representación gráfica

El gráfico usa escala logarítmica en ambos ejes: eje X = tamaño de entrada `n`, eje Y = operaciones teóricas `T(n)`, con una curva por algoritmo y los tamaños `n = 10`, `n = 100` y `n = 1.000` marcados. En escala log-log, `n³` y `n²` aparecen como rectas con pendientes 3 y 2, y la separación vertical entre ellas es precisamente la razón `n`.

```text
Operaciones T(n) [Escala Logarítmica]
  ^
10^9 |                                          *  T_A(1000) = 1.000.000.000
10^8 |                                        / |
10^7 |                                      /   |  <-- Razón = 1.000x
10^6 |                        *           /     o  T_B(1000) = 1.000.000
10^5 |                      / |         /     /
10^4 |                    /   o       /     /      T_B(100)  = 10.000
10^3 |      *           /   /       /     /        T_A(10)   = 1.000
10^2 |    / o         /   /       /     /          T_B(10)   = 100
10^1 |  / /         /   /       /     /
  0  +------+---------+---------+-------------------> Tamaño de entrada (n)
          n=10      n=100     n=1.000

  Leyenda:   *---* Algoritmo A: O(n³)      o---o Algoritmo B: O(n²)
```

**Figura 2.** Crecimiento de `T_A(n) = n^3` y `T_B(n) = n^2` en escala logarítmica.

```text
Razón T_A(n) / T_B(n)
  ^
1.000 |                                   [#]  1.000 veces más costoso
      |                                   [#]
  500 |                                   [#]
      |                                   [#]
  100 |                  [#]              [#]  100 veces más costoso
   10 |    [#]           [#]              [#]  10 veces más costoso
    0 +-----+-------------+----------------+-------> Tamaño de entrada (n)
          n=10          n=100           n=1.000
```

**Figura 3.** Razón `T_A(n) / T_B(n)` para `n = 10`, `100` y `1.000`.

---

## 9. Análisis e interpretación de los resultados

1. **¿Cuál realiza más operaciones?** El algoritmo A, para todo `n > 1`. Con `n = 1.000` son 1.000 millones de operaciones frente a 1 millón del B.
2. **¿Cómo cambia la diferencia?** Pasa de 900 a 990.000 y luego a 999.000.000 operaciones. Al multiplicar `n` por 10, la diferencia se multiplica aproximadamente por 1.000.
3. **¿Qué significa la razón?** Que A necesita `n` veces más operaciones que B; mientras más grande el polígono, mayor es la ventaja del algoritmo B.
4. **¿Por qué `n²` es más favorable que `n³`?** Porque `n^3 = n · n^2`, es decir, A hace el mismo trabajo que B multiplicado por un factor que crece con la entrada. Para entradas pequeñas la diferencia puede pasar desapercibida, pero para entradas grandes se vuelve decisiva.
5. **¿Qué efecto tendría el crecimiento cúbico en un videojuego?** Un videojuego debe mantener unos 60 cuadros por segundo (≈ 16 ms por cuadro). Si el terreno o los obstáculos tienen miles de vértices, un algoritmo cúbico podría causar tirones (*lag*), tiempos de carga largos y mayor consumo de CPU, mientras que uno cuadrático escala de forma mucho más manejable.

---

## 10. Conclusión y elección del algoritmo

Conviene utilizar el **algoritmo B**. Su crecimiento `O(n²)` es teóricamente más favorable que el `O(n³)` del algoritmo A: la razón `T_A(n) / T_B(n) = n` muestra que A es 10, 100 y 1.000 veces más costoso para `n = 10`, `n = 100` y `n = 1.000`, respectivamente, y la brecha sigue ampliándose con el tamaño del polígono.

Sin embargo, la complejidad no demuestra por sí sola que una implementación sea geométricamente correcta. Antes de usar B en producción, la empresa debe comprobar que triangule correctamente los polígonos requeridos (incluidos los cóncavos) y que respete las condiciones del problema. Además, este análisis usa coeficientes iguales a uno; en la práctica conviene complementarlo con mediciones de tiempo reales.

---

## Anexo A. Códigos de ejemplo en Python

Aunque el enunciado ya entrega los modelos de complejidad, se presentan dos implementaciones de ejemplo de triangulación por **recorte de orejas** (*ear clipping*) para ilustrar de dónde pueden provenir `n³` y `n²`. Un vértice es una “oreja” si el triángulo formado con sus dos vecinos es convexo y no contiene a ningún otro vértice del polígono.

### A.1. Algoritmo A: `O(n³)`, verificaciones repetidas

En cada una de las `n` iteraciones se recalculan todas las orejas: `n` iteraciones × `n` candidatos × `n` comprobaciones.

```text
Algoritmo A - Triangulación por "ear clipping" ingenuo. Complejidad: O(n^3)

Idea: en CADA iteración se vuelven a verificar TODOS los vértices para saber
cuáles son "orejas" (verificaciones repetidas). Cada verificación revisa los
demás vértices del polígono.

n iteraciones x n candidatos x n comprobaciones = O(n^3)
```

```python
import math


def cruz(a, b, c):
    """Producto cruz (b-a) x (c-a). > 0 => giro a la izquierda (antihorario)."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def punto_en_triangulo(p, a, b, c):
    return cruz(a, b, p) >= 0 and cruz(b, c, p) >= 0 and cruz(c, a, p) >= 0


def es_oreja(poli, idx, i, contador):
    """Verifica si el vértice idx[i] es una oreja. Cuesta O(n)."""
    m = len(idx)
    a, b, c = poli[idx[i - 1]], poli[idx[i]], poli[idx[(i + 1) % m]]

    if cruz(a, b, c) <= 0:            # vértice reflejo (no convexo)
        return False

    for j in range(m):                # revisa los demás vértices
        if j in (i - 1, i, (i + 1) % m):
            continue
        contador[0] += 1              # operación elemental contada
        if punto_en_triangulo(poli[idx[j]], a, b, c):
            return False

    return True


def triangular_A(poli):
    """poli: lista de (x, y) en sentido antihorario. Devuelve (triángulos, operaciones)."""
    idx = list(range(len(poli)))
    triangulos, contador = [], [0]

    while len(idx) > 3:
        # Se recalculan TODAS las orejas en cada iteración (costo O(n^2))
        orejas = [i for i in range(len(idx)) if es_oreja(poli, idx, i, contador)]
        i = orejas[0]
        triangulos.append((idx[i - 1], idx[i], idx[(i + 1) % len(idx)]))
        idx.pop(i)                    # se "corta" la oreja

    triangulos.append(tuple(idx))
    return triangulos, contador[0]


def poligono_regular(n):
    return [
        (math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n))
        for k in range(n)
    ]


if __name__ == "__main__":
    for n in (10, 50, 100):
        tris, ops = triangular_A(poligono_regular(n))
        print(
            f"n={n:4d}  triángulos={len(tris):4d}  "
            f"operaciones={ops:10d}  n^3={n**3:10d}"
        )
```

### A.2. Algoritmo B: `O(n²)`, orejas almacenadas

Las orejas se calculan una sola vez y, al cortar una, solo se re-verifican sus dos vecinos.

```text
Algoritmo B - Ear clipping optimizado. Complejidad: O(n^2)

Idea: se calcula UNA sola vez cuáles vértices son orejas y se guarda el
resultado. Al cortar una oreja solo cambian sus dos vecinos, así que
únicamente esos dos se vuelven a verificar (no todos).

inicio: n candidatos x n comprobaciones          = O(n^2)
n iteraciones x 2 re-verificaciones x O(n)       = O(n^2)
Total                                            = O(n^2)
```

```python
from algoritmo_a import cruz, punto_en_triangulo, poligono_regular


def triangular_B(poli):
    """poli: lista de (x, y) en sentido antihorario. Devuelve (triángulos, operaciones)."""
    n = len(poli)
    prev = [(i - 1) % n for i in range(n)]      # lista doblemente enlazada
    sig = [(i + 1) % n for i in range(n)]
    contador = [0]

    def es_oreja(i):
        a, b, c = poli[prev[i]], poli[i], poli[sig[i]]
        if cruz(a, b, c) <= 0:
            return False

        j = sig[sig[i]]
        while j != prev[i]:                    # recorre los demás vértices
            contador[0] += 1
            if punto_en_triangulo(poli[j], a, b, c):
                return False
            j = sig[j]

        return True

    oreja = [es_oreja(i) for i in range(n)]      # cálculo inicial: O(n^2)
    triangulos, restantes, i = [], n, 0

    while restantes > 3:
        while not oreja[i]:                     # busca una oreja ya marcada
            i = sig[i]

        p, s = prev[i], sig[i]
        triangulos.append((p, i, s))
        sig[p], prev[s] = s, p                  # se elimina el vértice i
        restantes -= 1
        oreja[p], oreja[s] = es_oreja(p), es_oreja(s)  # solo 2 re-verificaciones
        i = s

    triangulos.append((prev[i], i, sig[i]))
    return triangulos, contador[0]


if __name__ == "__main__":
    for n in (10, 100, 1000):
        tris, ops = triangular_B(poligono_regular(n))
        print(
            f"n={n:5d}  triángulos={len(tris):5d}  "
            f"operaciones={ops:10d}  n^2={n**2:10d}"
        )
```

> **Dependencia entre archivos:** el ejemplo del algoritmo B importa `cruz`, `punto_en_triangulo` y `poligono_regular` desde `algoritmo_a`. Para ejecutarlo de esa manera, ambos archivos deben estar en la misma carpeta y el código del algoritmo A debe guardarse como `algoritmo_a.py`.

### A.3. Cálculo teórico y razón

```python
"""Cálculo teórico T_A(n)=n^3, T_B(n)=n^2 y razón T_A/T_B."""


def T_A(n):
    return n ** 3


def T_B(n):
    return n ** 2


print(f"{'n':>6} {'T_A(n)':>16} {'T_B(n)':>12} {'T_A/T_B':>10}")
for n in (10, 100, 1000):
    print(f"{n:>6} {T_A(n):>16,} {T_B(n):>12,} {T_A(n)/T_B(n):>10.0f}")
```

### A.4. Verificación experimental (conteo de operaciones)

Se ejecutaron ambos códigos sobre polígonos regulares contando las comprobaciones punto-en-triángulo. Los valores medidos tienen coeficientes distintos de uno (A ≈ `n³/3` y B ≈ `2n²`), pero confirman la forma del crecimiento: al multiplicar `n` por 10, A crece cerca de 1.000 veces y B cerca de 100 veces.

| `n`   | Operaciones A  | Operaciones B | `n³`          | `n²`      |
|------:|---------------:|--------------:|--------------:|----------:|
| 10    | 231            | 112           | 1.000         | 100       |
| 100   | 323.301        | 19.012        | 1.000.000     | 10.000    |
| 1.000 | No ejecutado*  | 1.990.012     | 1.000.000.000 | 1.000.000 |

*\* Con `n = 1.000`, A requeriría aproximadamente `3,3 × 10⁸` comprobaciones, demasiado lento para correrlo en Python puro.*

---

## Authors

- [@Jhoan Molina Gómez](https://github.com/Molina-university)
- [@Adrian Camilo Rincon](https://github.com/CamiloRincon17)