FROM ruby:2.2.2-onbuild
RUN mkdir -p /usr/src/app
RUN mkdir -p /data/keys
WORKDIR /usr/src/app
COPY keys.rb /usr/src/app/
ENTRYPOINT ["ruby", "keys.rb"]
