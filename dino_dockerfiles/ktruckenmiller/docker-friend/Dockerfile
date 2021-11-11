FROM node AS static
RUN npm install webpack hapi babel-cli -g
WORKDIR /code
COPY package.json /code
RUN npm install
COPY . /code
RUN npm run build
RUN ls


FROM node as FRIEND
RUN apk add --no-cache net-tools iptables curl jq
RUN npm install webpack hapi babel-cli -g
RUN npm install ifconfig-linux lodash
WORKDIR /code/api
COPY api/package.json /code/api
RUN npm install

COPY api /code/api
COPY startups/ifconfig.js /code
COPY --from=static /code/dist /code/dist
WORKDIR /code
COPY index.html setup.sh /code/

ENTRYPOINT ["/code/setup.sh"]


FROM nginx:alpine as NGINX
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

FROM FRIEND as DEV
WORKDIR /code
RUN npm install -g nodemon babel-polyfill
