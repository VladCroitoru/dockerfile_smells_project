ARG PORT=80

FROM node:lts-alpine

RUN apk --update add\
    bash\
    git

WORKDIR /var/www

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 80

CMD bin/boot
