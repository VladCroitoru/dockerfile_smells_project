FROM ruby

RUN mkdir -p /opt/epguide
COPY . /opt/epguide/

WORKDIR /opt/epguide
RUN bundle install

CMD ["rackup", "-p", "80", "--host", "0.0.0.0"]
