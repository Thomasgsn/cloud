#

1. Pourquoi faut-il sauvegarder le modèle entraîné ?
L'entraînement d'un modèle demande généralement beaucoup de temps et de puissance de calcul. Sauvegarder le modèle permet de conserver ses poids et ses apprentissages pour pouvoir le réutiliser instantanément, sans avoir à tout recalculer à chaque fois que l'on veut faire une prédiction.

2. Pourquoi le modèle est-il chargé au démarrage de l'API ?
Il est chargé au démarrage pour être stocké en mémoire vive (RAM) une seule et unique fois. Si le modèle était chargé à chaque fois qu'un utilisateur fait une requête sur l'endpoint `/predict`, cela ralentirait drastiquement le temps de réponse de l'API.

3. Pourquoi utilise-t-on 0.0.0.0 dans Docker ?
L'adresse `127.0.0.1` restreint les connexions à l'intérieur même du conteneur. En utilisant `0.0.0.0`, on indique à l'application d'accepter les connexions provenant de toutes les interfaces réseau, ce qui permet à ta machine hôte d'accéder au port exposé par le conteneur.

4. Quelle est la différence entre entraîner un modèle et servir un modèle ?

* **Entraîner un modèle** : C'est la phase d'apprentissage où l'algorithme analyse un jeu de données historiques pour trouver des modèles mathématiques et ajuster ses paramètres.
* **Servir un modèle (inférence)** : C'est la phase de mise en production où le modèle (déjà entraîné) est mis à disposition, souvent via une API, pour recevoir de nouvelles données inédites et renvoyer des prédictions en direct.

5. Pourquoi Docker est-il utile pour déployer une API ML ?
Docker permet d'encapsuler l'API, le modèle, la version exacte de Python et toutes les dépendances dans un environnement isolé appelé conteneur. Cela garantit que l'application s'exécutera de manière strictement identique, que ce soit sur ton ordinateur local, sur celui d'un collègue ou sur un serveur de production (éliminant le fameux problème du "ça marche sur ma machine").
