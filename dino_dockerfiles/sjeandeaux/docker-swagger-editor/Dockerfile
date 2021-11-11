FROM node:0.10

MAINTAINER Stéphane Jeandeaux <stephane.jeandeaux@gmail.com>

RUN npm update npm &&\
    npm install -g http-server 

RUN apt-get update && apt-get install unzip
ADD https://github.com/swagger-api/swagger-editor/releases/download/v2.9.8/swagger-editor.zip /tmp/swagger.zip
RUN mkdir /swagger && unzip /tmp/swagger.zip -d /swagger

RUN apt-get clean && rm -f /tmp/swagger.zip 

EXPOSE 8888
CMD ["http-server", "/swagger/swagger-editor", "-p", "8888", "--cors"]
