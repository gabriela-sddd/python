
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
import os

# Configurações do Telegram (obtenha as suas em https://my.telegram.org/auth)
api_id = 'insira o api id'
api_hash = 'insira o hash'
phone_number = '+5561... seu telefone'

def download_files(client, chat_name_or_id):
    # Diretório onde os arquivos serão salvos
    download_dir = 'downloads'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

# Criar uma pasta "download_telegram" dentro do diretório de download
    download_telegram_dir = os.path.join(download_dir, 'download_telegram')
    if not os.path.exists(download_telegram_dir):
        os.makedirs(download_telegram_dir)
        
    print("Iniciando o download dos arquivos...")

    try:
        # Obtendo a entidade do chat
        chat_entity = client.get_entity(chat_name_or_id)

        # Filtrar mensagens apenas com documentos (arquivos)
        messages = client.get_messages(chat_entity, filter=InputMessagesFilterDocument)

        # Ordenar as mensagens pelo ID
        messages = sorted(messages, key=lambda x: x.id)

        # Baixar os arquivos
        for msg in messages:
            file_name = os.path.join(download_dir, msg.file.name)
            client.download_media(msg, file_name)

        print("Todos os arquivos foram baixados com sucesso e salvos na pasta 'downloads'!")

    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

if __name__ == "__main__":
    # Criar um cliente Telegram
    client = TelegramClient('session_name', api_id, api_hash)

    # Conectar ao Telegram
    client.start(phone_number)

    chat_name_or_id = input("Digite o nome ou ID do chat de onde deseja extrair os arquivos: ")
    download_files(client, chat_name_or_id)

    # Encerrar a conexão
    client.disconnect()
