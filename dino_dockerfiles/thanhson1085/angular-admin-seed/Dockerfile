FROM ubuntu:14.04
MAINTAINER Nguyen Sy Thanh Son <thanhson1085@gmail.com>

RUN apt-get update && \
    apt-get install -y supervisor sqlite3 build-essential wget \
    python-pip python-dev git imagemagick nginx \
    redis-server
RUN \
    cd /tmp && \
    wget http://nodejs.org/dist/v4.2.2/node-v4.2.2.tar.gz && \
    tar xvzf node-v4.2.2.tar.gz && \
    rm -f node-v4.2.2.tar.gz && \
    cd node-v* && \
    ./configure && \
    CXX="g++ -Wno-unused-local-typedefs" make && \
    CXX="g++ -Wno-unused-local-typedefs" make install
RUN \
    cd /tmp && \
    rm -rf /tmp/node-v* && \
    npm install -g npm && \
    printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc


RUN node -v && npm -v
RUN npm install -g nodemon
RUN npm install -g bower
RUN npm install -g grunt-cli

WORKDIR /build
ADD ./package.json /build/package.json
ADD ./bower.json /build/bower.json
# install all package
RUN bower install --allow-root
RUN npm install
RUN npm install sqlite3 --save
RUN npm install -g pm2
ADD . /build

EXPOSE 80:80

RUN pip install supervisor-stdout
COPY nginx.angular-admin-seed.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
