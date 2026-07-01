# Projets Cloud M1 IA

[Lien vers le Codespaces](https://verbose-tribble-x764p9jr76p2v4r9.github.dev/)

[README HOUSING-API](/housing-api/README.md)\
[README FRONTEND HOUSING-API](/housing-api-frontend/README.md)

## Lancement

### Vérifier que le Codespaces est à jour

```bash
git pull
```

### Lancement sur différent environnement

- `make help` pour voir toutes les commandes custom
- `make local` lance le backend Docker puis le frontend Streamlit avec `BACKEND_URL=http://localhost:8000`
- `make codespaces` fait la même chose avec `BACKEND_URL=https://verbose-tribble-x764p9jr76p2v4r9-8000.app.github.dev/`

**WARN:** vérifier la visibilité des ports

`Ctrl + C` ferme uniquement le front.\
Pour fermer le back, lancer la commande `make backend-down`.
