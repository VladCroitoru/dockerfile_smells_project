FROM node

WORKDIR /usr/app

COPY package.json ./

#RUN apt update && apt upgrade -y

RUN yarn

COPY . .

EXPOSE 3333

CMD ["yarn", "dev"]
