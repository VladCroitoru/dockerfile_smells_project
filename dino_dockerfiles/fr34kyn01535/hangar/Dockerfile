FROM node:carbon

WORKDIR /usr/src/hangar
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 8080

ENV PORT=8080
ENV DB_HOST=localhost
ENV DB_USER=hangar
ENV DB_PASSWORD=
ENV DB_NAME=hangar

CMD [ "npm", "start" ]