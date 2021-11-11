FROM ubuntu:latest

RUN apt-get update && apt-get install -y ruby
RUN gem install fakes3

RUN mkdir -p /var/data/fakes3

EXPOSE 3128

CMD ["fakes3", "-r", "/var/data/fakes3", "-p", "3128", "-H", "fakes3"]