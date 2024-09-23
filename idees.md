? -> pas sur de l'integrer dans le projet

I- Les principaux pages web :

	1. Page d'accueil / Page de démarrage
		
			*interface utilisateur : 
				-match rapide : sans creation de compte et enregistrements de donnees.
			?	-help : guide d'utilisation de commandes clavier. (ex: un petit cadran un peu transparent qui s'affiche de haut en bas avec les commandes et un croix pour le fermer)
				-connexion
				-subscribe

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

	3. page de connexion

			*interface utilisateur :

				-Menu : retour page de demarrage.
				-formule de connexion :
					Nom d'utilisateur
					Mot de passe
				?	Mot de passe oublie
					[Connect]

	3. Page de jeu (Pong en temps réel) : 2 types (match rapide ou match connecte)
			
			-affichage : les paddles, la balle, et le score en temps réel.

	4. Page d'accueil du compte personnel du joueur

			-deconnexion
			-setting : modifier le profil
			-ajouter un ami : 
			-liste d'amis :
				-status 
				-chat
				-invitation de jeu
			-Match History
		?	-Classement : redirection

	5. Page de Match History :
			-Statistiques de jeu : nombre de victoires, défaites.
			-History : contre qui (cliquable pour voir son profil), quand, victoire ou defaite. 

II- Les APIs necessaires :

	* Authentification et gestion des utilisateurs :

		- Création de comptes utilisateurs (ex: POST /api/users/signup/).

		- Connexion / déconnexion (ex: POST /api/users/login/) : Gérer l'authentification avec un système de jeton (JWT). 

		- Validation des sessions (ex: GET /api/users/session/) : 
				
				1. Validation de Connexion
					Cela concerne la vérification des identifiants de l'utilisateur lors de la connexion initiale. Si les identifiants sont corrects, une session est créée (ou un token est généré), permettant à l'utilisateur d'accéder à l'application.
				2. Accès aux Ressources Protégées
					Après la connexion, à chaque requête que l'utilisateur fait pour accéder à des ressources protégées (comme des pages privées, des API sécurisées, etc.), le système doit valider la session ou le token pour s'assurer que l'utilisateur est toujours authentifié et que sa session est active.
					Si la validation échoue (par exemple, si la session a expiré ou si le token est invalide), l'accès à ces ressources doit être refusé, et l'utilisateur doit être redirigé vers la page de connexion ou informé qu'il doit se reconnecter.

	* Gestion des parties :

		- Match rapide (sans compte) : Créer une API pour lancer une partie sans créer de compte, peut-être en générant un identifiant temporaire pour le joueur (ex: POST /api/game/quickmatch/).
		
		- Enregistrement des parties : Pour les utilisateurs connectés, créer une API qui enregistre le résultat des parties dans la base de données (ex: POST /api/game/results/).
		
		- Historique des matchs : Permettre aux utilisateurs connectés de récupérer l’historique de leurs matchs (ex: GET /api/game/history/).

	* Statistiques des joueurs
		
		- Suivi des statistiques : Stocker les données des matchs (victoires, défaites, scores) et les rendre accessibles via une API pour les afficher sur le profil utilisateur (ex: GET /api/stats/player/{user_id}/).
		
	?	- Classements : Implémenter un système de classement des meilleurs joueurs (ex: GET /api/stats/leaderboard/).

	* Gestion des amis :

		- Ajouter/retirer des amis : API pour gérer les demandes d’amitié entre joueurs (ex: POST /api/friends/add/, DELETE /api/friends/remove/).
		
		- Lister les amis : Permettre à un utilisateur de voir sa liste d’amis pour jouer contre eux (ex: GET /api/friends/).

	* Administration et sécurité :
		
	?	- Protection contre les abus : Mise en place de limites de requêtes (rate-limiting) et vérification des requêtes (ex: protection contre les attaques DDoS).

	* Système de notifications :

		- Notifications en temps réel : Informer les joueurs en temps réel lorsqu'un ami les invite à une partie ou lorsqu'un nouveau match est disponible (via WebSockets ou des services comme Firebase Cloud Messaging).
		
		- Notifications par email : Envoyer des emails automatiques pour des événements spécifiques (ex: confirmation de compte, résultats de match, demandes d’amitié).

	* Paramètres du joueur :

		- Personnalisation du profil : API pour gérer les paramètres du compte utilisateur, comme changer le pseudo, l’avatar (ex: PUT /api/user/settings/).

?	* Gestion des tournois :

		- Organisation de tournois : API pour créer et gérer des tournois avec des groupes d'utilisateurs, où le système attribue automatiquement les matchs (ex: POST /api/tournament/create/).
		
		- Suivi des résultats de tournoi : API pour suivre la progression des joueurs dans un tournoi et afficher les résultats en temps réel (ex: GET /api/tournament/{id}/results/).
