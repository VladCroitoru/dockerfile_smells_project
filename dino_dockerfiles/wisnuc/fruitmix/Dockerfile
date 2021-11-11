# The default version of Ubuntu 16.04's python is 3.0, some npm packages can not be built.
FROM ubuntu:14.04

MAINTAINER JiangWeiGitHub <wei.jiang@winsuntech.cn>

# Update apt sourcelist
RUN echo "deb http://ubuntu.uestc.edu.cn/ubuntu/ trusty main restricted universe multiverse" > /etc/apt/sources.list \
 && echo "deb http://ubuntu.uestc.edu.cn/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://ubuntu.uestc.edu.cn/ubuntu/ trusty-proposed main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://ubuntu.uestc.edu.cn/ubuntu/ trusty-security main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://ubuntu.uestc.edu.cn/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list

# update apt
RUN apt-get update

# install all essential packages with apt-get
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
apt-transport-https \
ca-certificates \
build-essential \
wget \
git \
python \
imagemagick \
graphicsmagick \
supervisor

# install ffmpeg for Ubuntu 14.04
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-properties software-properties-common \
 && add-apt-repository ppa:mc3man/trusty-media \
 && apt-get update \
 && apt-get -y install ffmpeg

# install nodejs with binary packages
RUN wget https://nodejs.org/dist/v6.2.1/node-v6.2.1-linux-x64.tar.xz \
 && tar -Jxf node-v6.2.1-linux-x64.tar.xz \
 && \cp -rf ./node-v6.2.1-linux-x64/* /usr/local/ \
 && rm -rf node-v6.2.1-linux-x64 node-v6.2.1-linux-x64.tar.xz

# install fruitmix project's source code
# RUN cd / \
#  && mkdir git \
#  && cd /git \
#  && git clone https://github.com/wisnuc/fruitmix.git \
#  && cd fruitmix \
#  && echo "{" > .babelrc \
#  && echo "  \"presets\": [\"es2015\"]," >> .babelrc \
#  && echo "  \"plugins\": [\"syntax-async-functions\", \"transform-regenerator\", \"transform-es2015-template-literals\", \"transform-runtime\"]" >> .babelrc \
#  && echo "}" >> .babelrc
 
RUN cd / \
 && mkdir git \
 && cd /git \
 && git clone https://github.com/wisnuc/fruitmix.git \
 && cd fruitmix

# point out working directory
WORKDIR /git/fruitmix

# install npm packages
# RUN npm --registry http://registry.cnpmjs.org install -g babel-cli fs-xattr nodemon gm ffmpeg imagemagick graphicsmagick \
#  && npm --registry http://registry.cnpmjs.org install babylon babel-preset-es2015 babel-preset-es2016 babel-plugin-transform-runtime \
#  && npm --registry http://registry.cnpmjs.org install
# # PS: the reason that use '--registry http://registry.cnpmjs.org' is that tianchao's network is you know why.

# install npm packages
RUN npm install -g babel-cli fs-xattr nodemon gm ffmpeg imagemagick graphicsmagick \
 && npm install babylon babel-preset-es2015 babel-preset-es2016 babel-plugin-transform-runtime \
 && npm install

# build source code
RUN npm run build

# deploy mongodb enviroment
RUN mkdir /mongodb \
 && mkdir /data \
 && mkdir -p /var/log/supervisor
VOLUME /mongodb /data /var/log/supervisor
EXPOSE 80

# install mongodb
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \
 && echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb-org

# configure supervisor for running mongodb & fruitmix both
RUN echo "[supervisord]" > /etc/supervisor/conf.d/supervisord.conf \
 && echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "[program:mongod]" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "command=/bin/bash -c \"mongod --dbpath /mongodb\"" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "[program:fruitmix]" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "command=/bin/bash -c \"npm start\"" >> /etc/supervisor/conf.d/supervisord.conf \
 && echo "" >> /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
