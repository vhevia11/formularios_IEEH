import pandas as pd
from clean import data_cleaner
from register import complete_form

#Definir nombre del archivo a leer, es necesario guardar en la misma carpeta del script
archivo = 'IEEH-F.xlsx'
#Leer archivo excel 
df = pd.read_excel(archivo)
#Realizar procesamiento de limpieza al dataframe
df_clean = data_cleaner(df)
#Genar formulario con cada uno de los registros del IEEH, se debe ingresar el dataframe limpio, además del nombre del hospital para generar los pdfs correspondientes
complete_form(df_clean,'HOSPITAL DEL SALVADOR')

