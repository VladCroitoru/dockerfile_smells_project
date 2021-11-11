FROM python:3.6.5-slim-stretch
# Dockerfile for that image https://github.com/antonshilov/spellbase

LABEL maintainer="Dmitry Gordin <gordin.mitya@gmail.com>" \
      description="Base image for JamSpell https://github.com/bakwc/JamSpell"

# Workaround for JamSpell https://github.com/bakwc/JamSpell/issues/17
RUN apt-get update && \
    apt-get install --no-install-recommends -y locales && rm -rf /var/lib/apt/lists/* && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8
# End of a workaround