FROM node

RUN mkdir -p home/app

COPY . /home/app

WORKDIR /home/app

RUN npm install

#Run this when the container is started
CMD ["node", "src/index.js"]