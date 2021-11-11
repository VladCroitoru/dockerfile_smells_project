FROM gullitmiranda/elixir

# Install local Elixir hex and rebar
RUN  apk add --update postgresql-client \
  && rm -rf /var/cache/apk/* /var/tmp/* \

CMD ["psql"]