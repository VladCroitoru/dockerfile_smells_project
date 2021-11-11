FROM node:16.3-alpine

WORKDIR /usr/share/html

# Nur das frontend, backend und die build.sh werden benötigt
COPY frontend/ frontend/
COPY backend/ backend/
COPY build.sh ./

# Die build.sh baut aus frontend und backend den "build" Ordner
RUN ./build.sh

# Frontend und backend nehmen nun nur noch unnötig Platz weg, darum werden sie gelöscht
RUN rm -rf frontend/ backend/

# Der Port 5000 wird aus dem docker container freigegeben
EXPOSE 5000

# Zum Starten des Servers die index.js Datei ausführen
CMD [ "node", "build/src/index.js" ]
