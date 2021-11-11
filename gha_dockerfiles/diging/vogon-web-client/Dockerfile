FROM node:13.8

WORKDIR /usr/src/app
RUN mkdir host
RUN git clone -b master https://github.com/diging/vogon-web-client.git


RUN ["chmod", "+x", "/usr/src/app/vogon-web-client/startup.sh"]
WORKDIR /usr/src/app/vogon-web-client
ENTRYPOINT ["./startup.sh"]