import smtplib
import schedule
from email.message import EmailMessage
import DB_Connect
import random
import time
from threading import Thread
print('---------------------------')
print('Bem vindo ao Daily Letter Server')
print('---------------------------')
print('---------------------------')


# region | App setup |

def autenticar_destinatario_e_remetente():
    try:
        global remetente
        global senha_remetente
        remetente = input('Digite o seu e-mail: ')
        senha_remetente = input('Digite a sua senha: ')
        print('Autenticando E-mail')
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(f'{remetente}', f'{senha_remetente}')
        print('E-mail autenticado com sucesso!')
    except:
        print('Login ou Senha inválidos')
        autenticar_destinatario_e_remetente()


autenticar_destinatario_e_remetente()


def definir_hora():
    global Hora
    Hora = int(input('Defina a hora do dia que deseja enviar o e-mail no formato HHMM: '))
    if len(str(Hora)) != 4:
        print('Digite um numero valido')
        definir_hora()


definir_hora()

hora = (str(Hora)[:2] + ':' + str(Hora)[2:])

print('Horario definido para: ' + hora)


destinatario = input('Digite o e-mail do destinatario: ')
print('Destinatario definido como: ' + f'{destinatario}')


titulo = input('Digite o título do E-mail: ')
print('Título do E-mail Definido para: ' + f'{titulo}')
print('---------------------------')

# endregion


def random_number():
    msgcount = DB_Connect.get_msg_count()
    random_number = random.randint(1, msgcount)
    return random_number


def ramdom_message():
    picked_message = DB_Connect.get_random_msg(random_number())
    print('Mensagem Selecionada: ' f'{picked_message}')
    return picked_message


def enviar_email():  # -> Função pra enviar E-mail |
    print('Enviando E-mail')
    # | Define a Mensagem  |
    msg = EmailMessage()
    msg.set_content(f'{ramdom_message()}')
    msg['Subject'] = f'{titulo}'
    msg['From'] = f'{remetente}'
    msg['to'] = f'{destinatario}'

    # | Login |
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.login(f'{remetente}', f'{senha_remetente}')

    # | Envia e-mail |

    s.sendmail(f'{remetente}', f'{destinatario}', msg.as_string())
    print('Carta enviada')

    # | Desconecta |
    s.quit()

# region | Agenda |


schedule.every().monday.at(f'{hora}').do(enviar_email)
schedule.every().tuesday.at(f'{hora}').do(enviar_email)
schedule.every().wednesday.at(f'{hora}').do(enviar_email)
schedule.every().thursday.at(f'{hora}').do(enviar_email)
schedule.every().friday.at(f'{hora}').do(enviar_email)


# endregion

def run_agenda():
    while True:
        schedule.run_pending()
        time.sleep(1)


def run_socket():
    import Server_Socket

# region | MultiThreads - Roda Socket e Agenda ao mesmo tempo |


Thread(target=run_socket).start()
Thread(target=run_agenda()).start()

# endregion
