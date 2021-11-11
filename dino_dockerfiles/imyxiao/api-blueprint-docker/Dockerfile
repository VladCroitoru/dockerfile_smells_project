FROM centos

RUN yum install -y epel-release && yum update -y && yum install -y node npm make nginx git
RUN npm --registry=https://registry.npm.taobao.org
RUN npm install -g aglio drakov

COPY scripts/startup.sh /usr/local/bin/
COPY scripts/deploy.sh /usr/local/bin/
COPY scripts/webhook.js /usr/local/bin/

RUN chmod -R 755 /usr/local/bin/*

CMD /usr/local/bin/deploy.sh && /usr/local/bin/startup.sh
