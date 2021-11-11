FROM centos
RUN yum install -y epel-release
RUN yum install -y nodejs npm
COPY package.json /src/package.json
RUN cd /src; npm install --production
COPY . /src
EXPOSE 8081
CMD ["node","/src/index.js"]
