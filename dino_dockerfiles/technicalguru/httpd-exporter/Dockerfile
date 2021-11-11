FROM perl:latest

# Install Perl
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        libtext-unidecode-perl \
        libencode-detect-perl  \
    && rm -r /var/lib/apt/lists/*

# Install Perl modules
RUN curl -L http://cpanmin.us | perl - App::cpanminus
RUN cpanm Text::Unidecode \
    && cpanm Encode::Detect \
    && cpanm JSON \
    && cpanm JSON::XS

# Install
RUN mkdir /usr/local/httpd-exporter \
    && mkdir /usr/local/httpd-exporter/modules \
    && mkdir /usr/local/httpd-exporter/test    \
    && mkdir /usr/local/httpd-exporter/help    \
    && mkdir /usr/local/httpd-exporter/contrib \
    && mkdir /usr/local/httpd-exporter/examples

COPY exporterd.pl /usr/local/httpd-exporter/
COPY modules/*    /usr/local/httpd-exporter/modules/
COPY test/*       /usr/local/httpd-exporter/test/
COPY help/*       /usr/local/httpd-exporter/help/
COPY contrib/*    /usr/local/httpd-exporter/contrib/
COPY examples/*   /usr/local/httpd-exporter/examples/

RUN chmod 755 /usr/local/httpd-exporter/*.pl

# Configuration dir
RUN mkdir /etc/httpd-exporter
RUN chmod 777 /etc/httpd-exporter

# Test
RUN /usr/local/httpd-exporter/exporterd.pl --test

# Run as root (unfortunately) to make sure we can read and write the mounted dirs
WORKDIR /usr/local/httpd-exporter
CMD /usr/local/httpd-exporter/exporterd.pl

