FROM alpine:3.14
EXPOSE 3000/tcp
EXPOSE 19713/tcp
ADD src/ /home
WORKDIR /home
RUN apk add --no-cache npm yarn nodejs-current
RUN npm i -g concurrently ts-node nodemon
RUN npm i
WORKDIR /home/site
RUN yarn install
WORKDIR /home
RUN mkdir temp
ENTRYPOINT npm start