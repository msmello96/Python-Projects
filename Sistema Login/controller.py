from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Cadastro
from hashlib import sha256


def RetornaSession():
    USUARIO = 'marcelo'
    SENHA = 'marcelo123'
    HOST = 'localhost'
    BANCO = 'syslogin'
    PORT = '3306'

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)

    return Session()

session = RetornaSession()

class CadastroController:
    
    @classmethod
    def verificaDados(cls, nome, email, senha):
        if len(nome) < 3 or len(nome) > 50:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) < 6 or len(senha) > 100:
            return 4
        
        return 1

    @classmethod
    def novoCadastro(cls, novoNome, novoEmail, novaSenha):
        session = RetornaSession()
        usuario = session.query(Cadastro).filter(Cadastro.email == novoEmail).all()

        if len(usuario) > 0:
            return 5
        
        dados_verificados = cls.verificaDados(novoNome, novoEmail, novaSenha)

        if dados_verificados != 1:
            return dados_verificados

        try:
            novaSenha = sha256(novaSenha.encode()).hexdigest()

            a = Cadastro(nome=novoNome, email=novoEmail, senha=novaSenha)
            session.add(a)
            session.commit()
        except:
            return 6

class LoginController():
    @classmethod
    def login(cls, email, senha):
        session = RetornaSession()
        senha = sha256(senha.encode()).hexdigest()
        logado = session.query(Cadastro).filter(Cadastro.email == email).filter(Cadastro.senha == senha).all()

        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False


# CadastroController().novoCadastro('Maisa', 'Maisa@gmail.com', 'Maisa1234567')
# print(LoginController.login('marcelo@gmail.com', 'Marcelo123'))
