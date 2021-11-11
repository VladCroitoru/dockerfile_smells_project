FROM watsy0007/rubyarn:0.0.9


RUN mkdir -p /tmp/bundler
WORKDIR /tmp/bundler
COPY Gemfile /tmp/bundler
RUN bundle install

CMD ['bash']
