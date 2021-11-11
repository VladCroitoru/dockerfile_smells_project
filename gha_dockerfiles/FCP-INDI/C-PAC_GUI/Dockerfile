FROM node:8-alpine
RUN npm install -g -s --no-progress yarn

RUN mkdir -p /code
WORKDIR /code
ADD . /code

RUN yarn global add yalc
RUN yarn

CMD ["yarn", "dev:renderer"]
EXPOSE 1212
