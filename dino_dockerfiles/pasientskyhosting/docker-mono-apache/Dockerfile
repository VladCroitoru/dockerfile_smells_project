FROM debian:jessie-slim
MAINTAINER Joakim Karlsson <jk@patientsky.com>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
    && echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots 4.8.1/main" > /etc/apt/sources.list.d/mono-xamarin.list \
    && echo "deb http://download.mono-project.com/repo/debian wheezy-apache24-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \
    && echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \
    && apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
         curl \
         tzdata \
         binutils \
         ca-certificates-mono \
         fsharp \
         mono-vbnc \
         referenceassemblies-pcl \
         apache2 \
         libapache2-mod-mono \
         mono-apache-server4 \
         mono-xsp4-base \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/tmp/* \
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

RUN a2enmod mod_mono \
    && service apache2 stop \
    && mkdir -p /etc/mono/registry /etc/mono/registry/LocalMachine \
    && sed -ri ' \
      s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
      s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
      ' /etc/apache2/apache2.conf

RUN rm -rf /etc/apache2/sites-enabled/000-default.conf
ADD ./config/apache2-site.conf /etc/apache2/sites-enabled/000-default.conf

WORKDIR /var/www
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
