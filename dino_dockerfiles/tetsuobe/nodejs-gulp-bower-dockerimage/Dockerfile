FROM debian:jessie

MAINTAINER tetsuobe <tetsuobe@gmail.com>

RUN apt-get update && apt-get install -y curl git supervisor bzip2 && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y nodejs

RUN npm set progress=false && \
    npm install --global --progress=false gulp bower && \
    echo '{ "allow_root": true }' > /root/.bowerrc

RUN apt-get autoclean -y && \
    apt-get clean -y

EXPOSE 8080

COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf