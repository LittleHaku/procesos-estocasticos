# Parte B: Análisis del Paseo por Popularidad en Grafos Barabasi-Albert

En esta segunda parte del examen, se analiza el comportamiento de un paseo por popularidad en un grafo generado bajo el modelo Barabasi-Albert. Este modelo es conocido por generar grafos con propiedades de escala libre, donde unos pocos nodos concentran la mayoría de las conexiones (alta popularidad), mientras que la mayoría tienen un grado mucho menor.

El objetivo es estudiar la fracción del grafo visitada en función del tiempo para diversos valores del parámetro $\alpha$. Este parámetro modula la probabilidad de transición en el paseo, definida matemáticamente como:

\[
p(j|i) =
\begin{cases}
\displaystyle\frac{d_j^\alpha}{\sum\limits_{k:(i,k)\in E} d_k^\alpha} & \text{si} \ (i,j) \in E \\
0 & \text{si} \ (i,j) \notin E
\end{cases}
\]

donde $d_i$ es el grado del nodo $i$, $n$ es el número total de nodos, y $\alpha$ determina el peso relativo de los nodos más populares frente a los menos conectados. Valores altos de $\alpha$ favorecen transiciones hacia nodos de mayor grado, es decir, más populares, mientras que valores bajos permiten explorar nodos menos conectados.

## Procedimiento

1. **Selección de Valores de $\alpha$**:
   Inicialmente, se estudiaron los valores sugeridos en el enunciado: $\alpha \in \{-2, -1, -0.5, 0, 1, 2, 5\}$. Posteriormente, se realizó un análisis más detallado para identificar tendencias, incluyendo valores intermedios ($\alpha = -0.25$, $-0.75$, $-1.5$) y extremos ($\alpha = -4$).

2. **Métrica de Evaluación**:
   Se evaluó el tiempo necesario para visitar el 50% del grafo en función de $\alpha$. Esta métrica permite cuantificar la eficiencia del paseo al equilibrar exploración y explotación.

3. **Análisis Gráfico**:
   Se generaron gráficas que muestran la fracción del grafo visitada a lo largo del tiempo, así como el tiempo promedio necesario para alcanzar el 50% de los nodos.

## Resultados

- **Tendencias Generales**:

  - Para valores altos de $\alpha$ ($\alpha > 1$), el paseo se concentra en unos pocos nodos de alto grado, lo que limita la exploración del grafo. Este comportamiento se traduce en tiempos elevados para alcanzar el 50% del grafo.
  - Valores bajos de $\alpha$ ($\alpha < -1$) también presentan un comportamiento subóptimo. En estos casos, la probabilidad asignada a todos los nodos tiende a ser uniforme y baja, lo que ralentiza el paseo.
  - Los mejores resultados se observaron para valores intermedios de $\alpha$ (entre $-1$ y $-0.5$). Específicamente, $\alpha = -0.75$ obtuvo el menor tiempo promedio con 767.193 visitas.

- **Observaciones Detalladas**:
  Al extender el rango de $\alpha$ hacia valores extremos ($\alpha = -4$), no se logró mejorar los resultados debido a que la probabilidad de transición se concentra en nodos de bajo grado, reduciendo la eficiencia del paseo. Por otro lado, los valores intermedios como $\alpha = -0.25$ y $-0.75$ mostraron un balance óptimo entre exploración y explotación del grafo.

## Conclusión

El parámetro $\alpha$ juega un rol fundamental en la dinámica del paseo por popularidad. Este estudio sugiere que valores cercanos a $\alpha = -0.75$ son ideales para maximizar la eficiencia del paseo en grafos de tipo Barabasi-Albert, logrando un equilibrio entre explorar nodos populares y menos conectados. Este resultado podría ser relevante en aplicaciones que requieren muestreos eficientes de redes escala libre, como el análisis de redes sociales o bioinformáticas.

Para trabajos futuros, se podría explorar cómo el tamaño del grafo o el método de inicialización afectan estos resultados, así como analizar la fracción visitada para umbrales diferentes al 50%.
