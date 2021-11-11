FROM node:9.1

RUN apt-get update && apt-get install -y unzip
RUN wget https://releases.hashicorp.com/envconsul/0.7.2/envconsul_0.7.2_linux_amd64.zip\
    && unzip envconsul_0.7.2_linux_amd64.zip\
    && ln -sf $PWD/envconsul /usr/local/bin

COPY ./app /app
WORKDIR /app
RUN yarn
