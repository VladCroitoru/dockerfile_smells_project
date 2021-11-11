FROM circleci/ruby:2.3.7
WORKDIR /home/circleci

COPY work/ $WORKDIR

RUN sudo apt-get update && sudo apt-get upgrade -y
RUN sudo apt-get install -y libpcap-dev

RUN gem update
RUN bundle install
