# Docker file pour un serveur web et le jeu 2048

# Basé sur la dernière image de nginx, https://hub.docker.com/_/nginx
FROM nginx

# L'image est basée sur debian, les commandes apt fonctionnent
RUN apt update

# Afin de pouvoir récupérer le code de 2048, nous avons besoin de git
RUN apt -y install git

# La commande WORKDIR permet de définir le dossier de travail
WORKDIR /usr/share/nginx

# On estime que les fichiers par défaut ne sont pas nécessaire
RUN rm -rf html

# On clone le code de l'application dans le répertoire qui est «servi» par
# nginx, notre serveur web, qui a précédemment été supprimé
RUN git clone https://github.com/gabrielecirulli/2048.git /usr/share/nginx/html

# On expose le port 80, port par défaut des applications web
EXPOSE 80
