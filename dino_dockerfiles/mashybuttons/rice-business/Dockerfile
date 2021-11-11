FROM node

RUN mkdir /src

RUN npm install nodemon -gq

WORKDIR /src
COPY . /src
RUN npm install -q

EXPOSE 3002

CMD npm run start_prod
