FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update # 0529
RUN apt-get install -y python python-pip wget

RUN pip install --upgrade pip
RUN pip install http://www.jbox.dk/sling/sling-1.0.0-cp27-none-linux_x86_64.whl

RUN mkdir /usr/local/sling
WORKDIR /usr/local/sling
RUN wget http://www.jbox.dk/sling/sempar.flow

COPY trying_out.py trying_out.py
RUN echo SLING is a parser for annotating text with frame semantic annotations. | python trying_out.py
