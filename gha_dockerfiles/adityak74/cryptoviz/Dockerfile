FROM mhart/alpine-node:16

WORKDIR /app
RUN apk add --no-cache make gcc g++ python3
COPY . .
RUN npm install
EXPOSE 5000
CMD [ "npm", "start" ]
