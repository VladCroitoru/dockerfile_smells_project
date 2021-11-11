FROM buildpack-deps:stretch

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs inotify-tools netcat

RUN mkdir /koans

COPY ./*.sh /

RUN chmod +x /*.sh

WORKDIR /koans

CMD "/bin/bash"