FROM ruby:2.2.2

ADD ./ /src
WORKDIR /src

RUN gem install bundler
RUN bundle install

ENTRYPOINT ["bundle", "exec"]
CMD ["./app","-p","80","-o","0.0.0.0"]

EXPOSE 80
VOLUME /data
ENV DATA_DIR /data

