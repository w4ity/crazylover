# Importaciones necesarias para el bot de Telegram
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater
import random

# Función que devuelve un piropo al azar de una lista predefinida
def piropo_al_azar():
    piropos = [
        # ... (lista de piropos) Ejemplo:
    "Eres como un sueño del que no quiero despertar.",
    "Tu sonrisa ilumina mi día.",
    "Si la belleza fuera tiempo, tú serías la eternidad.",
    "Eres la razón por la que creo en el amor a primera vista.",
    "Cada día contigo es un regalo.",
    "Eres más dulce que el chocolate.",
    "Si fueras una estrella, serías la más brillante del cielo.",
    "Eres la obra maestra que la naturaleza tardó millones de años en crear.",
    "Cada momento contigo es como un cuento de hadas.",
    "Tu belleza deja sin palabras a las flores.",
    "Eres el sueño que nunca supe que tenía.",
    "Contigo cada día es San Valentín.",
    "Si la perfección tuviera nombre, sería el tuyo.",
    "Tus ojos son dos luceros que iluminan mi camino.",
    "Eres la melodía que siempre quiero escuchar.",
    "Eres la razón por la que creo en los cuentos de hadas.",
    "Eres como un rayo de sol en un día nublado.",
    "Cada día a tu lado es una aventura.",
    "Eres la chispa que enciende mi corazón.",
    "Tus abrazos son mi lugar favorito en el mundo.",
    "Eres tan dulce que podrías hacer que las abejas dejen de buscar miel.",
    "Si fueras un error, serías un error excepcional.",
    "¿Eres Google? Porque tienes todo lo que he estado buscando.",
    "Eres como una clave primaria, sin ti no puedo encontrar el sentido.",
    "Si fueras una función, serías asintótica, porque nunca te acercas, pero nunca te alejas.",
    "¿Eres un ángel? Porque eres tan raro que dudo que existas.",
    "Si fueras un algoritmo, serías O(1), porque eres constante en mi mente.",
    "Eres el archivo CSS que le da estilo a mi HTML.",
    "¿Tienes un nombre o puedo llamarte el mío?",
    "Eres como una excepción, difícil de manejar pero imposible de ignorar.",
    "Si fueras un lenguaje de programación, serías C++, porque tienes clases.",
    "¿Eres un programa? Porque haces que mi corazón se bloquee y se reinicie.",
    "Eres como JavaScript, todos dicen que debería amarte, pero realmente no entiendo por qué.",
    "¿Eres un cable HDMI? Porque sin ti, mi vida no tiene sentido.",
    "Tienes mucha suerte de ver este mensaje, a ver cuando me besas ya. "

    ]
    piropo = random.choice(piropos)
    return piropo

# Token de tu bot de Telegram y lista de usuarios a los que se les enviarán piropos
TOKEN = 'TU_TOKEN_DE_TELEGRAM'
lista_de_usuarios = ['ID_USUARIO1', 'ID_USUARIO2']  # Sustituir con las ID reales

# Función para manejar el comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Soy tu bot. Usa el comando /enviar_mensaje para enviar mensajes a la lista de usuarios.')

# Función para enviar un piropo a los usuarios de la lista
def enviar_mensaje(update: Update, context: CallbackContext) -> None:
    mensaje = f"{piropo_al_azar()}"
    for usuario in lista_de_usuarios:
        try:
            context.bot.send_message(chat_id=usuario, text=mensaje)
            print(f"Mensaje enviado a {usuario}")
        except Exception as e:
            print(f"No se pudo enviar mensaje a {usuario}: {str(e)}")

# Función para obtener la ID del usuario que envía el comando /id
def obtener_id(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    update.message.reply_text(f"Tu ID de usuario es: {user_id}")

# Función para obtener la ID de otro usuario (usado con el comando /whois)
def whois(update: Update, context: CallbackContext) -> None:
    # ... (código para obtener y mostrar la ID de otro usuario) Ejempolo:
    # Verifica si es un mensaje reenviado y si está respondiendo a un mensaje
    if update.message.forward_from:
        forwarder_name = update.message.forward_from.username
        forwarder_id = update.message.forward_from.id
        update.message.reply_text(f"ID de {forwarder_name}: {forwarder_id}")
    elif update.message.reply_to_message and update.message.reply_to_message.from_user:
        # Si está respondiendo a un mensaje, obtén la información del remitente del mensaje al que está respondiendo
        replied_user = update.message.reply_to_message.from_user
        update.message.reply_text(f"ID de {replied_user.username}: {replied_user.id}")
    else:
        update.message.reply_text("Por favor, reenvía un mensaje o responde a un mensaje para obtener información del usuario.")


# Función para manejar mensajes normales (no comandos)
def handle_message(update: Update, context: CallbackContext) -> None:
    # ... (código para manejar mensajes normales y realizar acciones) Ejemplo:
    text = update.message.text
    user_id = update.message.from_user.id

    if text == '/enviar_mensaje':
        enviar_mensaje(update, context)
    elif text == '/id':
        obtener_id(update, context)
        
    elif user_id not in lista_de_usuarios:
        # Si la ID del usuario no está en la lista, agrégala.
        lista_de_usuarios.append(user_id)
        update.message.reply_text(f"¡Bienvenido! ")
    else:
        if random.choice([True, False]):
            update.message.reply_text(f" {text}, si")
        else:
            update.message.reply_text("Bla bla bla...")



# Función principal para iniciar el bot y configurar manejadores
def main() -> None:
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot)

    # Agregar manejadores de comandos y mensajes
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("piropo", enviar_mensaje))
    updater.dispatcher.add_handler(CommandHandler("id", obtener_id))
    updater.dispatcher.add_handler(CommandHandler("whois", whois))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

# Punto de entrada para ejecutar el script
if __name__ == '__main__':
    main()
