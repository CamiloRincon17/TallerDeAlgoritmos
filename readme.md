# Taller de Algoritmos: Geometría Computacional

> Solución analítica, deducciones paso a paso, diagramas en texto (ASCII), análisis de complejidad $T(n)$ y código en Python.
> Documento 100 % autocontenido en Markdown: no usa imágenes externas.

---

## Resumen de resultados

| Ejercicio | Tema | Resultado clave |
|:---:|:---|:---|
| **1** | Giro de un robot autónomo | $\Delta = +18,\ -20,\ 0,\ -15$ → izquierda, derecha, recto, derecha |
| **2** | Intersección de rutas | Cruce propio, disjunto, cruce, contacto y superposición, todo en $O(1)$ |
| **3** | Comprobaciones entre $n$ tuberías | $T(n) = \frac{n(n-1)}{2} = \Theta(n^2)$ |
| **4** | Triangulación de un terreno | 3 triángulos, 2 diagonales, área total $36\ \text{u}^2$ |
| **5** | Algoritmo cúbico vs. cuadrático | $T_A/T_B = n$, conviene el algoritmo B |

## Tabla de contenidos

1. [Fundamentos teóricos: orientación en el plano](#fundamentos-teóricos-orientación-en-el-plano)
2. [Ejercicio 1: Giro del robot autónomo](#ejercicio-1-giro-del-robot-autónomo)
3. [Ejercicio 2: Intersección de rutas de autos autónomos](#ejercicio-2-intersección-de-rutas-de-autos-autónomos)
4. [Ejercicio 3: Comprobaciones entre n tuberías](#ejercicio-3-comprobaciones-entre-n-tuberías)
5. [Ejercicio 4: Triangulación de un terreno (ear clipping)](#ejercicio-4-triangulación-de-un-terreno-ear-clipping)
6. [Ejercicio 5: Comparación de algoritmos de triangulación](#ejercicio-5-comparación-de-algoritmos-de-triangulación)
7. [Anexo A: Códigos en Python](#anexo-a-códigos-en-python)
8. [Autores](#autores)

---

## Fundamentos teóricos: orientación en el plano

La herramienta central de la geometría computacional 2D es la **función de orientación** (producto cruz 2D).

Dados tres puntos $P(x_P, y_P)$, $Q(x_Q, y_Q)$ y $R(x_R, y_R)$, el determinante de la matriz homogénea es el **doble del área signada** del triángulo $\triangle PQR$:

$$
\mathrm{orient}(P, Q, R) = \det \begin{pmatrix} x_P & y_P & 1 \\ x_Q & y_Q & 1 \\ x_R & y_R & 1 \end{pmatrix} = (x_Q - x_P)(y_R - y_P) - (y_Q - y_P)(x_R - x_P)
$$

### Criterio de decisión

| Signo de $\Delta$ | Orientación | Significado |
|:---:|:---:|:---|
| $\Delta > 0$ | **Antihorario (CCW)** | $R$ queda a la **izquierda** de $\vec{PQ}$ (giro a la izquierda). |
| $\Delta < 0$ | **Horario (CW)** | $R$ queda a la **derecha** de $\vec{PQ}$ (giro a la derecha). |
| $\Delta = 0$ | **Colineal** | Los tres puntos están sobre la misma recta. |

Además, el **área** del triángulo es $\text{Área} = \dfrac{|\Delta|}{2}$.

---

## Ejercicio 1: Giro del robot autónomo

### 1. Comprensión y planteamiento del problema

Un robot autónomo se desplaza dentro de una bodega. Para decidir si gira a la izquierda, a la derecha o sigue recto, analiza tres posiciones consecutivas:

* $A$: posición anterior
* $B$: posición actual
* $C$: posición de destino

**Pregunta:** ¿qué giro hace el robot en cada uno de los cuatro casos dados?

### 2. Identificación de los datos de entrada

| Caso | $A$ (anterior) | $B$ (actual) | $C$ (destino) |
|:---:|:---:|:---:|:---:|
| 1 | $(1, 2)$ | $(5, 3)$ | $(3, 7)$ |
| 2 | $(2, 1)$ | $(6, 5)$ | $(8, 2)$ |
| 3 | $(1, 1)$ | $(3, 3)$ | $(6, 6)$ |
| 4 | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ |

### 3. Planteamiento de la función

$$\Delta = (x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A)$$

Equivale al producto cruz $\vec{AB} \times \vec{AC}$, y su signo decide el giro (ver tabla de fundamentos).

### 4. Cálculo del determinante para cada caso

**Caso 1:** $A(1,2)$, $B(5,3)$, $C(3,7)$

* $\vec{AB} = (4, 1)$ y $\vec{AC} = (2, 5)$
* $\Delta_1 = (4)(5) - (1)(2) = 20 - 2 = \mathbf{+18}$

**Caso 2:** $A(2,1)$, $B(6,5)$, $C(8,2)$

* $\vec{AB} = (4, 4)$ y $\vec{AC} = (6, 1)$
* $\Delta_2 = (4)(1) - (4)(6) = 4 - 24 = \mathbf{-20}$

**Caso 3:** $A(1,1)$, $B(3,3)$, $C(6,6)$

* $\vec{AB} = (2, 2)$ y $\vec{AC} = (5, 5)$
* $\Delta_3 = (2)(5) - (2)(5) = 10 - 10 = \mathbf{0}$

**Caso 4:** $A(0,4)$, $B(5,4)$, $C(3,1)$

* $\vec{AB} = (5, 0)$ y $\vec{AC} = (3, -3)$
* $\Delta_4 = (5)(-3) - (0)(3) = -15 - 0 = \mathbf{-15}$

### 5. Tabla resumen

| Caso | $A$ | $B$ | $C$ | $\Delta$ | Clasificación |
|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | $(1, 2)$ | $(5, 3)$ | $(3, 7)$ | **+18** | Antihorario (izquierda) |
| **2** | $(2, 1)$ | $(6, 5)$ | $(8, 2)$ | **−20** | Horario (derecha) |
| **3** | $(1, 1)$ | $(3, 3)$ | $(6, 6)$ | **0** | Colineal (sigue recto) |
| **4** | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ | **−15** | Horario (derecha) |

El código que reproduce esta tabla está en el [Anexo A.1](#a1-ejercicio-1-orientación-y-clasificación-del-giro).

### 6. Complejidad temporal $T(n)$

**Una sola terna.** Se hacen 4 restas de coordenadas, 2 multiplicaciones, 1 resta final y a lo sumo 2 comparaciones de signo. Son operaciones de costo constante:

$$T_{\text{terna}} = c_1 = \mathbf{O(1)}$$

**Una ruta de $n$ puntos.** Se evalúan $(n - 2)$ ternas consecutivas:

$$T(n) = \sum_{i=1}^{n-2} c_1 = c_1 (n - 2) + c_2 \implies \mathbf{T(n) = \Theta(n)}$$

* **Tiempo:** lineal en la cantidad de waypoints.
* **Espacio auxiliar:** $O(1)$.

### 7. Interpretación

1. El signo del determinante basta para decidir: no se necesitan ángulos, raíces ni funciones trigonométricas.
2. Solo se usan sumas y productos, así que con coordenadas enteras el resultado es **exacto** (sin errores de redondeo).
3. En el caso 3 el robot continúa recto porque $B$ queda entre $A$ y $C$. Si $C$ estuviera detrás de $A$, también daría $\Delta = 0$, pero sería una reversa. El determinante solo dice que son colineales.

### 8. Conclusión

El robot gira a la **izquierda** en el caso 1, a la **derecha** en los casos 2 y 4, y sigue **recto** en el caso 3. Revisar una ruta completa cuesta $\Theta(n)$.

---

## Ejercicio 2: Intersección de rutas de autos autónomos

### 1. Comprensión y planteamiento del problema

Dos autos autónomos recorren rutas representadas como segmentos de recta. Hay que decidir si dos segmentos $AB$ y $CD$ **se cruzan o se tocan**, cubriendo cuatro situaciones:

* cruce propio
* segmentos colineales disjuntos
* contacto en un extremo
* superposición colineal

### 2. Identificación de los datos de entrada

| Caso | Segmento $AB$ | Segmento $CD$ | Situación esperada |
|:---|:---:|:---:|:---|
| **1** | $A(1,1)$, $B(7,5)$ | $C(2,6)$, $D(8,1)$ | Cruce transversal propio |
| **2** | $A(1,1)$, $B(3,3)$ | $C(5,5)$, $D(7,7)$ | Colineales disjuntos |
| **3a** | $A(0,2)$, $B(6,2)$ | $C(3,0)$, $D(3,5)$ | Cruce vertical |
| **3b** | $A(0,2)$, $B(6,2)$ | $C(6,2)$, $D(9,5)$ | Contacto en el extremo $B$ |
| **3c** | $A(0,2)$, $B(6,2)$ | $C(4,2)$, $D(9,2)$ | Superposición colineal |

### 3. Planteamiento del método

Se calculan **cuatro orientaciones**:

* $\mathcal{O}_1 = \mathrm{orient}(A, B, C)$: lado de $C$ respecto a la recta $AB$
* $\mathcal{O}_2 = \mathrm{orient}(A, B, D)$: lado de $D$ respecto a la recta $AB$
* $\mathcal{O}_3 = \mathrm{orient}(C, D, A)$: lado de $A$ respecto a la recta $CD$
* $\mathcal{O}_4 = \mathrm{orient}(C, D, B)$: lado de $B$ respecto a la recta $CD$

**Regla 1, cruce propio.** Los segmentos se cruzan si los extremos de cada uno quedan en lados opuestos de la recta del otro:

$$(\mathcal{O}_1 \cdot \mathcal{O}_2 < 0) \ \land\ (\mathcal{O}_3 \cdot \mathcal{O}_4 < 0)$$

**Regla 2, casos especiales.** Si alguna orientación es $0$, ese punto es colineal con el otro segmento. Hay intersección si además cae dentro de su caja delimitadora (*bounding box*):

$$\min(x_P, x_R) \le x_Q \le \max(x_P, x_R) \ \land\ \min(y_P, y_R) \le y_Q \le \max(y_P, y_R)$$

### 4. Representación en el plano cartesiano

Leyenda: `#` segmento $AB$, `o` segmento $CD$, `X` punto de intersección, `█` tramo compartido.

**Caso 1: cruce transversal propio.** La intersección es $P = \left(\tfrac{44}{9}, \tfrac{97}{27}\right) \approx (4{,}89;\ 3{,}59)$ (cálculo en la sección 5).

```text
 y
 7 ┤ 
 6 ┤         Coo
 5 ┤           oooooo         ###B
 4 ┤                oooo█X#####
 3 ┤              #######oooooo
 2 ┤        #######           oooooo
 1 ┤     A###                      ooD
 0 ┤ 
   └───────────────────────────────────────▶ x
     0   1   2   3   4   5   6   7   8   9
```

**Caso 2: colineales disjuntos.** Intervalos en $X$: $[1,3]$ y $[5,7]$, con un hueco entre $x=3$ y $x=5$.

```text
 y
 8 ┤ 
 7 ┤                           ooD
 6 ┤                       ooooo
 5 ┤                     Coo
 4 ┤ 
 3 ┤           ##B
 2 ┤       #####
 1 ┤     A##
 0 ┤ 
   └───────────────────────────────────────▶ x
     0   1   2   3   4   5   6   7   8   9
```

**Caso 3a: cruce vertical** en el punto interior $(3,2)$.

```text
 y
 5 ┤             D
 4 ┤             o
 3 ┤             o
 2 ┤ A###########X###########B
 1 ┤             o
 0 ┤             C
   └───────────────────────────────▶ x
     0   1   2   3   4   5   6   7
```

**Caso 3b: contacto en el extremo.** $B$ y $C$ coinciden en $(6,2)$.

```text
 y
 5 ┤                                   ooD
 4 ┤                               ooooo
 3 ┤                           ooooo
 2 ┤ A#######################B=C
 1 ┤ 
 0 ┤ 
   └───────────────────────────────────────────▶ x
     0   1   2   3   4   5   6   7   8   9   10
```

**Caso 3c: superposición colineal.** El tramo compartido es $x \in [4, 6]$.

```text
 y
 4 ┤ 
 3 ┤ 
 2 ┤ A###############C███████BoooooooooooD
 1 ┤ 
 0 ┤ 
   └───────────────────────────────────────────▶ x
     0   1   2   3   4   5   6   7   8   9   10
```

### 5. Cálculo de las orientaciones

#### Caso 1: $A(1,1)$, $B(7,5)$, $C(2,6)$, $D(8,1)$

| Orientación | Vectores | Desarrollo | Valor |
|:---:|:---|:---|:---:|
| $\mathcal{O}_1 = \mathrm{orient}(A,B,C)$ | $\vec{AB}=(6,4)$, $\vec{AC}=(1,5)$ | $(6)(5)-(4)(1)=30-4$ | **+26** |
| $\mathcal{O}_2 = \mathrm{orient}(A,B,D)$ | $\vec{AB}=(6,4)$, $\vec{AD}=(7,0)$ | $(6)(0)-(4)(7)=0-28$ | **−28** |
| $\mathcal{O}_3 = \mathrm{orient}(C,D,A)$ | $\vec{CD}=(6,-5)$, $\vec{CA}=(-1,-5)$ | $(6)(-5)-(-5)(-1)=-30-5$ | **−35** |
| $\mathcal{O}_4 = \mathrm{orient}(C,D,B)$ | $\vec{CD}=(6,-5)$, $\vec{CB}=(5,-1)$ | $(6)(-1)-(-5)(5)=-6+25$ | **+19** |

**Punto de intersección.** Con las orientaciones se obtiene el parámetro sobre $AB$:

$$t = \frac{\mathcal{O}_3}{\mathcal{O}_3 - \mathcal{O}_4} = \frac{-35}{-54} = \frac{35}{54}$$

$$P = A + t\,\vec{AB} = \left(1 + 6\cdot\tfrac{35}{54},\ 1 + 4\cdot\tfrac{35}{54}\right) = \left(\tfrac{44}{9},\ \tfrac{97}{27}\right) \approx (4{,}89;\ 3{,}59)$$

#### Caso 2: $A(1,1)$, $B(3,3)$, $C(5,5)$, $D(7,7)$

Todos los puntos están sobre la recta $y = x$, así que las cuatro orientaciones valen $\mathbf{0}$.

#### Caso 3: $A(0,2)$, $B(6,2)$ frente a las tres variantes

| Variante | $C$ | $D$ | $\mathcal{O}_1$ | $\mathcal{O}_2$ | $\mathcal{O}_3$ | $\mathcal{O}_4$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **3a** Cruce | $(3,0)$ | $(3,5)$ | −12 | +18 | +15 | −15 |
| **3b** Contacto en $B$ | $(6,2)$ | $(9,5)$ | 0 | +18 | +18 | 0 |
| **3c** Superposición | $(4,2)$ | $(9,2)$ | 0 | 0 | 0 | 0 |

### 6. Determinación de la intersección

| Caso | Orientaciones | Razonamiento | ¿Intersecta? |
|:---:|:---|:---|:---:|
| **1** | $+26,\,-28,\,-35,\,+19$ | $\mathcal{O}_1\mathcal{O}_2<0$ y $\mathcal{O}_3\mathcal{O}_4<0$ (cruce propio) | **Sí** |
| **2** | $0,\,0,\,0,\,0$ | Colineales, pero las proyecciones en $X$ ($[1,3]$ y $[5,7]$) no se solapan | **No** |
| **3a** | $-12,\,+18,\,+15,\,-15$ | Signos opuestos en ambos pares | **Sí**, en $(3,2)$ |
| **3b** | $0,\,+18,\,+18,\,0$ | $\mathcal{O}_1=0$ y $C(6,2)$ coincide con el extremo $B$ | **Sí** (contacto) |
| **3c** | $0,\,0,\,0,\,0$ | Colineales y los intervalos en $X$ se solapan en $[4,6]$ | **Sí** (superposición) |

La función `interseccion` está en el [Anexo A.2](#a2-ejercicio-2-función-interseccion).

### 7. Complejidad: ¿por qué es $O(1)$?

1. **Cantidad finita y acotada de operaciones.**
   * Siempre son exactamente 4 llamadas a `orientacion`, con 7 operaciones cada una (4 restas, 2 productos y 1 resta final), es decir 28 operaciones.
   * `en_segmento` hace un número constante de comparaciones (`min`, `max`, `<=`) y se llama como máximo 4 veces.
2. **Independencia del tamaño.** El algoritmo trabaja directamente sobre las 8 coordenadas de entrada: no hay bucles, recursión ni aproximaciones iterativas.
3. **Conclusión formal:**

$$T = k \cdot c = \mathbf{O(1)}, \qquad S = \mathbf{O(1)}$$

### 8. Conclusión

Con solo cuatro determinantes y una verificación de caja delimitadora se resuelven todos los casos: cruce propio, contacto y superposición. El costo es constante, por eso este algoritmo sirve como **bloque básico** para problemas con muchos segmentos (ver Ejercicio 3).

---

## Ejercicio 3: Comprobaciones entre n tuberías

### 1. Comprensión y planteamiento del problema

Se quiere verificar si alguna de las $n$ tuberías (segmentos) se cruza con otra. La estrategia directa es comparar **todos los pares posibles** con la función `interseccion` del ejercicio anterior.

### 2. Identificación de la variable de entrada

$n$ = cantidad de tuberías. La operación a contar es **una llamada a `interseccion`**, que cuesta $O(1)$.

### 3. Planteamiento del algoritmo

```python
for i in range(n):
    for j in range(i + 1, n):
        interseccion(*tubos[i], *tubos[j])   # cada tubo = (P, Q)
```

**¿Por qué `j = i + 1`?**

* Evita comparar una tubería consigo misma ($i = j$).
* Evita repetir pares: `interseccion(A, B)` equivale a `interseccion(B, A)`.

### 4. Cálculo de las iteraciones

**Para $n = 5$:**

| $i$ | Valores de $j$ | Comparaciones |
|:---:|:---:|:---:|
| 0 | $1,2,3,4$ | 4 |
| 1 | $2,3,4$ | 3 |
| 2 | $3,4$ | 2 |
| 3 | $4$ | 1 |
| 4 | ninguno | 0 |
| **Total** | | **10** |

**Para $n = 8$:** $7+6+5+4+3+2+1+0 = \mathbf{28}$ comprobaciones.

### 5. Expresión exacta de $T(n)$

$$T(n) = \sum_{i=0}^{n-1} \sum_{j=i+1}^{n-1} 1 = \sum_{i=0}^{n-1} (n - 1 - i) = \frac{n(n - 1)}{2} = \binom{n}{2}$$

Comprobación: $T(5) = \frac{5 \cdot 4}{2} = 10$ ✓ y $T(8) = \frac{8 \cdot 7}{2} = 28$ ✓.

### 6. Orden de complejidad

$$T(n) = \tfrac{1}{2}n^2 - \tfrac{1}{2}n \implies \mathbf{T(n) = \Theta(n^2)}$$

Como cada comparación cuesta $O(1)$, el costo total del algoritmo también es $\Theta(n^2)$.

### 7. Tabla para grandes cantidades

| $n$ (tuberías) | Cálculo | Comprobaciones |
|---:|:---|---:|
| 100 | $\frac{100 \times 99}{2}$ | **4.950** |
| 1.000 | $\frac{1000 \times 999}{2}$ | **499.500** |
| 10.000 | $\frac{10000 \times 9999}{2}$ | **49.995.000** |

### 8. Interpretación

* Al multiplicar $n$ por 10, las comprobaciones se multiplican por cerca de **100**, el comportamiento típico de un algoritmo cuadrático.
* Duplicar la cantidad de tuberías cuadruplica el trabajo, porque $T(2n) \approx 4\,T(n)$.
* Con 10.000 tuberías ya son casi 50 millones de llamadas a `interseccion`.

### 9. Conclusión

Comparar todos los pares es simple y correcto, pero cuesta $\Theta(n^2)$. Funciona bien con pocas tuberías y se vuelve costoso con miles. Para entradas grandes existen algoritmos de barrido (*sweep line*) que reducen el trabajo.

---

## Ejercicio 4: Triangulación de un terreno (ear clipping)

### 1. Comprensión y planteamiento del problema

Se debe dividir un terreno poligonal en triángulos usando **recorte de orejas** (*ear clipping*): una "oreja" es un vértice cuyo triángulo con sus dos vecinos se puede recortar sin dejar fuera ni cruzar nada del polígono.

### 2. Identificación de los datos de entrada

Polígono simple recorrido en sentido antihorario, con $n = 5$ vértices:

$$A(0,0) \to B(8,0) \to C(8,6) \to D(4,3) \to E(0,6) \to A$$

```text
 y
 6 ┤ E               C
 5 ┤ │  ╲         ╱  │
 4 ┤ │    ╲     ╱    │
 3 ┤ │       D       │
 2 ┤ │               │
 1 ┤ │               │
 0 ┤ A───────────────B
   └─────────────────────▶ x
     0       4       8
```

*Esquema sin escala exacta: es un rectángulo de $8 \times 6$ con una muesca en V en la parte superior.*

**Verificación del sentido (fórmula del área de Gauss):**

$$2\cdot\text{Área} = \sum (x_i y_{i+1} - x_{i+1} y_i) = 0 + 48 + 0 + 24 + 0 = 72 > 0 \implies \text{antihorario},\ \text{Área} = 36\ \text{u}^2$$

### 3. Planteamiento del método

Para cada vértice $V$ con vecino anterior $P$ y siguiente $N$ se calcula $\Delta = \mathrm{orient}(P, V, N)$. Un vértice es **oreja** si cumple las tres condiciones:

1. **Convexidad:** ángulo interior menor a $180^\circ$ ($\Delta > 0$).
2. **Triángulo vacío:** ningún otro vértice del polígono queda dentro del triángulo $\triangle PVN$ ni sobre su borde.
3. **Diagonal interna:** la diagonal $PN$ queda dentro del polígono sin cortar aristas.

### 4. Clasificación de los vértices

| Vértice | Anterior | Siguiente | $\Delta$ | Tipo | ¿Oreja? | Razón |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $A(0,0)$ | $E$ | $B$ | +48 | Convexo | No | $D$ está sobre la diagonal $EB$ |
| $B(8,0)$ | $A$ | $C$ | +48 | Convexo | No | $D$ está sobre la diagonal $AC$ |
| $C(8,6)$ | $B$ | $D$ | +24 | Convexo | **Sí** | Triángulo $BCD$ vacío |
| $D(4,3)$ | $C$ | $E$ | **−24** | **Cóncavo** | No | Vértice reflejo |
| $E(0,6)$ | $D$ | $A$ | +24 | Convexo | **Sí** | Triángulo $DEA$ vacío |

Cálculo de ejemplo para $D$: $\vec{CD} = (-4,-3)$ y $\vec{CE} = (-8,0)$, entonces $\Delta = (-4)(0) - (-3)(-8) = -24$.

### 5. Proceso de recorte paso a paso

| Paso | Polígono actual | Oreja recortada | Triángulo | Diagonal creada | Área |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | $A, B, C, D, E$ | $C$ | $\triangle BCD$ | $BD$ | 12 |
| 2 | $A, B, D, E$ | $B$ | $\triangle ABD$ | $AD$ | 12 |
| 3 | $A, D, E$ | (último triángulo) | $\triangle ADE$ | n/a | 12 |

Después del paso 1, $D$ queda alineado con $B$ y $E$ ($\Delta = 0$), por eso en el paso 2 se recorta $B$.

### 6. Cantidad de triángulos y diagonales

Para un polígono simple de $n$ vértices:

* **Triángulos:** $n - 2 = 5 - 2 = \mathbf{3}$
* **Diagonales internas:** $n - 3 = 5 - 3 = \mathbf{2}$ (son $BD$ y $AD$)

### 7. Triangulación final

```text
 y
 6 ┤ E               C
 5 ┤ │  ╲         ╱  │
 4 ┤ │    ╲     ╱    │
 3 ┤ │       D       │
 2 ┤ │    ╱     ╲    │
 1 ┤ │  ╱         ╲  │
 0 ┤ A───────────────B
   └─────────────────────▶ x
     0       4       8
```

*Las diagonales $AD$ y $BD$ parten el terreno en $\triangle ADE$ (izquierda), $\triangle ABD$ (abajo) y $\triangle BCD$ (derecha).*

| Triángulo | Cálculo del área | Área |
|:---:|:---|:---:|
| $\triangle BCD$ | base $BC = 6$, altura $4$ → $\frac{6 \cdot 4}{2}$ | 12 |
| $\triangle ABD$ | base $AB = 8$, altura $3$ → $\frac{8 \cdot 3}{2}$ | 12 |
| $\triangle ADE$ | base $AE = 6$, altura $4$ → $\frac{6 \cdot 4}{2}$ | 12 |
| **Total** | | **36 u²** |

El total coincide con el área del polígono obtenida por Gauss (36), lo que confirma la triangulación.

### 8. Complejidad

* Una implementación ingenua que recalcula todas las orejas en cada iteración cuesta $O(n^3)$.
* Si se guardan las orejas y solo se re-verifican los dos vecinos del vértice recortado, cuesta $O(n^2)$.

Ese contraste es justamente el que se analiza en el Ejercicio 5.

### 9. Conclusión

El terreno se triangula con **3 triángulos** y **2 diagonales** ($BD$ y $AD$), y cada triángulo tiene área 12. El único vértice cóncavo, $D$, nunca es oreja, pero termina conectado con $A$ y $B$ por las diagonales.

---

## Ejercicio 5: Comparación de algoritmos de triangulación

> **Análisis de complejidad temporal:** comparación entre un algoritmo cúbico $O(n^3)$ y uno cuadrático $O(n^2)$.

### 1. Comprensión y planteamiento del problema

Una empresa de videojuegos necesita dividir polígonos que representan terrenos, edificios y obstáculos en regiones triangulares (**triangulación**), porque los motores gráficos y de colisiones trabajan de forma eficiente con triángulos. Dos equipos proponen implementaciones distintas y, como analizadores de algoritmos, debemos responder:

**¿Qué algoritmo conviene utilizar?**

| Propuesta | Descripción | Modelo de complejidad |
|:---|:---|:---:|
| **Algoritmo A** | Implementación sencilla con verificaciones repetidas. | Cúbica: $n^3$ |
| **Algoritmo B** | Implementación mucho más eficiente. | Cuadrática: $n^2$ |

El propósito no es probar cuál produce una triangulación correcta, sino comparar el **costo teórico** de ambas a medida que crece el polígono.

### 2. Identificación de la variable de entrada

$n$ = número de vértices del polígono. Los tamaños exigidos son $n = 10$, $n = 100$ y $n = 1.000$.

$n$ es la cantidad de vértices que recibe el algoritmo, no el número de triángulos del resultado. Un polígono simple de $n$ vértices siempre produce $n - 2$ triángulos.

```text
 y
 6 ┤ E               C
 5 ┤ │  ╲         ╱  │
 4 ┤ │    ╲     ╱    │
 3 ┤ │       D       │
 2 ┤ │    ╱     ╲    │
 1 ┤ │  ╱         ╲  │
 0 ┤ A───────────────B
```

**Figura 1.** Ejemplo de triangulación (el terreno del Ejercicio 4): $n = 5$ vértices se dividen en $n - 2 = 3$ triángulos.

### 3. Planteamiento de las funciones de tiempo

Con coeficiente constante igual a uno:

* **Algoritmo A (cúbico):** $T_A(n) = n^3$
* **Algoritmo B (cuadrático):** $T_B(n) = n^2$

> **Supuesto del modelo:** como el enunciado no entrega coeficientes ni costos adicionales, se comparan directamente $n^3$ y $n^2$. Los valores son unidades teóricas de operación, no segundos medidos.

### 4. Cálculo de las funciones

| $n$ | Algoritmo A | Algoritmo B |
|---:|:---|:---|
| **10** | $10^3 = 10 \times 10 \times 10 = 1.000$ | $10^2 = 100$ |
| **100** | $100^3 = 1.000.000$ | $100^2 = 10.000$ |
| **1.000** | $1.000^3 = 1.000.000.000$ | $1.000^2 = 1.000.000$ |

### 5. Tabla comparativa

| Tamaño $n$ | $T_A(n) = n^3$ | $T_B(n) = n^2$ | Big O de A | Big O de B |
|---:|---:|---:|:---:|:---:|
| 10 | 1.000 | 100 | $O(n^3)$ | $O(n^2)$ |
| 100 | 1.000.000 | 10.000 | $O(n^3)$ | $O(n^2)$ |
| 1.000 | 1.000.000.000 | 1.000.000 | $O(n^3)$ | $O(n^2)$ |

**Observaciones**

* A realiza más operaciones que B en los tres tamaños.
* La diferencia absoluta crece muy rápido: 900 operaciones con $n = 10$, 990.000 con $n = 100$ y 999.000.000 con $n = 1.000$.
* Cada vez que $n$ se multiplica por 10, A se multiplica por 1.000 y B solo por 100.

### 6. Determinación de la complejidad Big O

$$T_A(n) = n^3 \implies O(n^3) \qquad\qquad T_B(n) = n^2 \implies O(n^2)$$

La función cúbica crece más rápido que la cuadrática: $n^2 = O(n^3)$, pero $n^3 \neq O(n^2)$. Big O describe la **tendencia de crecimiento**, no el tiempo exacto en segundos.

### 7. Cálculo de la razón entre los algoritmos

$$\frac{T_A(n)}{T_B(n)} = \frac{n^3}{n^2} = n$$

| Tamaño $n$ | Sustitución | Razón |
|---:|:---|---:|
| 10 | $1.000 / 100$ | **10** |
| 100 | $1.000.000 / 10.000$ | **100** |
| 1.000 | $10^9 / 10^6$ | **1.000** |

**Interpretación:** la razón indica cuántas veces es mayor el costo de A frente al de B. La ventaja de B no es constante: **crece linealmente con $n$**.

### 8. Representación gráfica

En escala logarítmica en ambos ejes, $n^3$ y $n^2$ aparecen como rectas con pendientes 3 y 2. La separación vertical entre ellas es precisamente la razón $n$.

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

**Figura 2.** Crecimiento de $T_A(n)$ y $T_B(n)$ en escala logarítmica.

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

**Figura 3.** Razón $T_A(n)/T_B(n)$ para $n = 10$, $100$ y $1.000$.

### 9. Análisis e interpretación de los resultados

1. **¿Cuál realiza más operaciones?** El algoritmo A, para todo $n > 1$. Con $n = 1.000$ son 1.000 millones de operaciones frente a 1 millón del B.
2. **¿Cómo cambia la diferencia?** Pasa de 900 a 990.000 y luego a 999.000.000. Al multiplicar $n$ por 10, la diferencia se multiplica aproximadamente por 1.000.
3. **¿Qué significa la razón?** Que A necesita $n$ veces más operaciones que B. Mientras más grande el polígono, mayor es la ventaja de B.
4. **¿Por qué $n^2$ es más favorable que $n^3$?** Porque $n^3 = n \cdot n^2$: A hace el mismo trabajo que B multiplicado por un factor que crece con la entrada. Con entradas pequeñas pasa desapercibido, pero con entradas grandes es decisivo.
5. **¿Qué efecto tendría en un videojuego?** Un juego debe mantener unos 60 cuadros por segundo (≈ 16 ms por cuadro). Con miles de vértices, un algoritmo cúbico podría causar tirones (*lag*), tiempos de carga largos y mayor consumo de CPU, mientras que uno cuadrático escala de forma mucho más manejable.

### 10. Conclusión y elección del algoritmo

Conviene utilizar el **algoritmo B**. Su crecimiento $O(n^2)$ es más favorable que el $O(n^3)$ de A: la razón $T_A/T_B = n$ muestra que A es 10, 100 y 1.000 veces más costoso para $n = 10$, $100$ y $1.000$, y la brecha sigue ampliándose.

Sin embargo, la complejidad no demuestra por sí sola que una implementación sea geométricamente correcta. Antes de usar B en producción hay que comprobar que triangule bien los polígonos requeridos (incluidos los cóncavos). Además, este análisis usa coeficientes iguales a uno, así que conviene complementarlo con mediciones de tiempo reales.

---

## Anexo A: Códigos en Python

### A.1. Ejercicio 1: orientación y clasificación del giro

```python
def orientacion(A, B, C):
    """Producto cruz 2D de AB x AC. >0 antihorario, <0 horario, 0 colineal."""
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def clasificar_giro(det):
    if det > 0:
        return "Giro antihorario (izquierda)"
    elif det < 0:
        return "Giro horario (derecha)"
    return "Colineal (sin giro)"


casos = {
    "Caso 1": ((1, 2), (5, 3), (3, 7)),
    "Caso 2": ((2, 1), (6, 5), (8, 2)),
    "Caso 3": ((1, 1), (3, 3), (6, 6)),
    "Caso 4": ((0, 4), (5, 4), (3, 1)),
}

for nombre, (A, B, C) in casos.items():
    d = orientacion(A, B, C)
    print(f"{nombre}: det = {d:>3} -> {clasificar_giro(d)}")
```

Salida esperada:

```text
Caso 1: det =  18 -> Giro antihorario (izquierda)
Caso 2: det = -20 -> Giro horario (derecha)
Caso 3: det =   0 -> Colineal (sin giro)
Caso 4: det = -15 -> Giro horario (derecha)
```

### A.2. Ejercicio 2: función `interseccion`

```python
def signo(val):
    """Retorna +1, -1 o 0 según el signo de val."""
    return (val > 0) - (val < 0)


def orientacion(P, Q, R):
    return (Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])


def en_segmento(P, Q, R):
    """True si Q (colineal con PR) está dentro de la caja delimitadora de PR."""
    return (min(P[0], R[0]) <= Q[0] <= max(P[0], R[0]) and
            min(P[1], R[1]) <= Q[1] <= max(P[1], R[1]))


def interseccion(A, B, C, D):
    """True si los segmentos AB y CD se cruzan, se tocan o se superponen."""
    o1 = signo(orientacion(A, B, C))
    o2 = signo(orientacion(A, B, D))
    o3 = signo(orientacion(C, D, A))
    o4 = signo(orientacion(C, D, B))

    # Cruce propio
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    # Colinealidad o contacto
    if o1 == 0 and en_segmento(A, C, B): return True
    if o2 == 0 and en_segmento(A, D, B): return True
    if o3 == 0 and en_segmento(C, A, D): return True
    if o4 == 0 and en_segmento(C, B, D): return True

    return False


if __name__ == "__main__":
    print("Caso 1  (cruce propio)    :", interseccion((1,1), (7,5), (2,6), (8,1)))  # True
    print("Caso 2  (colineal disjunto):", interseccion((1,1), (3,3), (5,5), (7,7)))  # False
    print("Caso 3a (cruce vertical)  :", interseccion((0,2), (6,2), (3,0), (3,5)))  # True
    print("Caso 3b (contacto)        :", interseccion((0,2), (6,2), (6,2), (9,5)))  # True
    print("Caso 3c (superposición)   :", interseccion((0,2), (6,2), (4,2), (9,2)))  # True
```

### A.3. Ejercicio 3: todos los pares de tuberías

```python
def hay_cruces(tubos):
    """tubos: lista de segmentos ((x1, y1), (x2, y2)). Costo: n(n-1)/2 llamadas."""
    n = len(tubos)
    cruces = []
    for i in range(n):
        for j in range(i + 1, n):
            if interseccion(*tubos[i], *tubos[j]):
                cruces.append((i, j))
    return cruces
```

### A.4. Ejercicio 5: Algoritmo A, $O(n^3)$ (guardar como `algoritmo_a.py`)

Ear clipping ingenuo: en **cada** iteración se vuelven a verificar **todas** las orejas, es decir $n$ iteraciones × $n$ candidatos × $n$ comprobaciones.

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
    ip, isg = (i - 1) % m, (i + 1) % m          # vecinos (circular)
    a, b, c = poli[idx[ip]], poli[idx[i]], poli[idx[isg]]

    if cruz(a, b, c) <= 0:                       # vértice reflejo
        return False

    for j in range(m):                           # revisa los demás vértices
        if j in (ip, i, isg):
            continue
        contador[0] += 1
        if punto_en_triangulo(poli[idx[j]], a, b, c):
            return False
    return True


def triangular_A(poli):
    """poli: lista de (x, y) en sentido antihorario. Devuelve (triángulos, operaciones)."""
    idx = list(range(len(poli)))
    triangulos, contador = [], [0]

    while len(idx) > 3:
        # Se recalculan TODAS las orejas en cada iteración
        orejas = [i for i in range(len(idx)) if es_oreja(poli, idx, i, contador)]
        i = orejas[0]
        triangulos.append((idx[(i - 1) % len(idx)], idx[i], idx[(i + 1) % len(idx)]))
        idx.pop(i)                               # se "corta" la oreja

    triangulos.append(tuple(idx))
    return triangulos, contador[0]


def poligono_regular(n):
    return [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n))
            for k in range(n)]


if __name__ == "__main__":
    for n in (10, 50, 100):
        tris, ops = triangular_A(poligono_regular(n))
        print(f"n={n:4d}  triángulos={len(tris):4d}  operaciones={ops:10d}  n^3={n**3:10d}")
```

### A.5. Ejercicio 5: Algoritmo B, $O(n^2)$ (guardar como `algoritmo_b.py`)

Las orejas se calculan **una sola vez** y, al cortar una, solo se re-verifican sus dos vecinos.

```python
from algoritmo_a import cruz, punto_en_triangulo, poligono_regular


def triangular_B(poli):
    """poli: lista de (x, y) en sentido antihorario. Devuelve (triángulos, operaciones)."""
    n = len(poli)
    prev = [(i - 1) % n for i in range(n)]       # lista doblemente enlazada
    sig = [(i + 1) % n for i in range(n)]
    contador = [0]

    def es_oreja(i):
        a, b, c = poli[prev[i]], poli[i], poli[sig[i]]
        if cruz(a, b, c) <= 0:
            return False
        j = sig[sig[i]]
        while j != prev[i]:
            contador[0] += 1
            if punto_en_triangulo(poli[j], a, b, c):
                return False
            j = sig[j]
        return True

    oreja = [es_oreja(i) for i in range(n)]      # cálculo inicial: O(n^2)
    triangulos, restantes, i = [], n, 0

    while restantes > 3:
        while not oreja[i]:                      # busca una oreja ya marcada
            i = sig[i]
        p, s = prev[i], sig[i]
        triangulos.append((p, i, s))
        sig[p], prev[s] = s, p                   # se elimina el vértice i
        restantes -= 1
        oreja[p], oreja[s] = es_oreja(p), es_oreja(s)   # solo 2 re-verificaciones
        i = s

    triangulos.append((prev[i], i, sig[i]))
    return triangulos, contador[0]


if __name__ == "__main__":
    for n in (10, 100, 1000):
        tris, ops = triangular_B(poligono_regular(n))
        print(f"n={n:5d}  triángulos={len(tris):5d}  operaciones={ops:10d}  n^2={n**2:10d}")
```

> **Dependencia entre archivos:** `algoritmo_b.py` importa `cruz`, `punto_en_triangulo` y `poligono_regular` desde `algoritmo_a`. Ambos archivos deben estar en la misma carpeta.

### A.6. Cálculo teórico y razón

```python
def T_A(n): return n ** 3
def T_B(n): return n ** 2

print(f"{'n':>6} {'T_A(n)':>16} {'T_B(n)':>12} {'T_A/T_B':>10}")
for n in (10, 100, 1000):
    print(f"{n:>6} {T_A(n):>16,} {T_B(n):>12,} {T_A(n)/T_B(n):>10.0f}")
```

### A.7. Verificación experimental (conteo de operaciones)

Se ejecutaron ambos códigos sobre polígonos regulares contando las comprobaciones punto-en-triángulo. Los coeficientes reales no son 1 (A ≈ $n^3/3$ y B ≈ $2n^2$), pero confirman la forma del crecimiento: al multiplicar $n$ por 10, A crece cerca de 1.000 veces y B cerca de 100.

| $n$ | Operaciones A | Operaciones B | $n^3$ | $n^2$ |
|---:|---:|---:|---:|---:|
| 10 | 224 | 112 | 1.000 | 100 |
| 100 | 323.204 | 19.012 | 1.000.000 | 10.000 |
| 1.000 | no ejecutado\* | 1.990.012 | 1.000.000.000 | 1.000.000 |

\* Con $n = 1.000$, A requeriría cerca de $3{,}3 \times 10^8$ comprobaciones, demasiado lento para Python puro.

---

## Autores

- [@Jhoan Molina Gómez](https://github.com/Molina-university)
- [@Adrian Camilo Rincon](https://github.com/CamiloRincon17)