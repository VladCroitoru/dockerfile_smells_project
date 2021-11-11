FROM monostream/nodejs-gulp-bower:latest

EXPOSE 80 9900

COPY . /data
WORKDIR /data/app

RUN cd $(npm root -g)/npm \
 && npm install fs-extra \
 && sed -i -e s/graceful-fs/fs-extra/ -e s/fs\.rename/fs\.move/ ./lib/utils/rename.js

RUN npm install gulp live-server
RUN npm install devbridge-styleguide --save-dev
RUN npm install devbridge-styleguide -g
RUN styleguide initialize

RUN sed -i -e s/8080/9900/ ./styleguide/config.txt

CMD [ "gulp", "start-styleguide" ]
