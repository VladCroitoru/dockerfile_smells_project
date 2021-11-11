FROM ruby:2.5 as builder

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

RUN bundle exec jekyll build

# ----

FROM nginx

COPY --from=builder /usr/src/app/_site/ /usr/share/nginx/html
