# WebScraping-Qanlex
Contexto teorico. ![TP Base de datos 2024 UNSAM.pdf](https://github.com/AdrianPerez0306/gestorAlumnos/blob/42ace063c036c55184657ba6f19447c937ccb2e3/TP%20Base%20de%20datos%202024%20UNSAM.pdf)

## Instalación de entorno :hammer_and_wrench: 
Este desarrolo fue realizado en un entorno de `OS debian ubuntu 22.04`, [`python 3.10.12`].

`Python on Ubuntu 22.04`
```bash
sudo apt update
sudo apt install python3.10.12
```
```bash
python3 --version
```

Una vez instalado python, nos dirigimos al folder del proyecto, y ejecutamos:
```bash
pip install virtualenv
```
Una vez instalado Python, descargamos virtualenv para crear un entorno virtual e instalar las dependencias necesarias:
```bash
virtualenv .venv
source .venv/bin/activate
```
Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Instalación de entorno :hammer_and_wrench: 
Ejecutar el scrip en vscode(agregar extension de python debugger) o ejecutar:
```bash
python3 main.py
python3 preprocessing/preprocessing.py
```

