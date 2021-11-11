FROM debian:buster as builder

RUN set -xe \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -qq \
    && apt-get dist-upgrade -qq \
    && apt-get install -qqy --no-install-recommends \
        locales \
        openjdk-11-jdk-headless \
        git-core \
    && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && mkdir /var/sources

ENV LC_ALL=en_US.UTF-8

COPY gradle /var/sources/gradle
COPY gradlew /var/sources/gradlew

# Download gradle in a separate layer
RUN set -xe \
    && cd /var/sources \
    && ./gradlew --no-daemon --version

COPY . /var/sources

RUN set -xe \
    && cd /var/sources \
    && ./gradlew --no-daemon jar



FROM debian:buster

RUN set -xe \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -qq \
    && apt-get dist-upgrade -qq \
    && apt-get install -qqy --no-install-recommends \
        locales \
        openjdk-11-jre-headless \
    && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && SUDO_FORCE_REMOVE=yes apt-get autoremove -qq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir -p /etc/beholder \
    && mkdir -p /var/log/beholder

ENV LC_ALL=en_US.UTF-8

COPY --from=builder /var/sources/build/libs /root
COPY docker/beholder /sbin/
COPY docker/install-devtools.sh /sbin/
COPY docker/beholder.conf /etc/beholder/

CMD [ \
    "/usr/bin/java", \
    "-server", \
    "-Xms12m", \
    "-jar", \
    "/root/beholder-0.1.jar", \
    "--config-file=/etc/beholder/beholder.conf" \
]
