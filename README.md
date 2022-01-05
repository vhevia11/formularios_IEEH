# Formularios_IEEH
Script para generar automatización de registro de formularios IEEH

Corresponde a un conjunto de script en python que permiten la automatización del registro de formularios IEEH. La manera en que funciona es, tomando la exportación en excel desde la base de datos Access (en formato .xlsx), para luego leer, pre-procesar la tabla y registrar dentro del pdf del formulario a cada uno de los egresos generados.

## Instalación de scripts

Es necesario contar con instalación de python 3.7 y realizar los siguientes pasos para el correcto funcionamiento.

**Extracción de repositorio**

```
git clone https://github.com/vhevia11/formularios_IEEH.git
```

**Requerimientos**

**Pandas**
```
pip install pandas
```

**PyPDF2**

```
pip install pypdf2
```

**reportlab**

```
pip install reportlab
```
