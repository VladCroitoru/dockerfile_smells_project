FROM node:16

# Create app directory
WORKDIR /usr/src/parkirmana

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

COPY prisma ./prisma/

RUN npm install

COPY . .

#RUN npm install pm2 -g

EXPOSE 8181

CMD [ "prisma", "generate" ]

CMD [ "node", "main.js" ]