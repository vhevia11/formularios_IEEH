import pandas as pd

def data_cleaner(df):
    #Determinar largo de variables destino al alta, nombres, domicilio.
    df['DES_ALTA'] = df['DES_ALTA'].map(lambda x: str(x)[:-2])
    df['NOMBRES'] = df['NOMBRES'].map(lambda x: str(x)[:13])
    df['DOMICILIO'] = df['DOMICILIO'].map(lambda x: str(x)[:34])
    
    #Limpieza de datos vacios
    df = df.fillna(' ')

    #Cambio de formato fecha de nacimiento
    df['FECHA_NAC'] = df['A_NAC'].astype(str)+'/'+df['M_NAC'].astype(str)+'/'+df['D_NAC'].astype(str)
    df['FECHA_NAC'] = pd.to_datetime(df['FECHA_NAC'])
    df['FECHA_NAC'] =  df['FECHA_NAC'].dt.strftime('%d/%m/%Y')
    df['M_NAC'] = df['FECHA_NAC'].map(lambda x: str(x)[3:-5])
    df['D_NAC'] = df['FECHA_NAC'].map(lambda x: str(x)[:-8])

    #Cambio de formato fecha de ingreso
    df['FECHA_ING'] = df['ANO_ING'].astype(str)+'/'+df['MES_ING'].astype(str)+'/'+df['DIA_ING'].astype(str)
    df['FECHA_ING'] = pd.to_datetime(df['FECHA_ING'])
    df['FECHA_ING'] =  df['FECHA_ING'].dt.strftime('%d/%m/%Y')

    #Cambio de formato hora de ingreso
    df['HORA_ING'] = df['FECHA_ING'].astype(str)+' '+df['HORA_ING'].astype(str)+':'+df['MIN_ING'].astype(str)
    df['HORA_ING'] = pd.to_datetime(df['HORA_ING'])
    df['HORA_ING'] =  df['HORA_ING'].dt.strftime('%d/%m/%Y %H:%M')
    df['MIN_ING'] = df['HORA_ING'].map(lambda x: str(x)[14:])
    df['HORA_ING'] = df['HORA_ING'].map(lambda x: str(x)[11:-3])

    #Generar variables para cada parámetro de la fecha de ingreso
    df['DIA_ING'] = df['FECHA_ING'].map(lambda x: str(x)[:-8])
    df['MES_ING'] = df['FECHA_ING'].map(lambda x: str(x)[3:-5])
    df['ANO_ING'] = df['FECHA_ING'].map(lambda x: str(x)[8:])

    #Cambio de formato fecha de traslado 1
    df['MES_1_TRAS'] = df['MES_1_TRAS'].replace(' ', 0)
    df['DIA_1_TRAS'] = df['DIA_1_TRAS'].replace(' ', 0)
    df['MES_1_TRAS'] = df['MES_1_TRAS'].astype(int)
    df['DIA_1_TRAS'] = df['DIA_1_TRAS'].astype(int)
    df['ANO_1_TRAS'] = df['ANO_1_TRAS'].map(lambda x: str(x)[:-2])
    df['FECHA_1_TRAS'] = df['ANO_1_TRAS'].astype(str)+'/'+df['MES_1_TRAS'].astype(str)+'/'+df['DIA_1_TRAS'].astype(str)
    df.loc[(df['FECHA_1_TRAS'] == '0/0/0'), 'FECHA_1_TRAS'] = '2020/1/1'
    df.loc[(df['FECHA_1_TRAS'] == '/0/0'), 'FECHA_1_TRAS'] = '2020/1/1'
    df['FECHA_1_TRAS'] = pd.to_datetime(df['FECHA_1_TRAS'])
    df['FECHA_1_TRAS'] =  df['FECHA_1_TRAS'].dt.strftime('%d/%m/%Y')
    df.loc[(df['FECHA_1_TRAS'] == '01/01/2020'), 'FECHA_1_TRAS'] = ' '

    #Generar variables para cada parámetro de la fecha de traslado
    df['DIA_1_TRAS'] = df['FECHA_1_TRAS'].map(lambda x: str(x)[:-8])
    df['MES_1_TRAS'] = df['FECHA_1_TRAS'].map(lambda x: str(x)[3:-5])
    df['ANO_1_TRAS'] = df['FECHA_1_TRAS'].map(lambda x: str(x)[8:])

    df.loc[(df['FECHA_1_TRAS'] == '01/01/2020'), 'DIA_1_TRAS'] = ' '
    df.loc[(df['FECHA_1_TRAS'] == '01/01/2020'), 'MES_1_TRAS'] = ' '
    df.loc[(df['FECHA_1_TRAS'] == '01/01/2020'), 'ANO_1_TRAS'] = ' '

    #Cambio de formato fecha de traslado 2
    df['MES_2_TRAS'] = df['MES_2_TRAS'].replace(' ', 0)
    df['DIA_2_TRAS'] = df['DIA_2_TRAS'].replace(' ', 0)
    df['MES_2_TRAS'] = df['MES_2_TRAS'].astype(int)
    df['DIA_2_TRAS'] = df['DIA_2_TRAS'].astype(int)
    df['ANO_2_TRAS'] = df['ANO_2_TRAS'].map(lambda x: str(x)[:-2])
    df['FECHA_2_TRAS'] = df['ANO_2_TRAS'].astype(str)+'/'+df['MES_2_TRAS'].astype(str)+'/'+df['DIA_2_TRAS'].astype(str)
    df.loc[(df['FECHA_2_TRAS'] == '0/0/0'), 'FECHA_2_TRAS'] = '2020/1/1'
    df.loc[(df['FECHA_2_TRAS'] == '/0/0'), 'FECHA_2_TRAS'] = '2020/1/1'
    df['FECHA_2_TRAS'] = pd.to_datetime(df['FECHA_2_TRAS'])
    df['FECHA_2_TRAS'] =  df['FECHA_2_TRAS'].dt.strftime('%d/%m/%Y')
    df.loc[(df['FECHA_2_TRAS'] == '01/01/2020'), 'FECHA_2_TRAS'] = ' '

    #Generar variables para cada parámetro de la fecha de traslado 2
    df['DIA_2_TRAS'] = df['FECHA_2_TRAS'].map(lambda x: str(x)[:-8])
    df['MES_2_TRAS'] = df['FECHA_2_TRAS'].map(lambda x: str(x)[3:-5])
    df['ANO_2_TRAS'] = df['FECHA_2_TRAS'].map(lambda x: str(x)[8:])

    df.loc[(df['FECHA_2_TRAS'] == '01/01/2020'), 'DIA_2_TRAS'] = ' '
    df.loc[(df['FECHA_2_TRAS'] == '01/01/2020'), 'MES_2_TRAS'] = ' '
    df.loc[(df['FECHA_2_TRAS'] == '01/01/2020'), 'ANO_2_TRAS'] = ' '

    #Cambio de formato fecha de traslado 3
    df['MES_3_TRAS'] = df['MES_3_TRAS'].replace(' ', 0)
    df['DIA_3_TRAS'] = df['DIA_3_TRAS'].replace(' ', 0)
    df['MES_3_TRAS'] = df['MES_3_TRAS'].astype(int)
    df['DIA_3_TRAS'] = df['DIA_3_TRAS'].astype(int)
    df['ANO_3_TRAS'] = df['ANO_3_TRAS'].map(lambda x: str(x)[:-2])
    df['FECHA_3_TRAS'] = df['ANO_3_TRAS'].astype(str)+'/'+df['MES_3_TRAS'].astype(str)+'/'+df['DIA_3_TRAS'].astype(str)
    df.loc[(df['FECHA_3_TRAS'] == '0/0/0'), 'FECHA_3_TRAS'] = '2020/1/1'
    df.loc[(df['FECHA_3_TRAS'] == '/0/0'), 'FECHA_3_TRAS'] = '2020/1/1'
    df['FECHA_3_TRAS'] = pd.to_datetime(df['FECHA_3_TRAS'])
    df['FECHA_3_TRAS'] =  df['FECHA_3_TRAS'].dt.strftime('%d/%m/%Y')
    df.loc[(df['FECHA_3_TRAS'] == '01/01/2020'), 'FECHA_3_TRAS'] = ' '

    #Generar variables para cada parámetro de la fecha de traslado 3
    df['DIA_3_TRAS'] = df['FECHA_3_TRAS'].map(lambda x: str(x)[:-8])
    df['MES_3_TRAS'] = df['FECHA_3_TRAS'].map(lambda x: str(x)[3:-5])
    df['ANO_3_TRAS'] = df['FECHA_3_TRAS'].map(lambda x: str(x)[8:])

    df.loc[(df['FECHA_3_TRAS'] == '01/01/2020'), 'DIA_3_TRAS'] = ' '
    df.loc[(df['FECHA_3_TRAS'] == '01/01/2020'), 'MES_3_TRAS'] = ' '
    df.loc[(df['FECHA_3_TRAS'] == '01/01/2020'), 'ANO_3_TRAS'] = ' '

    #Cambio de formato fecha de traslado 4
    df['MES_4_TRAS'] = df['MES_4_TRAS'].replace(' ', 0)
    df['DIA_4_TRAS'] = df['DIA_4_TRAS'].replace(' ', 0)
    df['MES_4_TRAS'] = df['MES_4_TRAS'].astype(int)
    df['DIA_4_TRAS'] = df['DIA_4_TRAS'].astype(int)
    df['ANO_4_TRAS'] = df['ANO_4_TRAS'].map(lambda x: str(x)[:-2])
    df['FECHA_4_TRAS'] = df['ANO_4_TRAS'].astype(str)+'/'+df['MES_4_TRAS'].astype(str)+'/'+df['DIA_4_TRAS'].astype(str)
    df.loc[(df['FECHA_4_TRAS'] == '0/0/0'), 'FECHA_4_TRAS'] = '2020/1/1'
    df.loc[(df['FECHA_4_TRAS'] == '/0/0'), 'FECHA_4_TRAS'] = '2020/1/1'
    df['FECHA_4_TRAS'] = pd.to_datetime(df['FECHA_4_TRAS'])
    df['FECHA_4_TRAS'] =  df['FECHA_4_TRAS'].dt.strftime('%d/%m/%Y')
    df.loc[(df['FECHA_4_TRAS'] == '01/01/2020'), 'FECHA_4_TRAS'] = ' '

    #Generar variables para cada parámetro de la fecha de traslado 4
    df['DIA_4_TRAS'] = df['FECHA_4_TRAS'].map(lambda x: str(x)[:-8])
    df['MES_4_TRAS'] = df['FECHA_4_TRAS'].map(lambda x: str(x)[3:-5])
    df['ANO_4_TRAS'] = df['FECHA_4_TRAS'].map(lambda x: str(x)[8:])

    df.loc[(df['FECHA_4_TRAS'] == '01/01/2020'), 'DIA_4_TRAS'] = ' '
    df.loc[(df['FECHA_4_TRAS'] == '01/01/2020'), 'MES_4_TRAS'] = ' '
    df.loc[(df['FECHA_4_TRAS'] == '01/01/2020'), 'ANO_4_TRAS'] = ' '

    #Cambio de formato fecha de egreso
    df['FECHA_EGR'] = df['ANO_EGR'].astype(str)+'/'+df['MES_EGR'].astype(str)+'/'+df['DIA_EGR'].astype(str)
    df['FECHA_EGR'] = pd.to_datetime(df['FECHA_EGR'])
    df['FECHA_EGR'] =  df['FECHA_EGR'].dt.strftime('%d/%m/%Y')

    #Cambio de formato hora de egreso
    df['HORA_EGR'] = df['FECHA_EGR'].astype(str)+' '+df['HORA_EGR'].astype(str)+':'+df['MIN_EGR'].astype(str)
    df['HORA_EGR'] = pd.to_datetime(df['HORA_EGR'])
    df['HORA_EGR'] =  df['HORA_EGR'].dt.strftime('%d/%m/%Y %H:%M')
    df['MIN_EGR'] = df['HORA_EGR'].map(lambda x: str(x)[14:])
    df['HORA_EGR'] = df['HORA_EGR'].map(lambda x: str(x)[11:-3])

    df['DIA_EGR'] = df['FECHA_EGR'].map(lambda x: str(x)[:-8])
    df['MES_EGR'] = df['FECHA_EGR'].map(lambda x: str(x)[3:-5])
    df['ANO_EGR'] = df['FECHA_EGR'].map(lambda x: str(x)[8:])

    #Definir dataframe con anexo 02
    anexo02 = pd.read_excel('Anexo02.xlsx')
    df = df.merge(anexo02, left_on='COMUNA', right_on='Código Comuna', how='inner')

    #Definir dataframe con anexo 10
    anexo10 = pd.read_excel('Anexo10.xlsx')
    anexo10['Código'] = anexo10['Código'].astype(int)
    df = df.merge(anexo10, left_on='ESPEC', right_on='Código', how='inner')

    #definir cantidad de caracteres de areas funcionales de traslado
    df['AREAF_1_TRAS'] = df['AREAF_1_TRAS'].map(lambda x: str(x)[:-2])
    df['AREAF_2_TRAS'] = df['AREAF_2_TRAS'].map(lambda x: str(x)[:-2])
    df['AREAF_3_TRAS'] = df['AREAF_3_TRAS'].map(lambda x: str(x)[:-2])
    df['AREAF_4_TRAS'] = df['AREAF_4_TRAS'].map(lambda x: str(x)[:-2])
    df['AREAF_5_TRAS'] = df['AREAF_5_TRAS'].map(lambda x: str(x)[:-2])
    
    return df