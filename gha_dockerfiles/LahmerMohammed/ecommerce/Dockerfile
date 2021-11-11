arg NODE_VERSION=14
from node:${NODE_VERSION}

label Creator: "Lahmer Mohammed"

workdir /usr/src/backend

copy package*.json ./

run npm install


copy . .

expose 3000

cmd ["nest","start","--watch"]
