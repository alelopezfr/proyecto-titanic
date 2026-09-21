 Análisis Exploratorio de Datos del Titanic (EDA)

 Descripción del Proyecto
Este proyecto aborda un Análisis Exploratorio de Datos (EDA) sobre la información de los pasajeros del naufragio del RMS Titanic. La investigación aplica técnicas estadísticas y visualización de datos en Python para comprender la estructura del conjunto de datos, realizar procesos de limpieza de datos, crear nuevas variables relevantes y descubrir los patrones socioeconómicos y demográficos asociados a las probabilidades de supervivencia.

---

 Dataset

Nombre del dataset: Titanic - Machine Learning from Disaster (`train.csv`)
Fuente: [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)
Descripción breve: El conjunto de datos consta de 891 registros que representan a un grupo representativo de pasajeros a bordo del barco. Contiene 12 variables que abarcan información demográfica (edad, género), económica (clase de billete, tarifa pagada, puerto de embarque) y familiar (número de cónyuges, hermanos, padres e hijos a bordo), además de la variable objetivo de supervivencia.

---

Objetivo
El objetivo general es analizar qué factores influyeron de manera determinante en la tasa de supervivencia de los pasajeros durante el naufragio.

 Objetivos específicos:
1. Evaluar el impacto de las variables demográficas primarias (género y edad) en la prioridad de rescate.
2. Analizar la correlación entre la clase socioeconómica de los pasajeros (`Pclass`) y la tasa de supervivencia.
3. Determinar si viajar solo o acompañado afectó las posibilidades de supervivencia.
4. Identificar la distribución de las tarifas pagadas en relación con el estado final de supervivencia.

---

Requisitos
Para la correcta ejecución del proyecto se requiere:
Python versión 3.10 o superior.
 Dependencias y librerías listadas en el archivo `requirements.txt`:
   `pandas`: Manipulación y procesamiento de datos tabulares.
   `matplotlib`: Creación de figuras y visualizaciones base.
   `seaborn`: Generación de gráficos estadísticos de alto nivel.

---
 Instalación

Siguir minuciosamente esta serie de pasos en la consola de comandos para clonar el proyecto e instalar el entorno de trabajo:

 Clonar el repositorio:
   ```cmd
   git clone URL_DEL_REPOSITORIO

Entrar al proyecto:

DOS
cd proyecto-titanic
Crear el entorno virtual:

DOS
python -m venv .venv
Activarlo e instalar dependencias:

En Windows (Command Prompt / CMD):

DOS
.venv\Scripts\activate
pip install -r requirements.txt
Ejecución
Una vez activo el entorno virtual con sus dependencias instaladas, ejecuta el script principal de análisis ejecutando el siguiente comando en la raíz del proyecto:

DOS
python src/analysis.py
El script imprimirá en pantalla las estadísticas clave del análisis y generará/actualizará automáticamente los gráficos en la carpeta outputs/.

Análisis Realizados

Diagnóstico inicial y tratamiento de valores nulos:

Se identificaron valores faltantes en las columnas Age, Cabin y Embarked.

La columna Cabin fue descartada debido a un porcentaje crítico de valores ausentes (>75%).

Los valores nulos de Age se imputaron utilizando la mediana agrupada por clase socioeconómica (Pclass).

Los registros faltantes de Embarked se rellenaron utilizando la moda.

Ingeniería de Variables (Feature Engineering):

FamilySize: Suma de SibSp + Parch + 1 para calcular la dimensión total del grupo familiar a bordo.

IsAlone: Variable binaria que indica si el pasajero viajaba sin compañía (1) o acompañado (0).

AgeGroup: Categorización discreta de la edad en rangos: Niño (<12), Joven (<18), Adulto (<60) y Adulto mayor (>=60).

Resultados y Conclusiones

Sesgo de Género y Clase Social: Las mujeres pertenecientes a la primera y segunda clase mostraron las tasas de supervivencia más altas (superiores al 90%), lo cual evidencia un cumplimiento estricto del protocolo de evacuación "mujeres y niños primero", sumado al acceso preferencial a los botes salvavidas asignado a las clases altas.

Impacto de la Edad: El grupo categorizado como Niños presentó la mayor probabilidad de rescate entre todos los rangos de edad, mientras que la tasa disminuyó significativamente para adultos y adultos mayores.

Relación Económica: Los pasajeros sobrevivientes pagaron en promedio tarifas considerablemente más elevadas en comparación con aquellos que no sobrevivieron, respaldando la hipótesis de que la ubicación de los camarotes y el estatus socioeconómico jugaron un papel crucial durante la emergencia.


Estructura del Proyecto

proyecto-titanic/
├── data/
│   └── train.csv
├── outputs/
│   ├── supervivencia_clase_genero.png
│   ├── supervivencia_grupo_edad.png
│   └── tarifa_vs_supervivencia.png
├── src/
│   └── analysis.py
├── .gitignore
├── README.md
└── requirements.txt