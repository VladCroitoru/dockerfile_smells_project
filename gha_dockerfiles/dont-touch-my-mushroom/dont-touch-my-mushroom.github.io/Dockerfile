ARG JEKYLL_VERSION=3.8

FROM jekyll/jekyll:$JEKYLL_VERSION

ENV TZ=Europe/Zurich
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "Starting jekyll"

RUN ls -lah /srv/jekyll

CMD ["jekyll", "serve"]