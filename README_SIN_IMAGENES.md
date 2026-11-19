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
| **Caso 2** | $(2, 1)$ | $(6, 5)$ | $(8, 2)$ | **$-20$** | **Horario (Derecha)** |
| **Caso 3** | $(1, 1)$ | $(3, 3)$ | $(6, 6)$ | **$0$** | **Colineal (Sin giro)** |
| **Caso 4** | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ | **$-15$** | **Horario (Derecha)** |

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
