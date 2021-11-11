# ref. http://jdlm.info/articles/2016/03/06/lessons-building-node-app-docker.html

FROM node:6.11.2

RUN useradd --user-group --create-home --shell /bin/false app \
    && npm i -g -s pm2

ENV HOME=/home/app

USER root
COPY . $HOME/app
COPY nginx.conf /etc/nginx/sites-enabled/
RUN chown -R app:app $HOME/*

USER app
WORKDIR $HOME/app
RUN npm i -s && npm cache clean

# CMD ["service", "nginx", "start"]