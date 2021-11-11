FROM jekyll/jekyll

WORKDIR /srv/jekyll
COPY . /srv/jekyll
RUN jekyll build

CMD ["jekyll", "serve"]
