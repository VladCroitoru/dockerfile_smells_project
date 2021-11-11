FROM node:14

WORKDIR /app

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /app
COPY ./package*.json /app
COPY yarn.lock /app
RUN yarn

COPY . .

RUN chmod +x wait-for-it.sh

ENV NODE_ENV development
EXPOSE 3000
CMD ["yarn","dev"]