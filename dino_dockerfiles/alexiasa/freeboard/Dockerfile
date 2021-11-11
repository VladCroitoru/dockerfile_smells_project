FROM centos:centos6

RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN     yum install -y npm
RUN npm install express
COPY . /freeboard
WORKDIR /freeboard
RUN npm install
EXPOSE 3000
CMD ["node", "/freeboard/app.js"]

