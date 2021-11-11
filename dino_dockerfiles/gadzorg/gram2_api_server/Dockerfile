FROM ruby:2.2
MAINTAINER roots@asso.gadz.org

RUN mkdir /appli

COPY . /appli/

RUN gem install bundler -v 1.11.2 && \
    cd /appli && \ 
    bundle install --jobs=3 --retry=3 --deployment --without developpement

WORKDIR /appli

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
