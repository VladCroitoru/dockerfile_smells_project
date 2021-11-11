FROM node:8.9

# set debian to non-interactive mode
ENV DEBIAN_FRONTEND noninteractive

LABEL maintainer="Ivan de la Beldad Fernandez <ivandelabeldad@gmail.com>"

EXPOSE 10000

COPY . /app

WORKDIR /app

# install npm dependencies
RUN npm install --production --silent

CMD [ "node", "src/main.js" ]
