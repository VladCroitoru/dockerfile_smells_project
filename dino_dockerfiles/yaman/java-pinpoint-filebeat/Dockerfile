FROM anapsix/alpine-java:latest

RUN apk --no-cache add curl tar supervisor

WORKDIR /pinpoint
ADD https://github.com/naver/pinpoint/releases/download/1.6.2/pinpoint-agent-1.6.2.tar.gz /pinpoint/agent.tar.gz
RUN tar xfz agent.tar.gz

WORKDIR /filebeat
RUN curl -sfS https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.5.1-linux-x86_64.tar.gz \
    | tar -xz --strip-components=1
