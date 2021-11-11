FROM hypriot/rpi-node:4

RUN mkdir -p /app
WORKDIR /app
COPY /package.json /app
RUN npm install
COPY /src/* /app/
COPY /src/security/* /app/security/
EXPOSE 8080

CMD [ "node", "index.js" ]
