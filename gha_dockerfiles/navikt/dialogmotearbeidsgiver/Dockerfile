FROM node
LABEL org.opencontainers.image.source=https://github.com/navikt/dialogmotearbeidsgiver

WORKDIR /usr/src/app
COPY . .

RUN npm install express path mustache-express promise prom-client dotenv jsdom request

EXPOSE 8080

CMD ["npm", "start"]
