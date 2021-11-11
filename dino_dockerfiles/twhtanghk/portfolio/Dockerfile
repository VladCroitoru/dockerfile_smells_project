FROM node:13

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN (cd backend && yarn install) \
&& (cd frontend && npm i)

EXPOSE 1337

CMD (cd frontend && yarn build) && (cd backend && yarn start)
