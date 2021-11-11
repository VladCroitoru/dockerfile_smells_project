FROM node:latest

ENV HOME /root
WORKDIR /root

COPY . .

RUN npm install

EXPOSE 8000

CMD ["npm", "start"]
