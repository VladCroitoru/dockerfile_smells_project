# Blog dockerfile w/Techno Theme

FROM zerodivide1/docker-ghost:0.5.7
MAINTAINER Sean Payne <seantpayne@gmail.com>

ADD default-settings.patch /ghost/core/server/data/default-settings.patch

RUN \
  cd /ghost/core/server/data && \
  patch < default-settings.patch && \
  rm default-settings.patch

RUN \
  cd /ghost/content/themes && \
  git clone -b prod https://github.com/zerodivide1/ghost-theme-techno.git techno && \
  cd /ghost && \
  rm -f /ghost-start && \
  $(useradd ghost --home /ghost || true)

ADD start.bash /ghost-start

ENV NODE_ENV production

VOLUME ["/data", "/ghost-override"]

WORKDIR /ghost

CMD ["bash", "/ghost-start"]

EXPOSE 2368
