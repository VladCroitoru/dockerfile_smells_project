FROM mhart/alpine-node:5.10.1

WORKDIR /src
ADD package.json .
RUN npm install
ADD . .

EXPOSE 8080
CMD ["node", "app.js"]

