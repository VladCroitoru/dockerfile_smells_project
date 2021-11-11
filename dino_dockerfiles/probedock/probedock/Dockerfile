FROM probedock/probedock-docker-base

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install --without development test

COPY . /usr/src/app

EXPOSE 3000
CMD [ "./start.sh" ]
