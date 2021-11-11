FROM node

RUN apt-get update
RUN apt-get install -y build-essential

RUN mkdir -p /usr/app/
COPY ./package.json /usr/app/package.json
WORKDIR /usr/app
RUN npm install 
COPY . /usr/app/
RUN npm run build

CMD ["npm", "start"]
