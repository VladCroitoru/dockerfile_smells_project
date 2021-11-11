FROM sorrell/alpine-mono-xsp

ENV OMNIDB_VER 1.6.3

RUN apk add --no-cache \
  curl \
  zip

RUN curl -Lo /tmp/OmniDB.zip https://github.com/OmniDB/OmniDB/releases/download/v${OMNIDB_VER}/OmniDB-${OMNIDB_VER}.zip
RUN unzip /tmp/OmniDB.zip -d /opt/
RUN rm -f /tmp/OmniDB.zip

WORKDIR "/opt/OmniDB-${OMNIDB_VER}"

EXPOSE 9000
CMD xsp4 --nonstop --port 9000
