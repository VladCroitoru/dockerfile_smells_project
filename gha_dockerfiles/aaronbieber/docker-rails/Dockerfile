FROM ruby:2.5

ARG UID
ARG GID

RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

RUN addgroup --gid $GID user
RUN adduser --disabled-password --gecos '' --uid $UID --gid $GID user
USER user

WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
RUN bundle install

EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]
