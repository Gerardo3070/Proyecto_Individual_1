import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Levenshtein as lev
#pip install Levenshtein
#from unipath import Path
sns.set()
#csv=input('Dame el nombre del nuevo archivo de clientes con extensión')
#rutarel = Path('../Datasets/')
#ruta=Path(csv)
#rutasol = rutarel + ruta
#clientes2 = pd.read_csv(rutasol, delimiter=';')
'''
En el siguiente trabajo dejo fuera la automatización debido a que no entendí si se tenía que hacer o no
para eso utilicé unipath y pediría los archivos a cargar para hacerlo de manera automática



'''
clientes = pd.read_csv('../Datasets/Clientes.csv', delimiter=';')
clientes.rename(columns = {'ID': 'IdCliente', 'Nombre_y_Apellido': 'Nombre_completo', 'X': 'Latitud', 'Y': 'Longitud'}, inplace = True)
clientes['IdCliente'].drop_duplicates(inplace=True)
clientes.drop('col10', axis=1, inplace=True)
clientes['Latitud'] = clientes.apply(lambda row: str(row['Latitud']).replace(',','.'), axis=1)
clientes['Longitud'] = clientes.apply(lambda row: str(row['Longitud']).replace(',','.'), axis=1)
clientes = clientes.astype({"Latitud": np.float16, "Longitud": np.float16})
clientes['Lat'] = clientes['Latitud']
clientes['Lon'] = clientes['Longitud']
clientes['Latitud'] = clientes.apply(lambda row: row['Lat'] if row['Lat'] < -20 and row['Lat'] > -50 else row['Lon'], axis=1)
clientes['Longitud'] = clientes.apply(lambda row: row['Lon'] if row['Lon'] < -51 and row['Lon'] >-75 else row['Lat'], axis=1)
clientes.drop(['Lat'], inplace=True, axis=1)
clientes.drop(['Lon'], inplace=True, axis=1)
clientes.to_csv('Clientes_nuevo.csv')
############Tabla Compras
compra = pd.read_csv('../Datasets/Compra.csv', parse_dates=["Fecha"])
Q3=compra.Cantidad.describe()[6]
Q1=compra.Cantidad.describe()[4]
IQR=Q3-Q1
alto=Q3+(1.5*IQR)
compra=compra[compra.Cantidad<=alto]
compra=compra[compra.Precio<9555.04]
compra.to_csv('Compra_nuevo.csv')
########## Tabla Gasto
gasto = pd.read_csv('../Datasets/Gasto.csv', parse_dates=["Fecha"])
gasto.to_csv('Gasto_nuevo.csv')
########  Tabla localidades
localidades = pd.read_csv('../Datasets/Localidades.csv')
localidades.rename(columns = {'departamento_id': 'IdDepartamento', 'departamento_nombre': 'Departamento', 'centroide_lat': 'Latitud', 'centroide_lon': 'Longitud',
'id': 'IdTotal', 'localidad_censal_id': 'IdLocalidad', 'municipio_id': 'IdMunicipio', 'municipio_nombre': 'Municipio',
'nombre': 'Nombre', 'provincia_id': 'IdProvincia', 'provincia_nombre': 'Provincia',
'localidad_censal_nombre': 'Localidad'}, inplace = True)
localidades.drop(['IdMunicipio','Municipio'], axis=1, inplace=True)
localidades.to_csv('Localidades_nuevo.csv')
####### Tabla proveedores
proveedores = pd.read_csv('../Datasets/Proveedores.csv', encoding='latin-1')
proveedores.fillna('Sin dato', inplace=True)
proveedores.rename(columns = {'IDProveedor': 'IdProveedor', 'Address': 'Dirección', 'City': 'Ciudad',
'State': 'Estado', 'Country': 'País', 'departamen': 'Departamento'}, inplace = True)
proveedores.to_csv('Proveedores_nuevo.csv')
######## Tabla sucursales
sucursales = pd.read_csv('../Datasets/Sucursales.csv', delimiter=';')
sucursales['Latitud'] = sucursales.apply(lambda row: str(row['Latitud']).replace(',','.'), axis=1)
sucursales['Longitud'] = sucursales.apply(lambda row: str(row['Longitud']).replace(',','.'), axis=1)
sucursales.rename(columns = {'ID': 'IdSucursal'}, inplace = True)
localid=['Ciudad de Buenos Aires', 'Capital Federal', 'CABA', 'Vicente López', 'Martínez', 'Caseros', 'Moron', 'Castelar',
       'San Justo', 'Lanus', 'Avellaneda', 'Quilmes', 'La Plata',
       'Mar del Plata', 'Rosario', 'Córdoba', 'San Miguel de Tucumán', 'Mendoza', 'San Carlos de Bariloche']
