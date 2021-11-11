FROM ubuntu:20.04 as builder

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        gcc \
        g++ \
        libcgi-pm-perl \
        libgd-perl \
        libgraphviz-perl \
        make \
        wget

WORKDIR /
RUN wget https://cpan.metacpan.org/authors/id/S/SH/SHERLOCK/GO-TermFinder-0.86.tar.gz \
    && tar xvfz GO-TermFinder-0.86.tar.gz

WORKDIR /GO-TermFinder-0.86
RUN perl Makefile.PL \
    && make \
    && make install

#####

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove \
    && apt-get install -y \
        apache2 \
        build-essential \
        git \
        graphviz \
        libapache2-mod-wsgi-py3 \
        libcgi-pm-perl \
        libdata-stag-perl \
        libfile-which-perl \
        libgd-perl \
        libgo-perl \
        libgraphviz-perl \
        libio-string-perl \
        libipc-run-perl \
        net-tools \
        python3-pip \
    && pip3 install Flask \
    && pip3 install -U flask-cors \
    && pip3 install virtualenv

WORKDIR /usr/local/lib/x86_64-linux-gnu/perl/5.30.0
COPY --from=builder /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 .

WORKDIR /var/www
COPY www /var/www/

WORKDIR /var/www/tmp
RUN chmod 1777 .

WORKDIR /etc/apache2/sites-available
COPY FlaskApp.conf .

WORKDIR /var/www/FlaskApp/FlaskApp
RUN a2enmod wsgi \
    && a2ensite FlaskApp \
    && a2dissite 000-default \
    && virtualenv venv \
    && . venv/bin/activate

WORKDIR /

CMD ["apachectl", "-D", "FOREGROUND"]
