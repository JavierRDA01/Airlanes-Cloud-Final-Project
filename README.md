
# Proyecto: Cloud y Big Data


## 1. Descripción del Problema



El transporte aéreo es fundamental para la economía global, pero los retrasos y cancelaciones de vuelos representan un gran desafío tanto para las aerolíneas como para los pasajeros. Este proyecto analiza datos masivos de vuelos en los Estados Unidos (2018-2022) para identificar patrones, realizar consultas específicas y evaluar el rendimiento de un sistema de procesamiento en la nube.

### Objetivo Principal
Diseñar una aplicación Big Data basada en la nube que responda preguntas clave sobre retrasos y cancelaciones de vuelos, optimizando el procesamiento de consultas y analizando el rendimiento de la infraestructura utilizada.

---

## 2. Necesidad de Big Data y Cloud

### ¿Por qué Big Data?
- **Volumen:** El dataset contiene gran cantidad de registros de vuelos, con un tamaño superior a 1 GB.
- **Variedad:** Incluye datos como fechas, aerolíneas, tiempos de retraso, cancelaciones, entre otros.
- **Velocidad:** Es necesario analizar y generar resultados de manera eficiente para manejar consultas complejas.

### ¿Por qué Cloud?
- **Escalabilidad:** La nube permite aumentar recursos dinámicamente.
- **Eficiencia:** Plataformas en la nube optimizan almacenamiento y computación.
- **Colaboración:** Facilita el acceso al proyecto por parte de los miembros del equipo.

---

## 3. Descripción del Dataset

### Fuente
El dataset fue adquirido a través de Kaggle, una reconocida plataforma para análisis de datos.

Puedes consultar el [enlace del dataset](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2022.csv) para más información.


### Descripción
- Nombre: **Flight Status Prediction**.
- Periodo: 2018-2022 (se seleccionó 2022 para este análisis).
- Tamaño: **1.42 GB**.
- Formato: CSV.

### Estructura
El dataset está compuesto por 61 columnas que reflejan datos útiles sobre vuelos como:
- Fecha de vuelo.
- Aerolínea.
- Aeropuerto de origen y destino.
- Tiempos de retraso (llegada/salida).
- Cancelaciones.
- Número de vuelo.
---

## 4. Descripción de la Aplicación

### 4.1 Introducción
La aplicación es una tubería de procesamiento de datos basada en **Apache Spark** para analizar vuelos mediante consultas interactivas. Se utiliza un menú en línea de comandos para ejecutar análisis como cálculo de retrasos, filtros de vuelos y rutas únicas.

### 4.2 Modelo(s) de Programación

La aplicación utiliza los siguientes modelos y patrones de programación para realizar el análisis de datos:

#### Consultas y Patrones

**1. Número de vuelos por aerolínea.**
*Patrón: Numerical Summarization: Record Count.*
Permite contar la cantidad total de vuelos operados por cada aerolínea.

**2. Fecha del primer y último vuelo, y número de vuelos.**
*Patrón: Numerical Summarization: Min/Max/Count.*
Calcula la primera y última fecha de operación de cada aerolínea, además del total de vuelos.

**3. Promedio de retraso en llegada por día**
*Patrón: Numerical Summarization: Average.*
Calcula el retraso promedio de llegada agrupado por día de la semana.

**4. Índice invertido: palabras en nombres de ciudades a aerolíneas**
*Patrón: Inverted Index: Word to Documents.*
Relaciona las palabras encontradas en los nombres de ciudades con las aerolíneas que operan vuelos desde o hacia esas ciudades.

**5. Índice invertido: aeropuertos destino a aeropuertos origen.**
*Patrón: Inverted Index: Reverse Web-link Graph.*
Relaciona cada aeropuerto de destino con una lista de aeropuertos de origen que conectan con él.

**6. Filtrar vuelos con más de 30 minutos de retraso.**
*Patrón: Filtering: Basic Filtering.*
Selecciona únicamente los vuelos que tienen más de 30 minutos de retraso en la llegada.

**7. Rutas únicas (origen-destino)**
*Patrón: Filtering: Distinct.*
Extrae todas las combinaciones únicas de rutas de vuelo (aeropuerto origen y destino).

**8. Top K rutas con mayor retraso promedio**
*Patrón: Filtering: Top K.*
Devuelve las K rutas con mayor retraso promedio en llegada.

**Consultas Adicionales**

