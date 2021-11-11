FROM edvisor/nginx-node

COPY package.json /app/
WORKDIR /app

RUN npm install

COPY gulpfile.js ./
COPY bower.json ./

COPY nginx/*.conf /etc/nginx/conf.d/

COPY ./www ./www
COPY ./scss ./scss
RUN ./node_modules/.bin/gulp
