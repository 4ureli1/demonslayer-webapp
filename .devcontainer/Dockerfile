# Utilise une image officielle de Python
FROM python:3.12-slim

# Configure l'utilisateur et le dossier de travail
WORKDIR /workspace

# Installe les dépendances système
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copie et installe les dépendances Python
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port pour Flask
EXPOSE 5000

# Commande par défaut
CMD ["python", "app.py"]