Las consultas 9, 10 y 11 no se asocian a un patrón específico, pero fueron añadidas al proyecto por su relevancia práctica y utilidad para los usuarios. Estas consultas permiten obtener información clave como retrasos promedio por aerolínea y franjas horarias, así como el porcentaje de vuelos cancelados.



### 4.3 Plataforma
La aplicación se ejecuta en **Google Cloud Platform (GCP)**, utilizando:
- **Google Cloud Dataproc:** Clústeres gestionados para Apache Spark.
- **Google Cloud Storage (GCS):** Repositorio para datos de entrada y resultados.

### 4.4 Infraestructura
- **Clúster:**
  - Nodo Maestro: `e2-standard-4` (4 vCPUs, 16 GB RAM).
  - Nodos de Trabajo: `e2-standard-4` (2 nodos, escalables).
- **Conjunto de Datos:**
  - Tamaño: 1.4 GB.
  - Ubicación: `gs://group18-441715-proyecto-final/data/Combined_Flights_2022.csv`.
- **Resultados:**
  - Ubicación: `gs://group18-441715-proyecto-final/resultados/`.

### 4.5 Características
- **Selección Dinámica:** Menú interactivo para ejecutar consultas.
- **Estructura Modular:** Funciones independientes para cada consulta.
- **Optimización de Recursos:** Caché y particionamiento para mejorar el rendimiento.

### 4.6 Flujo de Trabajo
1. **Especificación de Consultas:**
   El usuario selecciona una consulta (con parámetros adicionales como el valor de `K`).
2. **Especificación de Carga de Datos:**
   Importación desde Google Cloud Storage a un DataFrame de Spark. Tanto la dirección de entrada del dataset como la dirección de salida del output se deben especificar en el comando introducido
3. **Ejecución de Consultas:**
   Transformaciones y acciones en Spark.
4. **Generación de Resultados:**
   Los resultados se muestran en consola y se guardan en GCS.

---

## 5. Diseño del Software

### Estructura del Código
- **`main.py`:**
  - Punto de entrada.
  - Gestiona entrada del usuario y ejecución de consultas.
- **`queries.py`:**
  - Contiene funciones específicas para cada consulta.

### Entrada del Usuario
- Selección de consultas a través de la selección introducida por comando.
- Parámetros adicionales (`--k` para consultas Top-K).
- Selección de la dirección de entrada de datos.
- Selección de la dirección del output con los resultados de la consulta.

### Procesamiento de Datos
- Carga desde GCS a DataFrames de Spark.
- Transformaciones y acciones para ejecutar consultas.

### Salida
- Resultados en consola y CSV en GCS. En este repositorio estarán subidos ejemplos de la ejecución de todas las queries en el apartado results.
---

## 6. Uso de la Aplicación

### Ejecución del Programa
El programa se puede ejecutar con `spark-submit` en un clúster de Spark o en la propia instancia de la máquina.

### Ejemplo de Comandos

**1. Mediante un clúster de Spark y ejecutándose desde la Cloud Shell:**

 
* Consultas simples:

 ```bash
   gcloud dataproc jobs submit pyspark gs://[BUCKET]/code/main.py \
    --cluster=[CLUSTER_NAME] \
    --region=[REGION] \
    --py-files=gs://[BUCKET]/code/queries.py \
    -- \
    --choice=[CHOICE_NUMBER] \
    --input-path=gs://[BUCKET]/data/[DATASET_NAME] \
    --output-path=gs://[BUCKET]/results/

   ```
Ejemplo del comando:
   ```bash
   gcloud dataproc jobs submit pyspark gs://group18-441715-proyecto-final/code/main.py \
    --cluster=cluster-small \
    --region=europe-southwest1 \
    --py-files=gs://group18-441715-proyecto-final/code/queries.py \
    -- \
    --choice=4 \
    --input-path=gs://group18-441715-proyecto-final/data/Combined_Flights_2022.csv \
    --output-path=gs://group18-441715-proyecto-final/results/
   ```

* Consultas con parámetros:

 ```bash
    gcloud dataproc jobs submit pyspark gs://[BUCKET]/code/main.py \
    --cluster=[CLUSTER_NAME] \
    --region=[REGION] \
    --py-files=gs://[BUCKET]/code/queries.py \
    -- \
    --choice=8 \
    --k=[K_VALUE] \
    --input-path=gs://[BUCKET]/data/[DATASET_NAME] \
    --output-path=gs://[BUCKET]/results/
   ```
