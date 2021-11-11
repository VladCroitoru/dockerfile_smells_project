FROM iojs:2.0.2

MAINTAINER Jon Dotsoy <hi@jon.soy>


# Create the folder app
RUN mkdir /app


# install Sails
RUN npm install -g sails@0.11.0

VOLUME ["/app"]

WORKDIR /app

EXPOSE 1337
EXPOSE 80
EXPOSE 447
