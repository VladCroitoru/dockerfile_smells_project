FROM node
MAINTAINER Norbert Schultz <norbert.schultz@reactivecore.de>

COPY src /app
RUN cd /app; npm install
CMD ["node", "/app/main.js"]

EXPOSE 25
