from node:5

run mkdir /app
workdir /app
add ./package.json /app/package.json
run npm install --production -d
add . /app

expose 4000

cmd node server.js
