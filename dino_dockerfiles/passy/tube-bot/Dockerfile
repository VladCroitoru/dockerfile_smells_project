FROM node:6.3.1
MAINTAINER Pascal Hartig <phartig@rdrei.net>

ENV PORT 5000

RUN useradd --user-group --create-home --shell /bin/false app
RUN mkdir -p /app
COPY package.json bower.json *.js /app/
COPY src /app/src
RUN chown -R app:app /app

USER app
WORKDIR /app
RUN npm install
RUN npm run build

VOLUME "/app/config"
EXPOSE $PORT

# vim:tw=0:

