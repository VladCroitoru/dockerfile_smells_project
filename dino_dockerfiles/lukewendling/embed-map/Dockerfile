FROM node:4.2

RUN mkdir /git-tmp
WORKDIR /git-tmp
RUN apt-get update && \
    apt-get install -y git

RUN git config --global user.name "John Smith" && \
    git config --global user.email "email@example.com"

RUN mkdir /app
WORKDIR /app

RUN git clone --depth 1 https://github.com/lukewendling/embed-map.git

WORKDIR /app/embed-map
RUN npm install -g bower
RUN npm install && bower install --allow-root
EXPOSE 3000
CMD npm start
