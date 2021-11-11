FROM liftopia/ubuntu-rvm-base
MAINTAINER Liftopia Operations ops@liftopia.com

RUN \
  bash -l -c 'rvm install 1.9.3' ;\
  bash -l -c 'rvm use 1.9.3 --default' ;\
  bash -l -c 'gem install bundler'

CMD [ "/bin/bash", "--login" ]
