FROM debian:bullseye-20210816-slim

ENV LANG=C.UTF-8 USER=root HOME=/root

# Tools for dockerfiles and image management
COPY rootfs /

# Base tools that are used by all images
RUN apt_install \
    runit \
    gettext-base \
    ca-certificates \
    curl \
    jo \
    jq \
    make \
    time \
    git \
    openssh-client \
    file \
 # Copy single binaries from packages and remove packages
 && cp /usr/bin/chpst \
       /usr/bin/envsubst \
       /usr/local/bin \
 && dpkg -P runit gettext-base \
 && apt-get -qqy autoremove \
 && dpkg -l|awk '/^rc/ {print $2}'|xargs -r dpkg -P \
 && (cd /usr/local/bin && ln -s chpst setuidgid && ln -s chpst softlimit && ln -s chpst setlock) \
\
 # Create basic folders
 && mkdir -p /feedback /submission /exercise \
 && chmod 0770 /feedback \
\
 # Change HOME for nobody from /nonexistent to /tmp
 && usermod -d /tmp nobody \
 # Create two more nobody users
 && groupadd doer -g 65501 \
 && useradd doer -u 65501 -g 65501 -c "a nobody user" -s /usr/sbin/nologin -m -k - \
 && groupadd tester -g 65502 \
 && useradd tester -u 65502 -g 65502 -c "a nobody user" -s /usr/sbin/nologin -m -k - \
 && :

# Base grading tools
COPY bin /usr/local/bin

# Base environment
WORKDIR /submission
ENTRYPOINT ["/gw"]
CMD ["/exercise/run.sh"]
