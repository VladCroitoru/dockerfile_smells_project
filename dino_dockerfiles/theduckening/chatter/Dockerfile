FROM node:argon

RUN useradd --user-group --create-home --shell /bin/false app &&\
    npm install --global npm@3.7.5
ENV HOME=/home/app

COPY . $HOME/app
RUN chown -R app:app $HOME/*

USER app

WORKDIR $HOME/app
RUN npm install --production && npm cache clean
EXPOSE 9999
CMD ["npm", "start"]