Ejemplo del comando:
   ```bash
   gcloud dataproc jobs submit pyspark gs://group18-441715-proyecto-final/code/main.py \
    --cluster=cluster-small \
    --region=europe-southwest1 \
    --py-files=gs://group18-441715-proyecto-final/code/queries.py \
    -- \
    --choice=8 \
    --k=10 \
    --input-path=gs://group18-441715-proyecto-final/data/Combined_Flights_2022.csv \
    --output-path=gs://group18-441715-proyecto-final/results/

   ```

**2. Ejecución del trabajo localmente**
   
   También se puede ejecutar el trabajo de forma local. Sin embargo, esta opción es menos recomendable ya que en general es menos eficaz que ejecutarlo desde GCP. Además es necesario instalar dependencias y configuraciones para archivos binarios por lo que no recomendamos esta opción.

   El ejemplo de comando son los siguientes:
   *  Para la conusulta 8:
   ```bash
   spark-submit main.py --choice=8 --k=10 --input-path=data/Combined_Flights_2022.csv --output-path=results/consulta8/

   ```
   *  Para el resto de consultas:
   ```bash
   spark-submit main.py --choice=3 --input-path=data/Combined_Flights_2022.csv --output-path=results/consulta3/

   ```

### Lista de Consultas Disponibles
    1. Número de vuelos por aerolínea.
    2. Fecha del primer y último vuelo, y número de vuelos.
    3. Promedio de retraso en llegada por día.
    4. Índice invertido: palabras en nombres de ciudades a aerolíneas.
    5. Índice invertido: aeropuertos destino a aeropuertos origen.
    6. Filtrar vuelos con más de 30 minutos de retraso.
    7. Rutas únicas (origen-destino).
    8. Top K rutas con mayor retraso promedio.
    9. Promedio de retraso por aerolínea.
    10. Porcentaje de vuelos cancelados por aerolínea.
    11. Retraso promedio por franja horaria.

   La única que necesita parámetros adicionales es la consulta 8.

---

## 7. Evaluación del Rendimiento
Se realizaron pruebas con diferentes configuraciones de clúster en Google Cloud Dataproc para evaluar el rendimiento de la aplicación en términos de tiempo de respuesta y escalabilidad. El objetivo era medir cómo varía el tiempo de ejecución al incrementar el número de nodos en el clúster.

**Configuración de los Clústeres:**

Para estas pruebas, se utilizaron clústeres con las siguientes configuraciones:

| Clúster | Nodos de Trabajo | Tipo de Máquina | Núcleos Totales |Memoria Total (RAM) |
|--------------|--------------|--------------|--------------|--------------|
| Cluster-2-Nodes     | 2 | e2-standard-4 | 8 vCPUs      | 32 GB     |
| luster-3-Nodes     | 3   | e2-standard-4  | 12 vCPUs      | 48 GB     |
| Cluster-4-Nodes     | 4 | e2-standard-4  | 16 vCPUs      | 64 GB      |


**Resultados del Tiempo de Ejecución:**

Se probó la consulta 4 (Índice Invertido: Palabras en nombres de ciudades a aerolíneas) en los tres clústeres. Los tiempos de ejecución fueron los siguientes:

| Clúster         | Nodos de Trabajo | Tiempo de Ejecución |
|------------------|------------------|----------------------|
| Cluster-2-Nodes  | 2               | 1.50 minutos         |
| Cluster-3-Nodes  | 3               | 1.51 minutos         |
| Cluster-4-Nodes  | 4               | 1.37 minutos         |

**Análisis del Rendimiento**
1. Observación del Tiempo de Respuesta
   
   Aunque se esperaba que el tiempo de ejecución disminuyera linealmente al aumentar el número de nodos, los resultados muestran que entre 2 y 3 nodos no hubo mejoras significativas en el tiempo de respuesta.
Con 4 nodos, hubo una mejora leve en el tiempo de ejecución (1.37 minutos frente a 1.50 minutos en el clúster de 2 nodos).

