FROM ruby:2.3
EXPOSE 4567

RUN apt-get update && apt-get install -y git
RUN apt-get install -y nodejs

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/

COPY Rakefile /usr/src/app/
WORKDIR /usr/src/app
RUN gem install bundler
RUN bundle install

COPY . /usr/src/app

ENTRYPOINT ["rake"]
CMD ["dev"]

# 1) Build: docker build -t devbamboracom .
# 2) Run:   docker run -v `pwd`/source:/usr/src/app/source -w /usr/src/app -p 4567:4567 devbamboracom
