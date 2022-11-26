import telebot
import requests

# Pegar o ID do ultimo chat que o bot foi inserido ou mandaram mensagem
def last_chat_id():
    token = ''  #Token ID do BOT, fornecido pelo FatherBot
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum Grupo Encontrado!')
        else:
            print("A resposta falhou, codigo de status:{}".format(response.status_code))
    except Exception as e:
        print ("Erro no getUpdates:", e)
        
        
#Função Enviar mensagem
def send_message(msg):
    token = ''  #Token ID do BOT, fornecido pelo FatherBot
    chat_id = ''   #Chat ID (descoberto utilizando a funçao anterior)

    try:
        data = {"chat_id": chat_id,"text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url,data)
    except Exception as e:
        print("Erro no SendMessage:", e)


