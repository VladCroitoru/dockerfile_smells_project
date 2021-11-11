FROM centos:centos6

# Enable EPEL for Node.js
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# Install Node.js and npm
RUN yum install -y npm git
# clone dynamo archiver project
RUN mkdir -p /opt/app && cd /opt/app && git clone https://github.com/yegor256/dynamo-archive.git

ADD https://raw.githubusercontent.com/yegor256/dynamo-archive/master/package.json /tmp/package.json
RUN cd /tmp && npm install
RUN cp -a /tmp/node_modules /opt/app/dynamo-archive

VOLUME /dynamodata

#install pip
RUN cd /tmp && curl -L -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py

#use pip to install aws-cli (http://aws.amazon.com/cli/)
RUN pip install awscli

#install crontab
RUN yum install -y cronie
RUN service crond start
RUN echo '* * * * * root /opt/app/dynamo-archive/backup.sh' >> /etc/crontab

ONBUILD ADD scripts/backup.sh /opt/app/dynamo-archive/backup.sh
ONBUILD RUN chmod +x /opt/app/dynamo-archive/backup.sh
ONBUILD ADD misc /opt/app/misc

ADD scripts/start_job.sh /opt/app/dynamo-archive/start_job.sh
RUN chmod +x /opt/app/dynamo-archive/start_job.sh

WORKDIR /opt/app/dynamo-archive
ADD . /opt/app/dynamo-archive

CMD ["./start_job.sh"]
