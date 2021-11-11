FROM node

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN npm i

CMD npm test
