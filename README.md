# WebScraping-Qanlex
Contexto teorico. ![ejercicio.pdf](https://github.com/AdrianPerez0306/WebScraping-Qanlex/blob/1919300833bcfd8d714f6c503c734e3a3e101743/Qanlex%20-%20Ejercicio%20para%20aplicantes.pdf)

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
python3 -m venv .venv
source .venv/bin/activate
```
Instalar dependencias:
```bash
pip install -r requirements.txt
```
Una vez instaladas las dependencias ya podemos ejecutar los scripts
