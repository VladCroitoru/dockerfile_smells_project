FROM node

RUN wget https://github.com/viktorhajer/darts-scoreboard-ng/archive/refs/heads/master.zip
RUN unzip master.zip

WORKDIR /darts-scoreboard-ng-master

RUN npm install -g @angular/cli
RUN npm i @angular-devkit/build-angular
RUN ng build

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0", "--disable-host-check"]