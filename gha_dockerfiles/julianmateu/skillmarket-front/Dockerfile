FROM node:13-alpine

WORKDIR /app

RUN apk add git

COPY package.json package-lock.json ./

RUN npm install

COPY .eslintignore *.js ./
COPY ./public ./public
COPY ./src ./src

RUN npm run build -- --mode development

EXPOSE 8080

CMD npm run serve
