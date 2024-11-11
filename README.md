# Distributed Systems Project

## Chat System Using RPC

### Project Overview

This project involves the development of a distributed chat system using **RPC** (Remote Procedure Call) technology. The client envisions a modular chat room where multiple users can join, exchange messages, and interact in real-time. The system includes the following key methods:

### System Methods

1. **Join_System**: Allows a user to request registration in the system using their name. This method assigns a unique ID to the user.
2. **Enter_Room**: Allows a user (identified by their unique ID) to join the chat room.
3. **Leave_Room**: Allows a user (identified by their unique ID) to leave the chat room.
4. **Send_Message**: Allows a user to send a message using their unique ID.
5. **List_Messages**: Allows a user to view all messages posted in the chat room.
6. **Send_Message_To_User**: Allows a user to send a private message to a specific user. Only the two users involved can view the message.
7. **List_Users**: Allows a user to get a list of active users in the chat room.

### How to Use

1. Clone the repository and set up the development environment.
2. Register in the chat system using the `Join_System` method.
3. Use `Enter_Room` to join the chat room and start participating in conversations.
4. Use `Send_Message` to broadcast a message to everyone in the chat.
5. To send a private message to a specific user, use `Send_Message_To_User`.
6. View all current messages in the chat using `List_Messages`.
7. Check the active users in the chat room with `List_Users`.
8. When you’re done, you can exit the room with `Leave_Room`.

### Technologies Used

- **RPC**
- **Distributed Systems Architecture**

---

# Projet de Systèmes Distribués

## Système de Chat Utilisant RPC

### Présentation du Projet

Ce projet consiste en la création d’un système de chat distribué utilisant la technologie **RPC** (Remote Procedure Call). Le client imagine une salle de discussion modulaire où plusieurs utilisateurs peuvent rejoindre, échanger des messages et interagir en temps réel. Le système comprend les méthodes clés suivantes :

### Méthodes du Système

1. **Ingressar_no_sistema** : Permet à un utilisateur de demander son enregistrement dans le système en utilisant son nom. Cette méthode assigne un identifiant unique à l’utilisateur.
2. **Entrar_na_sala** : Permet à un utilisateur (identifié par son identifiant unique) de rejoindre la salle de discussion.
3. **Sair_da_sala** : Permet à un utilisateur (identifié par son identifiant unique) de quitter la salle de discussion.
4. **Enviar_mensagem** : Permet à un utilisateur d’envoyer un message en utilisant son identifiant unique.
5. **Listar_mensagens** : Permet à un utilisateur de consulter tous les messages publiés dans la salle de discussion.
6. **Enviar_mensagem_usuario** : Permet à un utilisateur d’envoyer un message privé à un autre utilisateur. Seuls les deux utilisateurs impliqués peuvent voir le message.
7. **Listar_usuarios** : Permet à un utilisateur d’obtenir la liste des utilisateurs actifs dans la salle de discussion.

### Instructions d’Utilisation

1. Clonez le dépôt et configurez l'environnement de développement.
2. Inscrivez-vous dans le système de chat avec la méthode `Ingressar_no_sistema`.
3. Utilisez `Entrar_na_sala` pour rejoindre la salle de discussion et commencer à participer aux conversations.
4. Utilisez `Enviar_mensagem` pour envoyer un message à tous les utilisateurs.
5. Pour envoyer un message privé à un utilisateur spécifique, utilisez `Enviar_mensagem_usuario`.
6. Consultez tous les messages actuels dans la salle de discussion avec `Listar_mensagens`.
7. Vérifiez les utilisateurs actifs dans la salle de discussion avec `Listar_usuarios`.
8. Lorsque vous avez terminé, vous pouvez quitter la salle avec `Sair_da_sala`.

### Technologies Utilisées

- **RPC**
- **Architecture de Systèmes Distribués**
