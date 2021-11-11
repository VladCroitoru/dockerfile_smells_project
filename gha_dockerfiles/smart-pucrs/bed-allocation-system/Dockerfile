FROM alpine

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV JACAMO_HOME=/jacamo/build
ENV PATH $PATH:$JAVA_HOME/bin #:$JACAMO_HOME/scripts

RUN apk add --update --no-cache git gradle openjdk8-jre bash fontconfig ttf-dejavu graphviz
RUN git clone https://github.com/jacamo-lang/jacamo.git && \
    cd jacamo && \
    gradle config

COPY . /app

RUN cd app && gradle build

EXPOSE 3271
EXPOSE 3272
EXPOSE 3273
EXPOSE 8080

WORKDIR /app


ENTRYPOINT [ "gradle", "run" ]

CMD []