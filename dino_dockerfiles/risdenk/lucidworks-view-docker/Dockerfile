FROM node:6

RUN wget -qO- https://github.com/lucidworks/lucidworks-view/tarball/master | tar zx -C / && mv /lucidworks-lucidworks-view* /lucidworks-view

WORKDIR /lucidworks-view

RUN npm install -g gulp bower
RUN npm install
RUN bower install --allow-root
RUN npm run build

COPY FUSION_CONFIG.js /lucidworks-view/FUSION_CONFIG.js

EXPOSE 3000
ENTRYPOINT ["npm", "start"]

