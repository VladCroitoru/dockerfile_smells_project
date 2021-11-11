FROM node:16-buster-slim

WORKDIR /home/node
COPY package*.json .
RUN npm install --production

# Bundle app source code
COPY --chown=node . .

# && usermod -aG sudo node
USER node
EXPOSE 9000

CMD ["node", "index.js"]

# docker build -t migutak/callscheduller:5.7.5 .