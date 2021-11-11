FROM node:latest

LABEL maintainer="Merlin Diavova <merlindiavova@amesplash.co.uk>"

WORKDIR /var/www/html

ARG uid=999

RUN npm i -g @adonisjs/cli adonisdocker

RUN usermod -u $uid node