2. Identificación de Cuellos de Botella
   
   El rendimiento no escaló de manera lineal debido a posibles factores:

   Sobrecarga de comunicación: Al aumentar los nodos, el tiempo necesario para la comunicación entre nodos puede contrarrestar las ventajas de procesamiento paralelo.
   
   El tamaño del dataset era de 1.4 GB, el dataset es relativamente pequeño para aprovechar completamente la distribución en clústeres más grandes.
   
   Con base en estos resultados, se sugiere utilizar un clúster con 2 nodos de trabajo para datasets similares (hasta 1.5 GB), ya que incrementos en los nodos no ofrecen mejoras significativas en el tiempo de ejecución para este tamaño de datos. Para datasets más grandes, se recomienda repetir las pruebas y observar si la escalabilidad mejora con clústeres más grandes.
---

## 8. Características Avanzadas
- **Evaluación Diferida:** Cálculos ejecutados solo cuando son necesarios.
- **Caché y Particionamiento:** Reducción de latencia.
- **Consultas Top K:** Identificación de patrones clave (e.g., rutas con mayores retrasos).
- **Uso de google colab**: 

---


## 9. Conclusiones

Este proyecto ha demostrado la importancia y el potencial del análisis de datos a gran escala utilizando tecnologías en la nube. Gracias a la combinación de **Google Cloud Platform** y **Apache Spark**, hemos logrado crear una aplicación eficiente, escalable y capaz de responder preguntas clave sobre retrasos y cancelaciones en vuelos. 

---

#### **Metas Alcanzadas**
- **Procesamiento de Big Data:** Logramos analizar un dataset de 1.4 GB, manejando consultas complejas y generando resultados en tiempos razonables.
- **Despliegue en la Nube:** Diseñamos e implementamos una infraestructura basada en Google Cloud Dataproc para ejecutar nuestro pipeline de procesamiento de datos.
- **Escalabilidad:** Probamos distintas configuraciones de clúster, evaluando su rendimiento para identificar la más adecuada.
- **Consultas Prácticas:** Desarrollamos consultas útiles para usuarios, como identificar las rutas con mayores retrasos o la aerolínea más confiable, brindando información valiosa para la toma de decisiones.

---

#### **Lecciones Aprendidas**
- **Manejo de Datos a Gran Escala:** Aprendimos a procesar datasets masivos, optimizando recursos y minimizando tiempos de ejecución en un entorno distribuido.
- **Valor de los Datos Masivos:** Este proyecto mostró cómo el análisis masivo de datos puede generar ventajas prácticas, como elegir la mejor aerolínea o el horario más conveniente para nuestras próximas vacaciones.
- **Importancia de la Validación:** Validar las consultas en un entorno aislado antes de su despliegue completo ahorró tiempo y recursos, garantizando su funcionalidad en un clúster.

---

#### **Sugerencias de Mejora**
- **Particionamiento de Datos:** Implementar un esquema de particionamiento optimizado para mejorar el tiempo de ejecución en consultas más grandes.
- **Visualización:** Integrar herramientas de visualización para presentar resultados en gráficos interactivos que faciliten la interpretación de los datos.
- **Automatización:** Diseñar un pipeline automatizado para ejecutar y guardar consultas de forma programada, optimizando procesos repetitivos.

---

#### **Futuro del Proyecto**
- **Análisis Predictivo:** Incorporar modelos de machine learning para predecir retrasos en vuelos basados en patrones históricos.
- **Expansión del Dataset:** Realizar análisis con datasets más grandes o con datos de vuelos internacionales.
- **Dashboard Interactivo:** Crear una interfaz web que permita a los usuarios ejecutar consultas y visualizar resultados en tiempo real.

---

#### **Reflexión Final**
Este proyecto ha sido una gran oportunidad para explorar cómo los datos masivos pueden transformar nuestra comprensión del mundo y mejorar la toma de decisiones. Desde un punto de vista práctico, herramientas como Spark y GCP permiten mejorar y optimizar procesos de nuestro día a día. Sinceramente, nos ha parecido de las asignaturas más útiles y estamos seguros de que utilizaremos lo aprendido en esta asignatura para seguir optimizando nuestro trabajjo o buscar nuevas alternativas con las que trabajar y que nos brinden nuevos enfoques y soluciones a nuestros problemas.

---

## 10. Referencias
- [Kaggle: Dataset "Flight Status Prediction"](https://www.kaggle.com/)
- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [Google Cloud Dataproc](https://cloud.google.com/dataproc/)
- [Google Colab](https://colab.research.google.com/): Entorno utilizado para pruebas iniciales y validación de queries.

## Authors

- Javier Ramírez de Andrés
- Álvaro González-Barros Medina 

