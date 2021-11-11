FROM iojs
MAINTAINER Austin Salgat <salgat@salgat.net>

WORKDIR /opt/head
RUN git clone git://github.com/mobz/elasticsearch-head.git

WORKDIR /opt/head/elasticsearch-head
ADD Gruntfile.js Gruntfile.js
RUN npm update
RUN npm install -g grunt-cli
RUN npm install -p /opt/head/elasticsearch-head

ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
