from xmlrpc.server import SimpleXMLRPCServer
import uuid

class ChatServer:
    def __init__(self):
        self.usuarios = {}
        self.mensagens = []
        self.usuarios_ativos = set()

    def Ingressar_no_sistema(self, nome_do_usuario):
        # Gera um ID único para o usuário
        usuario_id = str(uuid.uuid4())
        self.usuarios[usuario_id] = nome_do_usuario
        return usuario_id

    def Entrar_na_sala(self, usuario_id):
        # Marca o usuário como ativo
        if usuario_id in self.usuarios:
            self.usuarios_ativos.add(usuario_id)
            return f"Usuário {self.usuarios[usuario_id]} entrou na sala."
        return "Usuário não encontrado."

    def Sair_da_sala(self, usuario_id):
        # Remove o usuário da lista de ativos
        if usuario_id in self.usuarios_ativos:
            self.usuarios_ativos.remove(usuario_id)
            return f"Usuário {self.usuarios[usuario_id]} saiu da sala."
        return "Usuário não está na sala."

    def Enviar_mensagem(self, usuario_id, mensagem):
        # Adiciona a mensagem à lista de mensagens
        if usuario_id in self.usuarios_ativos:
            self.mensagens.append(f"{self.usuarios[usuario_id]}: {mensagem}")
            return "Mensagem enviada com sucesso."
        return "Usuário não está na sala."

    def Listar_mensagens(self):
        # Retorna todas as mensagens
        return self.mensagens

    def Enviar_mensagem_usuario(self, usuario_id, destinatario_id, mensagem):
        # Envia a mensagem apenas para o destinatário
        if usuario_id in self.usuarios_ativos and destinatario_id in self.usuarios_ativos:
            return f"Mensagem para {self.usuarios[destinatario_id]}: {mensagem}"
        return "Um ou ambos os usuários não estão na sala."

    def Listar_usuarios(self):
        # Retorna a lista de usuários ativos
        return [self.usuarios[usuario_id] for usuario_id in self.usuarios_ativos]

# Cria o servidor XML-RPC
server = SimpleXMLRPCServer(("localhost", 9000))
server.register_instance(ChatServer())

print("Servidor de chat iniciado...")
server.serve_forever()
