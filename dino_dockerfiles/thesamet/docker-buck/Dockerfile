FROM java:8

MAINTAINER thesamet@gmail.com

RUN apt-get update && apt-get install -y git ant gcc python python-dev

RUN useradd -m -s /bin/false buck
RUN mkdir /buck && chown buck /buck

USER buck
RUN git clone https://github.com/facebook/buck.git /buck/

WORKDIR /buck

RUN ant

USER root

RUN ln -sf /buck/bin/buck /usr/bin/

