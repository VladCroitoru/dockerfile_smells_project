FROM centos:centos7

MAINTAINER robert.carroll@gmail.com

# Enable EPEL, Node.js, and NPM
RUN yum install -y epel-release && yum install -y nodejs npm

# Copy app to /src
COPY . /src

WORKDIR /src

# Install app and dependencies into /src
RUN npm install

EXPOSE 8080

CMD ["node", "app.js"]