FROM ruby:2.3.1

RUN apt-get update
RUN apt-get install -y fping
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD start_container /usr/bin/start_container
RUN chmod +x /usr/bin/start_container
CMD start_container
