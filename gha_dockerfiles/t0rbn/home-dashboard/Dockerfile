FROM node:latest

COPY . .
WORKDIR /client
RUN npm install
RUN npm run build

WORKDIR /server
RUN npm install
RUN rm -rf dist
RUN npm run build
RUN mkdir dist/client
RUN cp -r /client/dist/* /server/dist/client

EXPOSE 8000
ENTRYPOINT npm run start
