# Réponses

1. Différence entre CI et CD

La CI automatise l'intégration et la vérification du code à chaque modification.
La CD automatise la mise à disposition d'un artefact validé, jusqu'au déploiement ou à une étape prête à déployer.

2. Rôle d'un trigger

Un trigger lance automatiquement la pipeline lorsqu'un événement survient, par exemple un push, une merge request ou une exécution planifiée.

3. Pourquoi utiliser YAML

YAML rend la pipeline lisible, déclarative et facile à versionner. On sépare la description du workflow de son exécution.

4. Avantages de l'automatisation en ML

Elle réduit les erreurs manuelles, accélère les itérations, rend les résultats reproductibles et facilite le suivi qualité des modèles.

5. Risque d'un déploiement sans validation

On peut mettre en production un modèle moins bon que la version précédente, ou un modèle biaisé / cassé, avec un impact direct sur les utilisateurs.
