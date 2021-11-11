FROM opensuse:13.2
MAINTAINER Jeff Bonhag <jbonhag@sca-corp.com>

RUN zypper --gpg-auto-import-keys ref
RUN zypper --non-interactive in wget tar
RUN zypper --non-interactive in gcc gcc-c++ gettext make
RUN zypper --non-interactive in ca-certificates unzip autoconf libtool which apache2 apache2-devel

RUN useradd -m docker

USER docker
WORKDIR /home/docker
RUN wget http://download.mono-project.com/sources/mono/mono-3.6.0.tar.bz2
RUN tar xvf mono-3.6.0.tar.bz2
WORKDIR mono-3.6.0
RUN ./configure && make
USER root
RUN make install

USER docker
WORKDIR /home/docker
RUN wget https://github.com/mono/mod_mono/archive/3.8.zip
RUN unzip 3.8.zip
WORKDIR mod_mono-3.8
RUN ./autogen.sh
RUN make
USER root
RUN make install

USER docker
WORKDIR /home/docker
RUN wget https://github.com/mono/xsp/archive/3.0.11.zip
RUN unzip 3.0.11.zip
WORKDIR xsp-3.0.11
USER root
RUN zypper --non-interactive in sqlite3
USER docker
RUN ./autogen.sh
RUN make
USER root
RUN make install

# now, we dance
USER docker
RUN mkdir -p /home/docker/app
WORKDIR /home/docker/app
RUN wget https://github.com/jeffbonhag/wcfservice1/archive/master.zip
RUN unzip master.zip
WORKDIR wcfservice1-master

# BUILD
RUN xbuild

# DEPLOY
USER root
RUN zypper --non-interactive in ed
RUN mv WcfService1 /srv/www/htdocs/
RUN ed -s /etc/apache2/httpd.conf <<< $'185d\nw'
RUN echo Include /etc/apache2/mod_mono.conf >> /etc/apache2/httpd.conf
RUN echo MonoServerPath /usr/local/bin/mod-mono-server4 >> /etc/apache2/httpd.conf
RUN echo AddType application/x-asp-net .svc >> /etc/apache2/httpd.conf



# RUN
USER root
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D",  "FOREGROUND"]

