FROM node

EXPOSE 3000
WORKDIR /app

COPY package.json /app
RUN npm install

COPY index.js scriptures.db /app/
RUN npm run build

CMD ["npm", "run", "start:production"]
