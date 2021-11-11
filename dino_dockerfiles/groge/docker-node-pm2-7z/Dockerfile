FROM centos:7
LABEL maintainer="groge <groge.choi@gmail.com>"

# install Node
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash -
RUN yum install -y nodejs wget
RUN yum clean all -y

# Install pm2
RUN npm install -g pm2 node-gyp

# 7zip for Patch
RUN wget https://www.mirrorservice.org/sites/dl.fedoraproject.org/pub/epel/7/x86_64/Packages/p/p7zip-16.02-10.el7.x86_64.rpm
RUN wget https://www.mirrorservice.org/sites/dl.fedoraproject.org/pub/epel/7/x86_64/Packages/p/p7zip-plugins-16.02-10.el7.x86_64.rpm

RUN rpm -U --quiet p7zip-16.02-10.el7.x86_64.rpm
RUN rpm -U --quiet p7zip-plugins-16.02-10.el7.x86_64.rpm

# Python for SNMP
#RUN apk add --no-cache --update python

ENV NODE_ENV production

EXPOSE 3000

WORKDIR /app

# Start pm2.json process file
CMD ["pm2-runtime", "start", "pm2.json"]
