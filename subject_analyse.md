# ft_transcendence

## Overview : 16 major, 11 minor

=> Everything - launched - single command line - container Docker.

=> Single-page application.

=> latest stable up-to-date version of Google Chrome.

=> minimal 7 major modules required

	• Web
		◦ Major module: Use a Framework as backend => Ruby ou Django
		◦ Minor module: Use a front-end framework or toolkit => Javascript ou Bootstrap 
		◦ Minor module: Use a database for the backend => PostgreSQL 
		◦ Major module: Store the score of a tournament in the Blockchain => Ethereum Solidity

	• User Management
		◦ Major module: Standard user management, authentication, users across tournaments.
		◦ Major module: Implementing a remote authentication.

	• Gameplay and user experience
		◦ Major module: Remote players
		◦ Major module: Multiplayers (more than 2 in the same game).
		◦ Major module: Add Another Game with User History and Matchmaking.
		◦ Minor module: Game Customization Options.
		◦ Major module: Live chat.

	• AI-Algo
		◦ Major module: Introduce an AI Opponent.
		◦ Minor module: User and Game Stats Dashboards

	• Cybersecurity
		◦ Major module: Implement WAF/ModSecurity with Hardened Configuration
		and HashiCorp Vault for Secrets Management.
		◦ Minor module: GDPR Compliance Options with User Anonymization, Local
		Data Management, and Account Deletion.
		◦ Major module: Implement Two-Factor Authentication (2FA) and JWT.

	• Devops
		◦ Major module: Infrastructure Setup for Log Management.
		◦ Minor module: Monitoring system.
		◦ Major module: Designing the Backend as Microservices.

	• Graphics
		◦ Major module: Use of advanced 3D techniques.

	• Accessibility
		◦ Minor module: Support on all devices.
		◦ Minor module: Expanding Browser Compatibility.
		◦ Minor module: Multiple language supports.
		◦ Minor module: Add accessibility for Visually Impaired Users.
		◦ Minor module: Server-Side Rendering (SSR) Integration.

	• Server-Side Pong
		◦ Major module: Replacing Basic Pong with Server-Side Pong and Implementing an API.
		◦ Major module: Enabling Pong Gameplay via CLI against Web Users with API Integration.


## Conception architecturale

1. Architecture Globale

**a. Vue d’Ensemble :
	Frontend : Interface utilisateur (UI) pour l'interaction avec les joueurs.
	Backend : Serveurs qui traitent la logique des jeux, la gestion des utilisateurs, et la communication avec la blockchain.
	Blockchain : Stockage décentralisé des scores des tournois.
	Microservices : Services indépendants pour chaque fonctionnalité majeure (gestion des utilisateurs, jeux, chat, etc.).
	Base de Données : Stockage des données des utilisateurs, des jeux, et autres informations nécessaires.

2. Composants du Backend

**a. Serveur Web :
	Framework : Django ou tout autre framework choisi pour la gestion des requêtes HTTP, l’authentification, et la logique métier.
	APIs : Endpoints RESTful ou GraphQL pour les interactions entre le frontend et le backend.
	Services : Services pour la gestion des jeux, des utilisateurs, et du chat.

**b. Microservices :
	Gestion des Utilisateurs : Authentification, autorisation, gestion des profils.
	Gestion des Jeux : Logique du jeu, matchmaking, score des jeux.
	Chat en Direct : Gestion des messages en temps réel entre les joueurs.
	AI : Service pour l’intelligence artificielle des adversaires.

**c. Base de Données :
	Base de Données Relationnelle : Par exemple, PostgreSQL pour les données structurées comme les profils des utilisateurs et les matchs.
	Base de Données NoSQL : Pour les données non structurées ou semi-structurées, si nécessaire.

**d. Blockchain :
	Contrats Intelligents : Pour la gestion et la vérification des scores de tournois.
	Node Blockchain : Service pour interagir avec la blockchain.

		Exemple Concret:
		
			Imaginons que le backend veuille stocker un score de tournoi sur la blockchain :
			Le joueur termine un match.
			Le backend reçoit les informations du match (joueurs, score, etc.).
			Le backend envoie une transaction à la blockchain via un appel à un contrat intelligent pour enregistrer le score.
			Le contrat intelligent sur la blockchain reçoit la transaction, la valide et stocke les données immuables.
			Le backend reçoit une confirmation (ou un échec) de la transaction et peut ensuite informer le joueur.


3. Architecture Frontend

**a. Framework Frontend :
	Choix du Framework : React, Vue.js, Angular, etc.
	Composants UI : Interface pour les jeux, gestion des utilisateurs, chat, et tableaux de bord.

**b. Communication avec le Backend :
	API Calls : Pour interagir avec les services backend via des appels API.
	Websockets : Pour les fonctionnalités en temps réel comme le chat en direct et les mises à jour des jeux.

4. Infrastructure

**a. Microservices :
	Conteneurisation : Utiliser Docker pour empaqueter les microservices.
	Orchestration : Kubernetes ou Docker Compose pour gérer les déploiements et les mises à l’échelle des services.

**b. Infrastructure de Log Management :
	Outils de Log : ELK Stack (Elasticsearch, Logstash, Kibana) ou des solutions similaires pour la gestion des logs.

**c. Monitoring :
	Outils de Monitoring : Prometheus, Grafana, ou autres outils pour surveiller les performances et la santé de l’application.

5. Sécurité

**a. WAF/ModSecurity :
	Configuration : Pour protéger l'application contre les menaces web courantes.

**b. HashiCorp Vault :
	Gestion des Secrets : Pour stocker et gérer les secrets de manière sécurisée.

**c. Authentification et Autorisation :
	JWT : JSON Web Tokens pour l'authentification et l'autorisation sécurisée.
	2FA : Authentification à deux facteurs pour ajouter une couche supplémentaire de sécurité.


