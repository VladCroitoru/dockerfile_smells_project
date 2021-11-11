FROM node
WORKDIR /app
EXPOSE 3000

COPY package.json /app/package.json
RUN npm install

COPY . /app
RUN npm run build

CMD npm start