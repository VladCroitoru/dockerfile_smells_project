FROM node:argon

RUN apt-get update && apt-get install -y --no-install-recommends ruby ruby-sass

RUN npm install -g bower grunt-cli

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN useradd twitchteam && echo "twitchteam:twitchteam" | chpasswd
RUN mkdir -p /home/twitchteam && chown -R twitchteam:twitchteam /home/twitchteam && chown -R twitchteam:twitchteam /usr/src/app
USER twitchteam

RUN npm -q install

RUN bower -q install

RUN mkdir -p /usr/src/app/dist/scripts

EXPOSE 9000
CMD [ "grunt", "serve:dist" ]
