FROM ruby:2

RUN gem install redis-browser

RUN apt-get update -yq && apt-get upgrade -yq && apt-get install nodejs -yq

RUN sed -i -e "s/bind: '127.0.0.1'/bind: '0.0.0.0'/g" /usr/local/bundle/gems/redis-browser-0.3.3/bin/redis-browser

# Define the entrypoint script.
ENTRYPOINT ["redis-browser"]

# Expose ports.
EXPOSE 4567
