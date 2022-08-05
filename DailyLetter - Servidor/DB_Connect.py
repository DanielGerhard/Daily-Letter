import mysql.connector

# region | login na DB |

def connect_DB():
    global cn
    global cursor
    cn = mysql.connector.connect(user='root', password='1234',
                                 host='localhost',
                                 database='dailyletter')
    cursor = cn.cursor()
    print('---------------------------')
    print('Conectado ao Banco de Dados')
    print('---------------------------')

# endregion


def get_msg_count():
    # Certifica que o número randomico não é maior que o de Mensagens
    cursor.execute("SELECT COUNT(*) FROM MENSAGENS")
    msgcount = cursor.fetchone()[0]
    return msgcount


def get_random_msg(random_number):
    try:
        cursor.execute(f"SELECT MENSAGEM FROM MENSAGENS WHERE IDMENSAGEM = '{random_number}'")
        return cursor.fetchone()[0]
    except:
        get_random_msg()


def registrar_mensagens(newusermessage):
    cursor.execute(f"INSERT INTO MENSAGENS VALUES(NULL, '{newusermessage}')")
    cn.commit()
