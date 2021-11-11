FROM node:latest
RUN apt-get update && apt-get -y install
RUN mkdir /discordBot
WORKDIR /discordBot
RUN git clone https://github.com/Iansutherland/MaximusBot.git maximus
WORKDIR maximus
COPY secret.json ./secret.json
RUN npm install
CMD ["node", "myBot.js"]