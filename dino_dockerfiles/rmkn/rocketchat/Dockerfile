FROM centos:7
MAINTAINER rmkn
RUN sed -i -e "s/en_US.UTF-8/ja_JP.UTF-8/" /etc/locale.conf
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime 
RUN yum -y update
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo ""

RUN yum -y install epel-release && yum -y update
COPY mongodb.repo /etc/yum.repos.d/

RUN yum install -y nodejs curl GraphicsMagick npm mongodb-org-server mongodb-org gcc-c++ which make
RUN npm install -g inherits n
RUN n 8.9.3

RUN curl -SL https://releases.rocket.chat/latest/download -o /tmp/rocket.chat.tgz \
        && tar zxf /tmp/rocket.chat.tgz -C /usr/local \
	&& mv /usr/local/bundle /usr/local/Rocket.Chat

WORKDIR /usr/local/Rocket.Chat/programs/server
RUN npm install
WORKDIR /usr/local/Rocket.Chat/programs/server/npm/node_modules
RUN npm rebuild sharp

ENV PORT 80
ENV ROOT_URL http://localhost/
ENV MONGO_URL mongodb://localhost:27017/rocketchat

COPY entrypoint.sh /

#VOLUME /data/db
RUN mkdir -p /data/db && chmod 777 /data/db
EXPOSE 80

CMD ["node", "/usr/local/Rocket.Chat/main.js"]

ENTRYPOINT ["/entrypoint.sh"]

