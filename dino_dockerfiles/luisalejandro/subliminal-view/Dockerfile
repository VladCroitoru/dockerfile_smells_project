ARG DISTRO="debian"
ARG CODENAME="sid"

FROM dockershelf/${DISTRO}:${CODENAME}}
LABEL maintainer "Luis Alejandro Martínez Faneyth <luis@collagelabs.org>"

RUN apt-get update && \
    apt-get install \
        sudo devscripts equivs

RUN useradd --create-home --shell /bin/bash --uid 1000 build
RUN echo "build ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/build

ADD debian/control /tmp/
RUN mk-build-deps -t 'apt-get -y -o Debug::pkgProblemResolver=yes --no-install-recommends' -ri /tmp/control
RUN rm /tmp/control

USER build
CMD ["bash"]