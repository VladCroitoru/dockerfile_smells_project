FROM node:7.8.0
#FROM armhf/node:7.8.0 # arch=armhf

COPY . /app
WORKDIR /app

RUN npm install --global gulp-cli
RUN npm install

RUN gulp build

EXPOSE 80
CMD ./entrypoint.sh