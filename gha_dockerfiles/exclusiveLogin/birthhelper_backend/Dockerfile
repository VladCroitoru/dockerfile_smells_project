FROM node:14.17.6
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN npm i -g npm
RUN rm dist/ -rf
RUN mkdir dist && cd dist && mkdir upload

ENV PM2_PUBLIC_KEY smyrbcl05x8u5yo
ENV PM2_SECRET_KEY m84owwtipe5nhoa

ENTRYPOINT npm run deploy:docker
EXPOSE 3000
