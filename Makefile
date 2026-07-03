SHELL := /bin/sh

BACKEND_DIR := housing-api
FRONTEND_DIR := housing-api-frontend
PIPELINE_DIR := ml-pipeline
BACKEND_URL ?= http://localhost:8000

.PHONY: help local codespaces backend-up backend-down frontend pipeline

codespaces: BACKEND_URL := https://verbose-tribble-x764p9jr76p2v4r9-8000.app.github.dev/

help:
	@printf '%s\n' \
		'  ' \
		'Commande disponibles:' \
		'  make help        	Afficher cette aide' \
		'  ' \
		'  HOUSING-API' \
		'  make local       	Lancer le backend et le frontend en local' \
		'  make codespaces  	Lancer le backend et le frontend pour Codespaces' \
		'  make backend-up  	Démarrer que le backend' \
		'  make backend-down	Arrêter le backend' \
		'  make frontend    	Démarrer que le frontend' \
		'  ' \
		'  ML-PIPELINE' \
		'  make pipeline    	Lancer la pipeline ML locale' \
		'  '

local:
	@set -e; \
	cd $(BACKEND_DIR) && docker compose up --build -d; \
	trap 'cd $(BACKEND_DIR) && docker compose down' INT TERM EXIT; \
	cd ../$(FRONTEND_DIR) && BACKEND_URL=$(BACKEND_URL) streamlit run app.py

codespaces:
	@set -e; \
	cd $(BACKEND_DIR) && docker compose up --build -d; \
	trap 'cd $(BACKEND_DIR) && docker compose down' INT TERM EXIT; \
	cd ../$(FRONTEND_DIR) && BACKEND_URL=$(BACKEND_URL) streamlit run app.py

backend-up:
	cd $(BACKEND_DIR) && docker compose up --build -d

backend-down:
	cd $(BACKEND_DIR) && docker compose down

frontend:
	cd $(FRONTEND_DIR) && BACKEND_URL=$(BACKEND_URL) streamlit run app.py

pipeline:
	cd $(PIPELINE_DIR) && python run_pipeline.py
