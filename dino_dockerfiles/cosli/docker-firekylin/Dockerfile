FROM node:latest
WORKDIR /
ADD https://raw.githubusercontent.com/cosli/docker-firekylin/master/package.json /package.json
RUN echo "Asia/Shanghai" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && wget https://raw.githubusercontent.com/cosli/docker-firekylin/master/initfire.sh \
    && chmod 755 initfire.sh \
    && npm install \
    && npm install -g pm2
