#FROM node:14 as build
FROM node:buster as build
WORKDIR /app
RUN yarn install --production=true
COPY . .

#FROM node:14-alpine
FROM node:buster
COPY --from=build /app /

#EXPOSE 3000 4000
CMD [ "node", "bot.js" ]