import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración de rutas de archivos
DATA_PATH = os.path.join("data", "train.csv")
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 2. Carga y exploración inicial
print("=== EXPLORACIÓN INICIAL DE DATOS ===")
df = pd.read_csv(DATA_PATH)

print(f"Número de pasajeros (filas): {df.shape[0]}")
print(f"Número de variables (columnas): {df.shape[1]}")
print("\nTipos de datos y estructura:")
print(df.info())

print("\nValores faltantes por columna:")
print(df.isnull().sum())

print(f"\nRegistros duplicados: {df.duplicated().sum()}")

# 3. Limpieza y Tratamiento de Valores Faltantes
df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'], inplace=True)

# 4. Creación de Nuevas Variables
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

def categorizar_edad(edad):
    if edad < 12:
        return 'Niño'
    elif edad < 18:
        return 'Joven'
    elif edad < 60:
        return 'Adulto'
    else:
        return 'Adulto mayor'

df['AgeGroup'] = df['Age'].apply(categorizar_edad)
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# 5. Análisis de Preguntas Clave
print("\n=== RESULTADOS DEL ANÁLISIS ===")
print(f"1. Porcentaje general de supervivencia: {df['Survived'].mean() * 100:.2f}%")

print("\n2. Tasa de supervivencia por género:")
print(df.groupby('Sex')['Survived'].mean() * 100)

print("\n3. Tasa de supervivencia por clase (Pclass):")
print(df.groupby('Pclass')['Survived'].mean() * 100)

print("\n4. Tasa de supervivencia según compañía (Solo vs Acompañado):")
print(df.groupby('IsAlone')['Survived'].mean() * 100)

# 6. Generación y Guardado de Visualizaciones
sns.set_theme(style="whitegrid")

# Gráfico 1
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Pclass', y='Survived', hue='Sex', ci=None, palette='Set2')
plt.title('Tasa de Supervivencia por Clase y Género')
plt.xlabel('Clase del Pasajero')
plt.ylabel('Tasa de Supervivencia')
plt.savefig(os.path.join(OUTPUT_DIR, 'supervivencia_clase_genero.png'), bbox_inches='tight')
plt.close()

# Gráfico 2
plt.figure(figsize=(8, 5))
order_edad = ['Niño', 'Joven', 'Adulto', 'Adulto mayor']
sns.barplot(data=df, x='AgeGroup', y='Survived', order=order_edad, palette='mako', ci=None)
plt.title('Tasa de Supervivencia por Grupo de Edad')
plt.xlabel('Grupo de Edad')
plt.ylabel('Tasa de Supervivencia')
plt.savefig(os.path.join(OUTPUT_DIR, 'supervivencia_grupo_edad.png'), bbox_inches='tight')
plt.close()

# Gráfico 3
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Survived', y='Fare', palette='Set1', showfliers=False)
plt.title('Distribución de Tarifas Pagadas según Supervivencia')
plt.xticks([0, 1], ['No Sobrevivió', 'Sobrevivió'])
plt.xlabel('Estado de Supervivencia')
plt.ylabel('Tarifa Pagada')
plt.savefig(os.path.join(OUTPUT_DIR, 'tarifa_vs_supervivencia.png'), bbox_inches='tight')
plt.close()

print(f"\nAnálisis finalizado con éxito. Gráficos guardados en la carpeta '{OUTPUT_DIR}'.")