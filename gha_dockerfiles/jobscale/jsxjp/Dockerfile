FROM node:buster-slim
SHELL ["bash", "-c"]
WORKDIR /home/node
COPY . .
RUN npm i --production && chown -R node. . && mv db.example db
USER node
CMD ["npm", "start"]
