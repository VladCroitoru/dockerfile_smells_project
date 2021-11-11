FROM herrfolgreich/docker-pages-reader:base-image

ARG repo

RUN set -ex \
 && mkdir -p /tmp/repo \
 && wget -qO- http://api.github.com/repos/${repo}/tarball \
  | tar xzf - --strip-components=1 -C /tmp/repo
 
RUN bundle exec jekyll build -s /tmp/repo -d /app \
 && rm -rf /tmp/repo

CMD ["nginx"]
