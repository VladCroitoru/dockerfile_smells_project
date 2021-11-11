FROM java:8
MAINTAINER Blastrain<tech@blastrain.co.jp>

ENV JAVAPATH /java
ENV PATH $JAVAPATH/bin:/usr/local/java/bin:$PATH

RUN wget https://github.com/digital-preservation/csv-validator/releases/download/1.1.5/csv-validator-cmd-1.1.5-application.zip \
    && unzip csv-validator-cmd-1.1.5-application.zip

ENV PATH /csv-validator-cmd-1.1.5/bin:$PATH
