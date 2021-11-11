FROM node:10.15.1
WORKDIR /app
EXPOSE 25
RUN apt-get update -qq
RUN apt-get install -y build-essential spamassassin spamc
RUN npm install -g mailin
CMD mailin --webhook $WEBHOOK_URL
