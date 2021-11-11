FROM maven

RUN     apt-get update \
    &&  apt-get -y install pandoc

VOLUME ["/book" "/wiki" "/root/.m2"]
WORKDIR /book

# do nothing loop
CMD touch /test && tail -f /test
