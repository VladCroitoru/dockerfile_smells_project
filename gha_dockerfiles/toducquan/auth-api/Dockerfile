FROM node:lts-alpine

WORKDIR /app

COPY package.json yarn.* ./

COPY . ./

RUN npm install

# EXPOSE 3333

ENTRYPOINT ["node","ace","serve","--watch"]