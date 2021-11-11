FROM mhart/alpine-node:base-8


WORKDIR /src
ADD . .

# WORKDIR /src
ADD package.json src/package.json
# RUN npm install

EXPOSE 8080
CMD ["node", "server.js"]
