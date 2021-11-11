FROM alpine:3.11 as build

ENV BUNDLE_SILENCE_ROOT_WARNING=1

WORKDIR /app
COPY Gemfile Gemfile.lock ./

RUN apk add --no-cache ruby ruby-dev ruby-bundler ruby-json build-base \
 && bundle install --frozen -j4 -r3 --no-cache --without development \
 && apk del --no-cache ruby-bundler \
 && rm -rf /usr/lib/ruby/gems/*/cache

FROM alpine:3.11 as prod

COPY --from=build /usr/lib/ruby/gems /usr/lib/ruby/gems
RUN apk add --no-cache ruby ruby-json ruby-etc apache2-utils \
 && ruby -e "Gem::Specification.map.each do |spec| \
      Gem::Installer.for_spec( \
        spec, \
        wrappers: true, \
        force: true, \
        install_dir: spec.base_dir, \
        build_args: spec.build_args, \
      ).generate_bin \
    end"

WORKDIR /app
COPY . .

ENV PORT=9292 \
    WEB_CONCURRENCY=4 \
    WEB_MAX_THREADS=4 \
    RACK_ENV=production

EXPOSE $PORT
USER nobody
STOPSIGNAL SIGINT
CMD ["/usr/bin/puma"]
