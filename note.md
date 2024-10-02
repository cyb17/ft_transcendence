## Ce qu'il faut savoir sur Django : 

1. models.py :
	
	- **django.db.models.Model** : base basique, a utiliser pour creer un modele personnalise.
	- **class Meta** : permet de configurer des options supplémentaires comme le nom de la table, l’ordre par défaut, etc.
	- **django.db.modles.Manager** : basique, a utiliser pour creer un manager personnalise.
	- **modele abstrait**: ne creer pas de db, utiliee seulement pour que d'autres soient herite de lui(ses attributs et fonctions).
	- **modele proxy** : un modele qui herite le modele de bases pour pourvoir ajouter ou modifier ses comportement.

	chaque modele possede obligatoirement un manager, soit par defaut soit personnalise.

2. views.py:

	- **Vue basée sur des fonctions (Function-Based Views, FBV)**.

	- **Vue basée sur des classes (Class-Based Views, CBV)** : 
		- **from django.views import View**: class basique de view
		- **from django.views.generic import ListView** : class generic de view, pour des view de simple taches, qui en necessitent par de personnalisations.
		- **from django.views.generic.edit import UpdateView**	: pour les operations CRUD.
		- **from django.contrib.auth.mixins import LoginRequiredMixin** : class mixins, souvent utilise en combinaison avec generic view pour avoir aussi les methodes de class mixins.

		| Méthode                                   |Description                                                                   |
		|-------------------------------------------|------------------------------------------------------------------------------|
		| FBV (Function-Based View)                 | Fonction simple qui prend une requête et renvoie une réponse.                |
		| CBV (Class-Based View)                    | Vue orientée objet qui offre plus de flexibilité et de réutilisation.        |
		| GCBV (Generic Class-Based View)           | Vues prédéfinies pour gérer les tâches courantes comme les listes et détails.|
		| CRUD Views (Create/Update/Delete)         | Vues génériques spécialisées pour les opérations CRUD.                       |
		| Mixins                                    | Combine des comportements dans des CBV pour une meilleure modularité.        |
		| Django REST Framework (DRF)               | Crée des API REST avec des vues basées sur des fonctions ou des classes.     |
		| Viewsets (DRF)                            | Combine plusieurs actions (CRUD) dans une seule vue pour une API REST.       | 


## Ce qu'il faut savoir sur Django REST Framework :


1. views.py : 

	- **from rest_framework.decorators import api_view**
	- **from rest_framework.views import APIView**
	- **from rest_framework.generics import UpdateAPIView**
	- **from rest_framework import viewsets**

	| Méthode              	 | Description                 	                      			|
	|------------------------|--------------------------------------------------------------|
	| **FBV**                | Vues basées sur des fonctions simples.             			|
	| **APIView**            | Vues basées sur des classes avec des méthodes HTTP définies. |
	| **GenericAPIView**     | Fournit des fonctionnalités génériques pour les vues.        |	
	| **ModelViewSet**       | Combine toutes les opérations CRUD dans une seule classe.    |

	Resume de l'heritage:

	BaseAPIView
   	└── APIView
       └── GenericAPIView
           ├── CreateModelMixin
           ├── RetrieveModelMixin
           ├── UpdateModelMixin
           └── DestroyModelMixin
               └── ModelViewSet


2. router : 

	from django.urls import path, include
	from rest_framework.routers import DefaultRouter
	from .views import UserViewSet

	router = DefaultRouter()
	router.register(r'users', UserViewSet)

	urlpatterns = [
	    path('api/', include(router.urls)),
	]

	**UserViewSet herite de ModelViewSet, rassemble les operations CRUD**
	**Le routeur prend en charge la création de routes pour toutes les opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) en une seule étape, simplifiant ainsi la gestion des routes dans l'application.** 

3. Serailizers : 

	**sont utilisés pour convertir des instances de modèles en formats JSON (ou d'autres formats) et pour valider les données entrantes.** 

