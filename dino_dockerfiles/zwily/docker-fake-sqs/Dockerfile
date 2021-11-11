FROM ruby:2.1

RUN gem install fake_sqs

EXPOSE 3000

RUN mkdir -p /var/lib/sqs

ENTRYPOINT [ "/usr/local/bundle/bin/fake_sqs", "-p", "3000", "--no-daemonize" ]
