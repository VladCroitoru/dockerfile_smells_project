FROM node:12.16.1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y make gcc build-essential

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install -g @angular/cli@9.1.0

COPY ./ ./

EXPOSE 4200

CMD ["npm", "run", "env"]
CMD ["ng", "serve", "--host", "0.0.0.0"]
