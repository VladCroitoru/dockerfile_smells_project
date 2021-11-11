FROM ubuntu:trusty

RUN apt-get update
RUN apt-get -y install npm git

RUN git clone https://github.com/jeangu/app-node.git /app
RUN cd /app; npm install

EXPOSE 3000
CMD ["nodejs", "/app/index.js" ]
