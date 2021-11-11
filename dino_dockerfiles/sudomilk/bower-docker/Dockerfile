FROM node:alpine

RUN ["npm", "install" , "-g", "bower"]
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN ["adduser", "-S", "bower"]
USER bower
WORKDIR /home/bower
VOLUME ["/home/bower"]
ENTRYPOINT ["bower"]
CMD ["--help"]
