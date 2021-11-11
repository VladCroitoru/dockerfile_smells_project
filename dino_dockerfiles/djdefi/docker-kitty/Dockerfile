FROM alpine:latest

RUN apk --update add \
  ruby && \
  gem install kitty

ENTRYPOINT ["kitty","-c"]
CMD ["1"]
