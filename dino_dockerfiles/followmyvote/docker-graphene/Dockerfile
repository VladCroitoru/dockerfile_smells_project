FROM base/archlinux
MAINTAINER Nathan Hourt <nathan@followmyvote.com>

ADD packages.sh /
RUN /packages.sh

RUN useradd -d /var/fmv -s /bin/false -rmN -u 995 fmv
WORKDIR /var/fmv

ADD aur.sh .
RUN ./aur.sh

USER fmv

ADD build.sh .
RUN ./build.sh
