FROM openjdk:8u171-jdk-slim

ENV CACHE_TAG $CACHE_TAG

RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y install git
RUN echo $CACHE_TAG
RUN sh -c '(echo "#!/usr/bin/env sh" && curl -L https://github.com/lihaoyi/mill/releases/download/0.6.0/0.6.0) > /usr/local/bin/mill && chmod +x /usr/local/bin/mill'

CMD ["mill", "-i"]
