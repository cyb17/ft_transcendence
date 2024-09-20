Les pages web necessaires :

*tache globale : le design de chaque page

1. Page d'accueil / Page de démarrage
	
		*interface utilisateur : 
			-match rapide : redirection vers la page de jeu, sans creation de compte et enregistrements de donnees.
			-help : guide d'utilisation de commandes clavier. 
			-connexion ： redirection
			-subscribe :  redirection

		*taches a faire : 
			-mettre en place les redirections des pages concernees.
			-creation du cadran de help. (ex: un petit cadran un peu transparent qui s'affiche de haut en bas avec les commandes et un croix pour le fermer)

2. page de souscription

		*interface utilisateur :
			
			-Menu : retour page de demarrage
			-formule de souscription :
				Nom d'utilisateur (Unique)
				E-mail
				Mot de passe
				Confirmez le mot de passe
				Avatar :           [Parcourir…]
				[Subscrib]   (Bouton d'envoi)

		*taches a faire : 
			-2FA et JWT  (reste a se renseigner pour avoir plus d'idees)
			-[hasher les MDP (sel, poivre, nb d'iteration) avant leur stockage](https://www.vaadata.com/blog/fr/comment-stocker-mots-de-passe-de-maniere-securisee-base-de-donnees/)

					1- A user creates an account
					2- Their password is hashed and stored on the database

			-enregistrer l'utilisateur dans database.

3. page de connexion

			-Menu : retour page de demarrage.
			-formule de connexion :
				Nom d'utilisateur
				Mot de passe
			?	Mot de passe oublie
				[Connect]

		*taches a faire : 

			-2FA and JWT.

					1- When the user attempts to log in, the hash of their entered password is compared to the has stored in the database
					2- If the hashes match, the user can access the account.
					3- If not, a generic error message is sent back such as “Entered invalid credentials” so hackers can’t trace the error to the username or password specifically.

3. Page de jeu (Pong en temps réel) : 2 types (match rapide ou match connecte)
		
		-affichage : les paddles, la balle, et le score en temps réel.
		Fonctions :
		Mécaniques de jeu Pong.
		Interaction en temps réel avec un autre joueur via WebSocket ou une autre technologie de synchronisation en temps réel.

4. Page d'accueil du compte personnel du joueur

		-deconnexion
		-setting : modifier le profil
		-ajouter un ami : 
		-liste d'amis :
			-status 
			-chat
			-invitation de jeu
		-Match History : redirection
	?	-Classement : redirection

5. Page de Match History :
		-Statistiques de jeu : nombre de victoires, défaites.
		-History : contre qui (cliquable pour voir son profil), quand, victoire ou defaite. 

		