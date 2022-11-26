# TelegramBot
Envio de mensagens pelo Telegram

Após criação do Bot pelo Father BOT no proprio Telegram, ele irá gerar um codigo API para utilização do BOT.
Esse codigo API está como TOKEN no codigo.


Após adicionar o token do bot, criar um grupo no telegram e adicionar o bot neste grupo e executar o metodo last_chat_id().
Esse comando irá identificar o código do grupo que foi adicionado por ultimo.

Após ter o Token e o codigo do grupo, somente preencher as variaveis e token e chat_id na função send_message.

Para enviar mensagens somente chamar a funcao   send_message(mensagem)
