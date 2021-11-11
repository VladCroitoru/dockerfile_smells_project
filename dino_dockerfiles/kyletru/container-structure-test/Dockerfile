# Latest Docker image
FROM docker:latest
MAINTAINER Kyle Truszkowski <kyletru@gmail.com>
RUN apk --no-cache add curl  
RUN curl -LO https://storage.googleapis.com/container-structure-test/v1.1.0/container-structure-test && chmod +x container-structure-test && mv container-structure-test /usr/bin/
RUN ln -s /usr/bin/container-structure-test /usr/bin/structure-test
