# CrazyLover
Este script en Python implementa un bot de Telegram que envía piropos románticos a usuarios específicos. El bot utiliza la biblioteca python-telegram-bot para interactuar con la API de Telegram.

# Funcionalidades
/start: Comando que da la bienvenida al usuario al bot. 

/piropo: Comando que envía piropos románticos al azar a usuarios específicos.

/id: Comando que devuelve la ID de usuario del remitente.

/whois: Comando que devuelve la ID de otro usuario al responder a su mensaje o reenviarlo.
# Configuración
Antes de ejecutar el bot, asegúrate de realizar los siguientes pasos:

### Obtener Token de Telegram:

Obtén un token para tu bot de Telegram siguiendo las instrucciones en BotFather.

Reemplaza 'TU_TOKEN_DE_TELEGRAM' con el token de tu bot en el script.
### Definir Lista de Usuarios:

En la variable 'lista_de_usuarios', añade las ID reales de los usuarios a los que deseas enviar piropos.
### Instalar Dependencias:

Instala las dependencias ejecutando.
```pip install python-telegram-bot```
### Ejecutar el Script:

Ejecuta el script para iniciar el bot.
```
python3 CrazyLover.py
```
# Piropos
La función 'piropo_al_azar()' elige aleatoriamente un piropo de la lista predefinida. Puedes personalizar la lista según tus preferencias.
 y enviar un pull request.
