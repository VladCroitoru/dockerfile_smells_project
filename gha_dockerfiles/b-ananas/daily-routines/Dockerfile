FROM node:14 as development
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000

# RUN npm migrate
# ENTRYPOINT npm run migrate:deploy & npm run start
# CMD [ "npm", "run", "migrate:deploy"]
CMD [ "npm", "run", "start" ]