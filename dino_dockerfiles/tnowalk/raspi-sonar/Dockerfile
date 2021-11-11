FROM resin/raspberrypi3-node:slim

WORKDIR /opt/raspi-sonar

COPY package.json .

CMD ["npm", "install"]

COPY . .

CMD ["npm", "start"]
