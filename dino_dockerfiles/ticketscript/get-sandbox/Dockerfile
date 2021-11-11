FROM sdorra/oracle-java-8:latest

MAINTAINER Jay <geoffrey.dekleijn@ticketscript.nl>

EXPOSE 8081

VOLUME /var/www

WORKDIR /var/www

RUN wget --no-check-certificate -O - "https://s3-us-west-2.amazonaws.com/getsandbox-assets/runtime-binary.tar" | tar x -C /usr/local/bin/

CMD ["/usr/local/bin/sandbox", "run", "--port=8081"]
