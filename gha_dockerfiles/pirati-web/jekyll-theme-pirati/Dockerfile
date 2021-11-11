FROM jekyll/jekyll:3.7.3

# Install ImageMagick
RUN apk --no-cache add \
    file \
    imagemagick \
    curl

RUN npx npm@5.6 i -g npm@5.8.0

CMD ["jekyll", "--help"]

ENTRYPOINT ["/usr/jekyll/bin/entrypoint"]

WORKDIR /srv/jekyll

VOLUME  /srv/jekyll

EXPOSE 35729
EXPOSE 3000
EXPOSE 4000
