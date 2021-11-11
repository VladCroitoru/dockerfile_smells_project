FROM node:6.3
MAINTAINER Francois Hill <francoishill11@gmail.com>

RUN apt-get update
RUN apt-get -y install unzip

ENV ZIP_URL "https://codeload.github.com/aurelia/skeleton-navigation/zip/master"
ENV SKELETON_SUBFOLDER "skeleton-esnext"

RUN mkdir -p /tmp/skeleton
WORKDIR /tmp/skeleton

ADD run_prod.sh .
RUN chmod +x ./run_prod.sh

EXPOSE 9000
CMD /tmp/skeleton/run_prod.sh