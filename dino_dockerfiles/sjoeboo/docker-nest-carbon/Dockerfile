FROM sjoeboo/rbenv:2.3.1

#RUN rbenv install 2.1.2
#RUN rbenv global 2.1.2
#RUN gem install bundler

ADD . /nest
WORKDIR /nest
RUN bundle install

ENV GRAPHITE_HOST  'graphite'
ENV GRAPHITE_PORT  2003
ENV NEST_EMAIL  'someone@something.com'
ENV NEST_PASS  'somepass'
CMD /nest/run.sh
