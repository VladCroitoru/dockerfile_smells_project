FROM node:12
WORKDIR /usr/src/app

COPY package.json ./
COPY yarn.lock ./
RUN yarn

COPY pages pages
COPY components components
COPY public public
COPY lib lib
COPY styles styles
COPY data data
COPY *.* ./

ENV CI=True
RUN yarn build

ENV TZ=US/Pacific
ENTRYPOINT [ "yarn", "start" ]
