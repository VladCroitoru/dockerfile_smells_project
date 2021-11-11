FROM node:14.9.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt update && apt dist-upgrade -y
RUN apt install git

COPY . /usr/src/app/
RUN npm install
RUN npm run build

EXPOSE 3000

CMD [ "npm", "run", "serve" ]
