FROM node:slim

RUN mkdir -p /var/api
COPY . /var/api
WORKDIR /var/api
RUN npm install

ENV PORT 3000
EXPOSE $PORT

CMD ["npm", "start"]
