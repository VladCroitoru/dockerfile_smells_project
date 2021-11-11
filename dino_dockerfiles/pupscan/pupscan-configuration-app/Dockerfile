FROM kkarczmarczyk/node-yarn:latest
MAINTAINER thibaut.mottet@pupscan.fr

WORKDIR /workspace
COPY . .
RUN yarn install
EXPOSE 8080

CMD ["yarn", "start"]