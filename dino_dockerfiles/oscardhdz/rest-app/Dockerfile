FROM node:alpine

RUN mkdir -p /home/api

WORKDIR /home/api

COPY . .

RUN npm install

ENV NODE_ENV=prod
ENV VALIDATE_DB=ON
ENV DB_CLIENT=sqlite3
ENV DB_FILE=database

CMD ["npm", "start"]
