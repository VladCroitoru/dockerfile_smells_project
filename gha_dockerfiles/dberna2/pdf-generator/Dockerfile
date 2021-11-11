FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
ENV NODE_VERSION=14

RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_14.x  | bash -
RUN apt-get -y install nodejs

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list
RUN apt-get update --fix-missing
RUN apt-get upgrade -y

# Download and install wkhtmltopdf
RUN apt-get install -y build-essential xorg libssl-dev libxrender-dev wget gdebi
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb

RUN apt-get -y install imagemagick librsvg2-dev librsvg2-bin

RUN apt-get -y clean && \
    apt-get -y purge && \
    rm -rf /var/lib/apt/lists/* /tmp/*

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./ ./

RUN chmod -R 741 /usr/src/app/wkhtmltox/bin/*

RUN npm install

EXPOSE 4000

CMD [ "npm", "run", "prod" ]
