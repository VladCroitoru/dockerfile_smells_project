FROM httpd:2.4

RUN apt-get update

# Install all the things
RUN apt-get update -qq \
  && apt-get install -y git vim \
  perl libncurses5 libselinux1 libsepol1 apache2 libapache2-mod-perl2 libxml-libxml-perl libunicode-string-perl \
  libterm-readkey-perl libmime-lite-perl libmime-types-perl libdigest-sha-perl libdbd-mysql-perl libxml-parser-perl libxml2-dev \
  libxml-twig-perl libarchive-any-perl libjson-perl lynx wget ghostscript xpdf antiword elinks texlive-base texlive-base-bin \
  psutils imagemagick adduser tar gzip unzip libsearch-xapian-perl libtex-encode-perl libcgi-pm-perl liburi-perl \
  libapache2-mod-perl2 libnet-ldap-perl libdate-calc-perl mysql-client cron

# Setup build variables
ARG APP_WORKDIR=/opt/eprints3
ARG BRANCH
ARG EPUSER=eprints

# Create the $APACHE_RUN_USER
RUN adduser --disabled-password --gecos "" $EPUSER

# Copy the application
COPY . $APP_WORKDIR
COPY ./docker/SystemSettings.pm $APP_WORKDIR/perl_lib/EPrints/SystemSettings.pm
RUN echo "LoadModule perl_module /usr/lib/apache2/modules/mod_perl.so" | tee -a /usr/local/apache2/conf/httpd.conf >/dev/null

# Change ownership of application and apache2 directories
RUN chown -R $EPUSER:$EPUSER $APP_WORKDIR

WORKDIR $APP_WORKDIR

RUN git checkout $BRANCH
RUN git submodule update --init
