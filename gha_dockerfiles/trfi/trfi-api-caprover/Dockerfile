FROM node:14.15.0

WORKDIR /app

COPY *.json /app/

RUN npm ci

COPY . /app/

EXPOSE 3000

CMD ["npm", "start"]