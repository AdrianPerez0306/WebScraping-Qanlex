# WebScraping-Qanlex
Contexto teorico. ![TP Base de datos 2024 UNSAM.pdf](https://github.com/AdrianPerez0306/gestorAlumnos/blob/42ace063c036c55184657ba6f19447c937ccb2e3/TP%20Base%20de%20datos%202024%20UNSAM.pdf)

## Instalación :hammer_and_wrench: 
Este desarrolo fue realizado en un entorno de `OS debian ubuntu 22.04`, [`python 3.10.12`], [`PostgreSQL`](https://www.postgresql.org/) con [`PgAdmin`](https://www.pgadmin.org/).

`Python on Ubuntu 22.04`
```bash
sudo apt update
sudo apt install python3
```
```bash
python3 --version
```
```bash
python3 pip install pandas
```
`PostgreSQL`
Acorde a [`PostgreSQL`](https://www.postgresql.org/download/linux/ubuntu/):
```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```
`PgAdmin`
Acorde a [`PostgreSQL`](https://www.postgresql.org/download/linux/ubuntu/):
```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```

Una vez tenemos instalado `python`, podemos comenzar el preprocesado. Partiendo del archivo [`raw-data.csv`](preprocessing/raw-data.csv) tenemos labels/columnas de la siguiente forma:

![image](https://github.com/user-attachments/assets/27a3ff0b-410a-4128-adc2-1f1714e79533)

Abrimos [`preprocessing.py`](preprocessing/preprocessing.py) y ejecutamos el script:
```bash
python preprocessing.py
```
Esto generara una serie de `archivos.csv`, que corresponden a los datos necesarios para realizar la carga dentro del sistema `PostgreSQL`
NOTA: Dentro script `preprocessing.py` se encuentra el path donde se descargaran los archivos. MODIFICAR ESTE PATH SEGUN SU O.S

![image](https://github.com/user-attachments/assets/a36596e0-0898-4533-9ef2-7624dd4ab945)

Una vez ejecutado, en el `path` que haya configurado en el script `preprocessing.py`, deberian aparecer una serie de archivos:

![image](https://github.com/user-attachments/assets/9d63581d-5389-4f5b-9fb0-9c8134cf3d9c)

Una vez con estos archivos en la carpeta correspondiente, procedemos a abrir `PgAdmin`. A partir de aqui hay 2 caminos posibles:

### 1 - Construccion del sistema de base de datos desde querys.
#### Pasos a seguir
##### a) Crear un server en PgAdmin.

![image](https://github.com/user-attachments/assets/3a22f8bb-34f5-4b8f-a55d-aeaa2466b365)

Determinar el nombre del server.

![image](https://github.com/user-attachments/assets/6d289825-8848-495f-bfe2-e0e0ec9668ba)

Una vez creado el server deberia verse un panel como el siguiente:

![image](https://github.com/user-attachments/assets/f413e971-1a44-4d10-9789-6a8ddee8bc7e)

Con el server ya creado procedemos a utilizar la query tool que provee `PostgreSQL`:
![image](https://github.com/user-attachments/assets/7bc8605f-209c-4888-a69e-d092fec69446)
![image](https://github.com/user-attachments/assets/dc254c26-a05d-4f2e-af2e-e15b8c49ddc9)


##### b) Abrir querys tool.
Una vez en el panel de querys, procedemos a ejecutar las querys. 

i) Ejecutar todos los querys en el folder `procedures_calls`

IMPORTANTE: Si quiere ejecutar las `procedures_calls` primero debe copiar los archivos dentro de `procedures` y ejecutarlos dentro de la query tool.

  `call_init` -> `call_load_column` -> `call_load_alumnos`
  Una vez ejecutados los querys, deberia estar creadas las tablas y cargados los datos de los archivos correspondientes.
  A partir de aqui, ya se pueden realizar consultas.

##### c) Ejecutar querys.
Una vez en el panel de querys, procedemos a ejecutar las querys. En este caso pordemos importarla seleccionando `Open file` en la query tool.
Aqui, ya importado el query correspondiente, ejecutamos dandole al boton de play. Ya ejecutados los querys se pueden realizar consultar.


![image](https://github.com/user-attachments/assets/1f95b4b1-b4a9-47b4-90a8-c91ae1c65272)

NOTA: Para realizar consultas se pueden repetir los pasos `b` y `c`, cargando los querys dentro del folder `consultas`, con los archivos del folder `consultas`

##### d) Respuesta de las querys.
A partir de aqui es cuestion de jugar con las consultar, modificar el sistema de gestion de base de datos, y extender las tablas, consultas, views, prodecures, etc...,  segun la necesidad.
![image](https://github.com/user-attachments/assets/8c8355fe-a92c-43b9-880b-ae5b0069f10b)


### 2 - Importar el archivo `SERVER.json`.
Dentro de `pgAdmin` seleccionar `Tools`-> `Import/Export server` -> Seleccionar `SERVER.json`

Esta seccion falta chequearla. Se recomienda utilizar la primera opcion.


