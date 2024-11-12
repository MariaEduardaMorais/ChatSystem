import xmlrpc.client

class ChatClient:
    def __init__(self):
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:9000")
        self.usuario_id = None

    def ingressar_no_sistema(self):
        nome_do_usuario = input("Digite seu nome de usuário: ")
        self.usuario_id = self.proxy.Ingressar_no_sistema(nome_do_usuario)
        print(f"Usuário cadastrado com ID: {self.usuario_id}")

    def entrar_na_sala(self):
        if self.usuario_id:
            response = self.proxy.Entrar_na_sala(self.usuario_id)
            print(response)
        else:
            print("Você precisa se cadastrar primeiro!")

    def sair_da_sala(self):
        if self.usuario_id:
            response = self.proxy.Sair_da_sala(self.usuario_id)
            print(response)
            self.usuario_id = None
        else:
            print("Você precisa estar na sala para sair!")

    def enviar_mensagem(self):
        if self.usuario_id:
            mensagem = input("Digite a mensagem que deseja enviar: ")
            response = self.proxy.Enviar_mensagem(self.usuario_id, mensagem)
            print(response)
        else:
            print("Você precisa estar na sala para enviar mensagens!")

    def listar_mensagens(self):
        if self.usuario_id:
            mensagens = self.proxy.Listar_mensagens()
            print("Mensagens no chat:")
            for msg in mensagens:
                print(msg)
        else:
            print("Você precisa estar na sala para ver as mensagens!")

    def enviar_mensagem_usuario(self):
        if self.usuario_id:
            destinatario_id = input("Digite o ID do destinatário: ")
            mensagem = input("Digite a mensagem privada: ")
            response = self.proxy.Enviar_mensagem_usuario(self.usuario_id, destinatario_id, mensagem)
            print(response)
        else:
            print("Você precisa estar na sala para enviar mensagens privadas!")

    def listar_usuarios(self):
        if self.usuario_id:
            usuarios = self.proxy.Listar_usuarios()
            print("Usuários ativos na sala:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("Você precisa estar na sala para listar os usuários!")

    def exibir_menu(self):
        while True:
            print("\n--- Menu de Chat ---")
            print("1. Ingressar no sistema")
            print("2. Entrar na sala")
            print("3. Sair da sala")
            print("4. Enviar mensagem")
            print("5. Listar mensagens")
            print("6. Enviar mensagem para outro usuário")
            print("7. Listar usuários ativos")
            print("8. Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.ingressar_no_sistema()
            elif opcao == "2":
                self.entrar_na_sala()
            elif opcao == "3":
                self.sair_da_sala()
            elif opcao == "4":
                self.enviar_mensagem()
            elif opcao == "5":
                self.listar_mensagens()
            elif opcao == "6":
                self.enviar_mensagem_usuario()
            elif opcao == "7":
                self.listar_usuarios()
            elif opcao == "8":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    client = ChatClient()
    client.exibir_menu()
