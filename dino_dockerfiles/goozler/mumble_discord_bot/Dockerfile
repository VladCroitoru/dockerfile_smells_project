FROM goozler/zeroc_ice_python:3.7.0.1
ARG BUILD_DATE
ARG VCS_REF
LABEL maintainer="Krutov Alexander <goozler@mail.ru>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/goozler/mumble_discord_bot.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc.1" \
      org.label-schema.description="Send a notification to Discord when someone \
has connected or disconnected to a Mumble server"

RUN set -ex \
  && pip install \
       pytz \
       requests \
  && find /usr/local -depth \
       \( \
         \( -type d -a \( -name test -o -name tests \) \) \
         -o \
         \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
       \) -exec rm -rf '{}' +;

WORKDIR /app
COPY Murmur.ice discord_bot.py ./

CMD ["python", "discord_bot.py"]
