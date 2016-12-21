##{u'username': u'Merdamerdabot', u'first_name': u'Merdabot', u'id': 305298639}
#!-*- conding: utf8 -*-

# Usando getUpdates():
#formato do update: vem uma lista em que cada elemento e um dicionario correspondendo a uma mensagem
#cada mensagem e um dicionario com apenas duas chaves: 'message' e 'update_id'
#estranhamente, u'message' e uma forma de escrever 'message'
#coisas que podem ser interessantesdentro de 'message': 'text' e o texto da mensagem; 'chat' e um dicionario com informacoes sobre a conversa  e 'from' e um dicionario indicando o remetente da mensagem

# Usando message_loop e handle:
#recebe-se direto o dicionario associado a chave 'message'


import telepot
boto=telepot.Bot("278859188:AAEIrp4ydKGe9AQWy59fbCRLsnpw6mQUFN8")
boto.getMe()

def contagem_incremento(addr, chat_id, incrementa):
    
    dados=open(addr,'r').read().split("\n")
    try:
        i=dados.index(str(chat_id))
        count=int(dados[i+1])
    except ValueError:
        i=len(dados)
        dados+=[chat_id,0]
        count=0
    if incrementa:
        count+=1
        dados[i+1]=count
        escritor=open(addr,'w')
        for elem in dados:
            escritor.write(str(elem)+"\n")
        escritor.close()
    return count


def handle(update):
    registro=open('log.txt','a')
    registro.write(str(update)+'\n'+'xxxx')
    registro.close()
    texto=update['text']
    chat_id=update['chat']['id']
    if texto=="/merda" or texto=="/merda@Merdamerdabot":
        contagem=contagem_incremento("estatisticas.txt",chat_id, True)
        boto.sendMessage(chat_id,"merda\n"*contagem)
    elif texto=="/stat" or texto=="/stat@Merdamerdabot":
        contagem=contagem_incremento("estatisticas.txt",chat_id,False)
        if update['chat']['type']=='group':
            mensagem="Fui chamado "+str(contagem)+" vezes no chat "+update['chat']['title']+".\n"+update['from']['first_name']+", seu merda!"
        else:
            mensagem="Fui chamado "+str(contagem)+" vezes no privado por "+update['chat']['first_name']+" "+update['chat']['last_name']+".\n"+update['from']['first_name']+", seu merda!"
        boto.sendMessage(chat_id,mensagem)
    elif texto=="/melda" or texto=="/melda@Merdamerdabot":
        boto.sendMessage(chat_id, "chola mais")
    




boto.message_loop(handle,0.1,20,None,True,3,True)
#KeyboardInterrupt nao funciona
#run_forever e necessario pra rodar fora do IDLE
