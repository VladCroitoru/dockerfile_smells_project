FROM node:lts

RUN mkdir /app
WORKDIR /app
ADD package.json /app/
COPY . /app/
RUN npm ci --silent

CMD [ "npm", "run","start" ]
