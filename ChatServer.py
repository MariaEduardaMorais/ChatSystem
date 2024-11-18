from xmlrpc.server import SimpleXMLRPCServer
import uuid

class ChatServer:
    def __init__(self):
        self.usuarios = {}  # {usuario_id: nome}
        self.mensagens = []  # Lista de mensagens públicas
        self.mensagens_privadas = []  # Lista de mensagens privadas no formato (remetente, destinatário, mensagem)
        self.usuarios_ativos = set()  # Conjunto de nomes de usuários ativos

    def Ingressar_no_sistema(self, nome_do_usuario):
        usuario_id = str(uuid.uuid4())
        self.usuarios[usuario_id] = nome_do_usuario
        return usuario_id

    def Entrar_na_sala(self, usuario_id):
        if usuario_id in self.usuarios:
            nome = self.usuarios[usuario_id]
            self.usuarios_ativos.add(nome)
            return f"Usuário {nome} entrou na sala."
        return "Usuário não encontrado."

    def Sair_da_sala(self, usuario_id):
        if usuario_id in self.usuarios:
            nome = self.usuarios[usuario_id]
            if nome in self.usuarios_ativos:
                self.usuarios_ativos.remove(nome)
                return f"Usuário {nome} saiu da sala."
        return "Usuário não está na sala."

    def Enviar_mensagem(self, usuario_id, mensagem):
        if usuario_id in self.usuarios:
            nome = self.usuarios[usuario_id]
            if nome in self.usuarios_ativos:
                self.mensagens.append(f"{nome}: {mensagem}")
                return "Mensagem enviada com sucesso."
        return "Usuário não está na sala."

    def Enviar_mensagem_usuario(self, usuario_id, destinatario_nome, mensagem):
        if usuario_id in self.usuarios:
            remetente_nome = self.usuarios[usuario_id]
            if remetente_nome in self.usuarios_ativos and destinatario_nome in self.usuarios_ativos:
                self.mensagens_privadas.append((remetente_nome, destinatario_nome, mensagem))
                return f"Mensagem privada enviada para {destinatario_nome}."
        return "Um ou ambos os usuários não estão na sala."

    def Listar_mensagens(self, usuario_id):
        if usuario_id in self.usuarios:
            nome = self.usuarios[usuario_id]
            if nome in self.usuarios_ativos:
                # Filtra mensagens públicas e privadas destinadas ao usuário
                mensagens_destinadas = [
                    f"(Privada de {remetente}) {mensagem}"
                    for remetente, destinatario, mensagem in self.mensagens_privadas
                    if destinatario == nome
                ]
                return self.mensagens + mensagens_destinadas
        return []

    def Listar_usuarios(self):
        return list(self.usuarios_ativos)

# Inicia o servidor
server = SimpleXMLRPCServer(("localhost", 9000))
server.register_instance(ChatServer())

print("Servidor de chat iniciado...")
server.serve_forever()
