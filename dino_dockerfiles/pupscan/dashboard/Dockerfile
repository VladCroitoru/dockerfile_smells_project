FROM kkarczmarczyk/node-yarn:latest
MAINTAINER thibaut.mottet@pupscan.fr

WORKDIR /workspace
COPY . .
RUN yarn install
EXPOSE 5000

CMD ["node", "app.js"]

