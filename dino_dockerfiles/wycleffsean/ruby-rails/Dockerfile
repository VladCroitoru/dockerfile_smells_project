FROM ruby:2.2.3

# Fixes overlayfs+nokogiri compilation combination
# https://github.com/docker-library/ruby/issues/55
RUN gem update --system '2.4.8'

COPY ./gems.rb ./gems.rb
RUN ruby gems.rb && rm gems.rb

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

CMD ["bash"]
