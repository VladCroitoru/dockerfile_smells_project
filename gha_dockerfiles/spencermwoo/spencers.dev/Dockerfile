# escape=`
# syntax=docker/dockerfile:1
FROM node:12 AS build
WORKDIR /app

COPY package* ./
RUN npm i

EXPOSE 3000
EXPOSE 3001

CMD ["npx", "@11ty/eleventy", "--serve", "--port=3000"]