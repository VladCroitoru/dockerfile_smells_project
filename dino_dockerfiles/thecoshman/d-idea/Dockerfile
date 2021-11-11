FROM frolvlad/alpine-glibc:alpine-3.6

ENV IDE_VER='2017.2.5'

RUN apk add --no-cache \
    bash \
    git \
    openjdk8

RUN apk add --no-cache \
    ca-certificates \
    wget \
 && update-ca-certificates \
 && echo ' = Downloadng Intellij IDE' \
 && wget --progress=dot:giga https://download.jetbrains.com/idea/ideaIC-$IDE_VER.tar.gz -O /tmp/intellij.tar.gz \
 && mkdir -p /opt/intellij \
 && tar -xzf /tmp/intellij.tar.gz --strip-components=1 -C /opt/intellij \
 && rm /tmp/intellij.tar.gz 

CMD /opt/intellij/bin/idea.sh
