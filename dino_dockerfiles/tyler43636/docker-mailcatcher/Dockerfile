FROM ruby:2.3

MAINTAINER "Tyler Payne" <tyler43636@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y libsqlite3-dev && \
    gem install mailcatcher --no-rdoc --no-ri

EXPOSE 1025
EXPOSE 1080

ENTRYPOINT ["mailcatcher"]

CMD ["-f", "--ip=0.0.0.0"]
