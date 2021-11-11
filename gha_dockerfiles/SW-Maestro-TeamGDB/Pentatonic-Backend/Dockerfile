FROM ubuntu:18.04
RUN apt-get update -y &&\
    apt-get install curl -y &&\
    curl -sL https://deb.nodesource.com/setup_14.x | bash && \
    apt-get install nodejs software-properties-common -y &&\
    add-apt-repository ppa:jonathonf/ffmpeg-4 -y&&\
    apt-get update -y &&\
    apt-get install ffmpeg -y

RUN mkdir -p /server

WORKDIR /server

ADD ./ /server

RUN npm install -g yarn;\
    yarn install; \
    yarn build

EXPOSE 4000

CMD ["yarn", "on" ]