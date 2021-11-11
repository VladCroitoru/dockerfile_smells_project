FROM bitnami/minideb:unstable

RUN  echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/90local-no-recommends

RUN  apt-get update \
  && apt-get install -y \
       curl \
       git \
       libpoppler-cpp-dev \
       locales \
       openssh-client \
       pandoc-citeproc \
       python3-apt \
       r-base-dev

RUN  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen en_US.utf8 \
  && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

RUN  R -e "install.packages('bspm')" \
  && echo "bspm::enable()" >> /etc/R/Rprofile.site \
  && R -e "install.packages(c('crminer', 'rmarkdown', 'rvest', 'snakecase', 'tidyRSS', 'urltools'))"

RUN mkdir -p /home/bibuser/.ssh

ENV HOME /home/bibuser

COPY update.sh /home/bibuser/update.sh
COPY known_hosts /home/bibuser/.ssh/known_hosts

RUN  chgrp -R 0 /home/bibuser \
  && chmod -R g=u /home/bibuser /etc/passwd

WORKDIR /home/bibuser

ENTRYPOINT ["./update.sh"]
