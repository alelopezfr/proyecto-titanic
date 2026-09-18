\# Análisis Exploratorio del Dataset Titanic



Este proyecto realiza un análisis exploratorio de datos (EDA) sobre el dataset del Titanic para identificar factores clave que influyeron en la supervivencia de los pasajeros.



\## Estructura del Proyecto



```text

proyecto-titanic/

├── data/

│   └── train.csv

├── outputs/

│   ├── supervivencia\_clase\_genero.png

│   ├── supervivencia\_grupo\_edad.png

│   └── tarifa\_vs\_supervivencia.png

├── src/

│   └── analysis.py

├── .gitignore

├── README.md

└── requirements.txt

```



\## Requisitos e Instalación



1\. Crear y activar entorno virtual:

&#x20;  ```cmd

&#x20;  python -m venv .venv

&#x20;  .venv\\Scripts\\activate

&#x20;  ```

2\. Instalar dependencias:

&#x20;  ```cmd

&#x20;  pip install -r requirements.txt

&#x20;  ```



\## Ejecución del Análisis



Para ejecutar el script principal y generar las visualizaciones:



```cmd

python src/analysis.py

```



\## Principales Hallazgos



1\. \*\*Género y Clase Social\*\*: Las mujeres de primera y segunda clase tuvieron las tasas de supervivencia más altas.

2\. \*\*Edad\*\*: Los niños tuvieron una prioridad notable en el rescate respecto a otros grupos de edad.

3\. \*\*Tarifa\*\*: Los pasajeros que sobrevivieron pagaron en promedio tarifas más altas, reflejando su ubicación en mejores clases.

