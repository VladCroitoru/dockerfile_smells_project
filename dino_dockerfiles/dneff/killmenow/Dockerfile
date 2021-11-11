FROM centos:centos7

# Enable EPEL for Node.js
RUN     rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
# Install Node.js and npm
RUN     yum install -y npm
COPY . /src
RUN cd /src; npm install
EXPOSE 3000

CMD ["node", "/src/bin/www"]
