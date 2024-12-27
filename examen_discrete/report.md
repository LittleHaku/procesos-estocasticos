# Parte B: Análisis del Paseo por Popularidad en Grafos Barabasi-Albert

En esta segunda parte del examen, se analiza el comportamiento de un paseo por popularidad en un grafo generado bajo el modelo Barabasi-Albert. Este modelo es conocido por generar grafos con propiedades de escala libre, donde unos pocos nodos concentran la mayoría de las conexiones (alta popularidad), mientras que la mayoría de los nodos tienen un grado mucho menor. Esta estructura es común en redes sociales, biológicas y tecnológicas [1].

El objetivo inicial de este estudio es analizar la fracción del grafo visitada en función del tiempo para diversos valores del parámetro $\alpha$. Este parámetro modula la probabilidad de transición en el paseo, definida matemáticamente como:

$$
p(j|i) =
\begin{cases}
\displaystyle\frac{d_j^\alpha}{\sum\limits_{k:(i,k)\in E} d_k^\alpha} & \text{si} \ (i,j) \in E \\\\
0 & \text{si} \ (i,j) \notin E
\end{cases}
$$

donde $d_i$ es el grado del nodo $i$, $n$ es el número total de nodos, y $\alpha$ es un parámetro que determina el peso relativo de los nodos más populares frente a los menos conectados. Valores altos de $\alpha$ favorecen transiciones hacia nodos de mayor grado, es decir, más populares, mientras que valores bajos o negativos promueven la exploración de nodos menos conectados, reduciendo la preferencia hacia los nodos con muchas conexiones.

## Procedimiento

1. **Estudio inicial de fracción visitada en función del tiempo**:
   Para comenzar, se simularon paseos en un grafo de tipo Barabasi-Albert con los siguientes parámetros iniciales: $n = 1000$ nodos, $m = 10$ enlaces por nodo añadido, y un límite temporal de $t_{\text{max}} = 5000$. Los valores de $\alpha$ considerados inicialmente fueron $\{-2, -1, -0.5, 0, 0.5, 1, 2, 5\}$. Se realizaron $n_{\text{tests}} = 1000$ pruebas para cada valor de $\alpha$, calculando la fracción promedio de nodos visitados en función del tiempo. Este enfoque permitió identificar las tendencias generales en el comportamiento del paseo para diferentes configuraciones.

2. **Ampliación del rango de valores de $\alpha$**:
   Basándose en los resultados iniciales, se amplió el rango de estudio para incluir valores intermedios ($\alpha = -0.25$, $-0.75$, $-1.5$) y extremos ($\alpha = -4$). Esto permitió refinar el análisis y explorar cómo valores menos comunes impactan la eficiencia del paseo.

3. **Cálculo del tiempo promedio necesario para alcanzar el 50% del grafo**:
   Como medida complementaria, se evaluó el tiempo promedio necesario para visitar el 50% del grafo. Esta métrica proporciona una perspectiva adicional sobre la eficiencia del paseo, más allá del análisis temporal de la fracción visitada.

## Resultados

- **Tendencias Generales**:

  - Para valores altos de $\alpha$ ($\alpha > 1$), el paseo tiende a concentrarse en unos pocos nodos de alto grado. Esto limita significativamente la exploración del grafo, resultando en tiempos elevados para alcanzar el 50% de los nodos. Este comportamiento refleja una explotación excesiva de los nodos más populares.
  - Valores bajos de $\alpha$ ($\alpha < -1$) también presentan un comportamiento subóptimo. En estos casos, la probabilidad asignada a cada nodo tiende a ser uniforme y baja, lo que ralentiza el paseo al no priorizar ningún nodo en particular.
  - Los mejores resultados se observaron para valores intermedios de $\alpha$ (entre $-1$ y $-0.5$). Específicamente, $\alpha = -0.75$ obtuvo el menor tiempo promedio con 767.193 visitas, lo que indica un balance óptimo entre exploración y explotación.

- **Observaciones Detalladas**:
  En el análisis inicial, se observó que para valores extremos como $\alpha = -4$, el rendimiento disminuye debido a que la probabilidad de transición se concentra en nodos de bajo grado, reduciendo la eficiencia del paseo. Sin embargo, valores intermedios como $\alpha = -0.25$ y $-0.75$ lograron un balance óptimo, maximizando la exploración del grafo en menor tiempo.

## Conclusión

El parámetro $\alpha$ desempeña un papel crucial en la dinámica del paseo por popularidad. Este estudio demuestra que valores cercanos a $\alpha = -0.75$ son ideales para maximizar la eficiencia en grafos de tipo Barabasi-Albert, logrando un equilibrio entre explorar nodos populares y menos conectados. Este resultado es particularmente relevante en aplicaciones como el muestreo eficiente de redes sociales, análisis de redes biológicas y diseño de algoritmos para sistemas distribuidos.

Además, el análisis sugiere que valores extremos, tanto altos como bajos, tienden a ser ineficientes debido a la falta de balance entre exploración y explotación. En futuros estudios, sería valioso explorar cómo otras propiedades del grafo, como su tamaño o distribución de grado, afectan el rendimiento del paseo. También podría investigarse cómo variar el umbral de fracción visitada (por ejemplo, 25% o 75%) impacta los resultados obtenidos.

## Referencias

[1]: https://es.wikipedia.org/wiki/Modelo_Barab%C3%A1si%E2%80%93Albert

1. [Barabási–Albert model](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model)
