FROM node:16
WORKDIR /app
COPY package.json ./
COPY ./ ./
RUN npm run init-setup 
CMD [ "npm", "run", "test-ci" ]
