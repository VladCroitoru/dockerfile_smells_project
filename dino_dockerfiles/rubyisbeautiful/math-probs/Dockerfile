FROM    rubyisbeautiful/centos6-ruby-2.2.3:latest

MAINTAINER <Bryan Taylor> bcptaylor@gmail.com

RUN git clone https://github.com/rubyisbeautiful/math-probs.git /usr/src/app
WORKDIR /usr/src/app
RUN bundle install

EXPOSE 80

CMD bundle exec rackup -s puma -o 0.0.0.0 -p 80