for i in range(len(sucursales.Localidad)):
    for j in range(len(localid)):
        if lev.ratio(sucursales2.Localidad[i], localid[j]) > 0.5:
            sucursales2.Localidad[i]= localid[j]
sucursales.loc[sucursales.Localidad=='CABA','Localidad']='Ciudad de Buenos Aires'
sucursales.loc[sucursales.Localidad=='Capital Federal','Localidad']='Ciudad de Buenos Aires'
sucursales.to_csv('Sucursales_nuevo.csv')
############   Tabla ventas
venta = pd.read_csv('../Datasets/Venta.csv', parse_dates=["Fecha"])
venta=venta.sort_values(by='Fecha')
venta.reset_index(inplace=True)
venta.drop('index', axis=1, inplace=True)
venta=venta[venta.Precio<=7626.55]
venta['Precio'].fillna(venta.Precio.mean(), inplace=True)
venta.fillna(1, inplace=True)
indexNames = venta[(venta.Cantidad > 20) & (venta.Precio > 400)].index
venta.drop(indexNames , inplace=True)
venta.reset_index(inplace=True)
venta.drop('index', axis=1, inplace=True)
venta.to_csv('Venta_nuevo.csv')



############## Nuevas tablas
####clientes
clientes2 = pd.read_csv('../Datasets/Clientes_v2.csv', delimiter=';')
clientes2.rename(columns = {'ID': 'IdCliente', 'Nombre_y_Apellido': 'Nombre_completo', 'X': 'Latitud', 'Y': 'Longitud'}, inplace = True)
clientes2['IdCliente'].drop_duplicates(inplace=True)
clientes2['Latitud'] = clientes2.apply(lambda row: str(row['Latitud']).replace(',','.'), axis=1)
clientes2['Longitud'] = clientes2.apply(lambda row: str(row['Longitud']).replace(',','.'), axis=1)
clientes2 = clientes2.astype({"Latitud": np.float16, "Longitud": np.float16})
clientes2['Lat'] = clientes2['Latitud']
clientes2['Lon'] = clientes2['Longitud']
clientes2['Latitud'] = clientes2.apply(lambda row: row['Lat'] if row['Lat'] < -20 and row['Lat'] > -50 else row['Lon'], axis=1)
clientes2['Longitud'] = clientes2.apply(lambda row: row['Lon'] if row['Lon'] < -51 and row['Lon'] >-75 else row['Lat'], axis=1)
clientes2.drop(['Lat'], inplace=True, axis=1)
clientes2.drop(['Lon'], inplace=True, axis=1)
clientes = pd.concat([clientes, clientes2])
clientes.drop_duplicates(inplace=True)
clientes.index = range(clientes.shape[0])
clientes.to_csv('Clientes_nuevo.csv')
###ventas
venta2 = pd.read_csv('../Datasets/Venta_Dic2020.csv', parse_dates=["Fecha"])
venta2=venta2.sort_values(by='Fecha')
venta2.reset_index(inplace=True)
venta2.drop('index', axis=1, inplace=True)
venta2=venta2[venta2.Precio<=7626.55]
venta2['Precio'].fillna(venta2.Precio.mean(), inplace=True)
venta2.fillna(1, inplace=True)
indexNames = venta2[(venta2.Cantidad > 20) & (venta2.Precio > 400)].index
venta2.drop(indexNames , inplace=True)
venta2.reset_index(inplace=True)
venta2.drop('index', axis=1, inplace=True)
venta = pd.concat([venta, venta2])
venta.index = range(venta.shape[0])
venta.to_csv('Venta_nuevo.csv')

'''
importación a sql
clientes.to_sql(name='clientes', con=engine, if_exists='append', index=False)
compra.to_sql(name='compra', con=engine, if_exists='append', index=False)
gasto.to_sql(name='gasto', con=engine, if_exists='append', index=False)
localidades.to_sql(name='localidades', con=engine, if_exists='append', index=False)
proveedores.to_sql(name='proveedores', con=engine, if_exists='append', index=False)
sucursales.to_sql(name='sucursales', con=engine, if_exists='append', index=False)
venta.to_sql(name='venta', con=engine, if_exists='append', index=False)
'''