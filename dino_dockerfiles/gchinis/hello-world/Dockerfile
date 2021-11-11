FROM node:9


COPY package.json /home/node
COPY app.js /home/node

WORKDIR /home/node
RUN ["npm", "install"]

EXPOSE 3000

CMD ["npm", "start"]