FROM node:16-alpine
EXPOSE 8080
COPY src/ /portal/src/
COPY package.json yarn.lock /portal/
COPY secret/ /portal/secret/
RUN apk update
WORKDIR /portal
RUN yarn
RUN yarn run build
CMD yarn run run
