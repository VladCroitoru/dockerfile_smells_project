FROM python:3.9-alpine

COPY requirements.txt /tmp/
RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        git \
        make \
        bash \
        curl \
        file \
        openssl \
        perl \
        sudo \
        swig \
    \
    # runtime
    && apk add --no-cache \
        libstdc++ \
    # mecab
    && mkdir -p /tmp/mecab \
    && cd /tmp/mecab \
    && git clone https://github.com/taku910/mecab . \
    && cd mecab \
    && ./configure --enable-utf8-only \
    && make \
    && make install \
    && rm -rf /tmp/mecab \
    \
    # mecab-ipadic-neologd
    && mkdir -p /tmp/mecab-ipadic-neologd \
    && cd /tmp/mecab-ipadic-neologd \
    && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd . \
    && ./bin/install-mecab-ipadic-neologd -n -y \
    && rm -rf /tmp/mecab-ipadic-neologd \
    \
    # pip
    && cd /tmp \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir \
        -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    \
    && apk del --purge .build-deps

WORKDIR /app
RUN mkdir dist

COPY src/testMecab.py src/fetchTweets.py src/generateModel.py src/makeSentence.py src/discord.py /app/
ENV MECAB_DICTIONARY_PATH=/usr/local/lib/mecab/dic/mecab-ipadic-neologd

ARG TZ
ARG USERS
ARG TWITTER_CK
ARG TWITTER_CS
ARG TWITTER_AT
ARG TWITTER_ATS
ARG DISCORD_WEBHOOK_URL

ENV TZ=${TZ}
ENV USERS=${USERS}
ENV TWITTER_CK=${TWITTER_CK}
ENV TWITTER_CS=${TWITTER_CS}
ENV TWITTER_AT=${TWITTER_AT}
ENV TWITTER_ATS=${TWITTER_ATS}
ENV DISCORD_WEBHOOK_URL=${DISCORD_WEBHOOK_URL}

COPY . /app/

RUN python src/testMecab.py \
    && python src/fetchTweets.py \
    && python src/generateModel.py

# Add script to crontab
RUN echo '0 0 * * * cd /app; python fetchTweets.py && python src/generateModel.py' > /var/spool/cron/crontabs/root

RUN echo '*/5 * * * * cd /app; python src/discord.py' > /var/spool/cron/crontabs/root

# Run crond
ENTRYPOINT ["crond", "-f"]


