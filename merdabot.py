##{u'username': u'Merdamerdabot', u'first_name': u'Merdabot', u'id': 305298639}
#!-*- encoding: utf8 -*-

# Usando getUpdates():
#getUpdates(self, offset=None, limit=None, timeout=None, allowed_updates=None)
#offset deve ser o update_id do ultimo update recebido + 1 (update_id nao tem nada a ver com tempo)
#formato do update: vem uma lista em que cada elemento e um dicionario correspondendo a uma mensagem
#cada mensagem e um dicionario com apenas duas chaves: 'message' e 'update_id'
#estranhamente, u'message' e uma forma de escrever 'message'
#coisas que podem ser interessantes dentro de 'message': 'text' e o texto da mensagem; 'chat' e um dicionario com informacoes sobre a conversa  e 'from' e um dicionario indicando o remetente da mensagem

# Usando message_loop e handle:
#recebe-se direto o dicionario associado a chave 'message'


import telepot
import time
boto=telepot.Bot("278859188:AAEIrp4ydKGe9AQWy59fbCRLsnpw6mQUFN8")

offset=int(open("offset.txt","r").readline())


class MensagemErrada(Exception):
    pass

def contagem_incremento(addr, chat_id, incrementa):
    
    dados=open(addr,'r').readlines()
    try:
        i=dados.index(str(chat_id)+"\n")
        count=int(dados[i+1])
    except ValueError:
        i=len(dados)
        dados+=[str(chat_id)+"\n",0]
        count=0
    if incrementa:
        count+=1
        dados[i+1]=str(count)+"\n"
        escritor=open(addr,'w')
        for elem in dados:
            escritor.write(str(elem))
        escritor.close()
    return count


def tratador(update):
    global offset
    offset=update["update_id"]+1
    print update
    
    update=update["message"]
    registro=open('log.txt','a')
    registro.write(str(update)+'\n')
    registro.close()
    if not 'text' in update:
        raise MensagemErrada
    texto=update['text']
    chat_id=update['chat']['id']
    if texto=="/merda" or texto=="/merda@Merdamerdabot":
        contagem=contagem_incremento("estatisticas.txt",chat_id, True)
        boto.sendMessage(chat_id,"merda\n"*contagem)
    elif texto=="/stat" or texto=="/stat@Merdamerdabot":
        contagem=contagem_incremento("estatisticas.txt",chat_id,False)
        if update['chat']['type']=='group':
            mensagem="Fui chamado "+str(contagem)+" vezes no grupo "+update['chat']['title']+".\n"+update['from']['first_name']+", seu merda!"
        else:
            mensagem="Fui chamado "+str(contagem)+" vezes no privado por "+update['chat']['first_name']+" "+update['chat']['last_name']+".\n"+update['from']['first_name']+", seu merda!"
        boto.sendMessage(chat_id,mensagem)
    elif texto=="/melda" or texto=="/melda@Merdamerdabot":
        boto.sendMessage(chat_id, "chola mais")
    
def recebedor(bot, handle):
    global offset
    mensagens=bot.getUpdates(offset, 100, 10, ["bot_command"])
    for msg in mensagens:
        try:
            handle(msg)
        except MensagemErrada:
            pass


recebedor(boto, tratador)
print offset
open("offset.txt","w").write(str(offset))




    


print "cheguei no fim"

#boto.message_loop(handle,0.1,20,None,None,True,20,False)
#KeyboardInterrupt nao funciona
#run_forever e necessario pra rodar fora do IDLE
