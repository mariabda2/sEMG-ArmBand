# sEMG-ArmBand

> Análisis de señales EMG de superficie (sEMG) usando las bases de datos NinaPro para clasificación de gestos en sujetos intactos y amputados.

---

## Descripción

Este repositorio implementa un pipeline de procesamiento y análisis de señales **sEMG (surface Electromyography)** orientado al estudio de gestos de la mano. Utiliza las bases de datos **NinaPro (DB1, DB2, DB3, DB4, DB5, DB7)** e integra datos de **107 sujetos intactos** y **13 sujetos amputados**, extrayendo características en ventanas de 200 ms para análisis exploratorio y preparación de datasets para clasificación.

El proyecto aplica dos estrategias de extracción de características:

- **Hilbert envelope**: captura información de amplitud/envolvente de la señal.
- **NoEnvelope (raw window)**: captura morfología y transiciones de la señal sin procesamiento previo.

Ambas se combinan en archivos **mixed** que asignan cada característica a la fuente más apropiada.

---

## Estructura del repositorio

```
sEMG-ArmBand/
├── data/
│   ├── master/          # Tablas consolidadas de sujetos y señales (intactos y amputados)
│   ├── metadata/        # Metadatos por sujeto para cada base de datos (DB1–DB7)
│   └── processed/       # Archivos CSV de características mixtas por DB (200 ms)
├── figures/             # Figuras generadas (boxplots, comparativas CV)
├── notebooks/
│   ├── 01_creates_db_merge.ipynb         # Merge de DBs en datasets maestros
│   ├── 02_creates_dataset_intact.ipynb   # Construcción del dataset de sujetos intactos
│   ├── 03_intact_database_analysis.ipynb # Análisis exploratorio (EDA) del dataset intacto
│   ├── transformation.ipynb              # Transformaciones de señal
│   └── Borradores/                       # Notebooks de desarrollo y exploración
├── requirements.txt
├── AGENTS.md
└── README.md
```

---

## Pipeline de notebooks

Ejecutar en el siguiente orden:

| # | Notebook | Descripción |
|---|----------|-------------|
| 1 | `01_creates_db_merge.ipynb` | Carga y une los CSV procesados de DB1–DB7 en tablas maestras de sujetos intactos y amputados. Filtra canales 1–8 y estímulos de interés. |
| 2 | `02_creates_dataset_intact.ipynb` | Construye el dataset final de sujetos no amputados (NinaProDB1, DB2, DB4, DB5) con las 8 features × 8 canales seleccionadas. |
| 3 | `03_intact_database_analysis.ipynb` | Exploración del comportamiento de las ventanas vs repeticiones. |

---

## Datos

### Bases de datos NinaPro utilizadas

| Base de datos | Grupo | Canales usados |
|---------------|-------|---------------|
| DB1 | Intactos | 1–8 |
| DB2 | Intactos | 1–8 |
| DB3 | Amputados | 1–8 |
| DB4 | Intactos | 1–8 (de 12) |
| DB5 | Intactos | 1–8 |
| DB7 | Amputados | 1–8 |

### Estímulos seleccionados

`22, 25, 27, 30, 31, 37, 40`

### Características extraídas (por canal)

**Desde NoEnvelope:** `MAVS`, `MNF`, `SSC`, `TD`, `WL`, `ZC`, `mDWT`

**Desde Hilbert:** `CoV`, `Energy`, `IAV`, `Kurtosis`, `MAV`, `Max`, `Mean`, `Median`, `Min`, `RMS`, `Range`, `Skewness`, `VAR`

### Formato de columnas en archivos processed

```
<Channel N>_<FeatureSuffix>   →  Ejemplo: Channel 4_RMS
```

Columnas de metadatos: `subject`, `stimulus`, `window_index`, `window_size_samples`, `window_size_ms`

**Total columnas por archivo (DB1, DB2, DB3, DB5, DB7):** 213 (208 señal + 5 metadatos)
**DB4:** 317 (312 señal + 5 metadatos, 12 canales originales)

---

## Instalación y uso

### Requisitos

- Python 3.14
- Entorno virtual recomendado

### Configuración

```bash
# Clonar el repositorio
git clone https://github.com/mariabda2/sEMG-ArmBand.git
cd sEMG-ArmBand

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar notebooks

```bash
jupyter lab notebooks/
```

Abre `notebooks/` en orden: `01_` → `02_` → `03_`.

---

## Dependencias

| Paquete | Uso |
|---------|-----|
| `numpy` | Computación numérica |
| `pandas` | Manipulación de datos tabulares |
| `scipy` | Computación científica y procesamiento de señales |
| `matplotlib` | Visualización |
| `seaborn` | Visualización estadística |
| `scikit-learn` | Machine learning y clasificación |
| `jupyter` / `ipykernel` | Entorno de notebooks |

---

## Notas importantes

- Los archivos de datos en `data/` son CSVs de gran tamaño; **no editar directamente**.
- Los datasets maestros (`intact_signals.csv`, `amputated_signals.csv`, etc.) son generados por el notebook `01_` y **no están commiteados** en el repositorio (ver `.gitignore`).
- El proyecto **no tiene estructura de paquete Python** — todo se ejecuta desde notebooks.
- No hay tests, linting ni CI configurado.
- Para DB4, solo se usan los canales 1–8 (el sensor tiene 12) para mantener consistencia entre bases de datos.

---

## Licencia

Ver archivo [LICENSE](LICENSE).
