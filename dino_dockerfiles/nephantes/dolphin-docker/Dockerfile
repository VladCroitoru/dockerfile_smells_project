FROM ubuntu:trusty
 
MAINTAINER Alper Kucukural <alper.kucukural@umassmed.edu>

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get dist-upgrade
 
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for debugging the container.
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-php5 php5-mcrypt\
                    php5-mysqlnd php5-gd php-pear php-apc php5-curl curl lynx-cur mysql-server \
                    libreadline-dev libsqlite3-dev libbz2-dev libssl-dev python python-dev \
                    libmysqlclient-dev python-pip git expect default-jre \
                    libxml2-dev software-properties-common gdebi-core wget awscli s3cmd \
                    tree vim libv8-dev subversion g++ gcc gfortran zlib1g-dev libreadline-dev \
                    libx11-dev xorg-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-openssl-dev \
                    default-jdk texinfo texlive-latex-base texlive-latex-recommended texlive-fonts-extra \
                    texlive-fonts-recommended r-cran-plyr r-cran-reshape2 ccache libpam0g-dev 
 
RUN add-apt-repository ppa:marutter/rrutter

RUN apt-get clean

## Download R-devel
RUN cd /tmp \
	&& wget https://stat.ethz.ch/R/daily/R-devel.tar.gz \
        && tar xvfz R-devel.tar.gz 

## Build and install 
RUN cd /tmp/R-devel \
	&& R_PAPERSIZE=letter				\
	R_BATCHSAVE="--no-save --no-restore" 		\
	R_BROWSER=xdg-open				\
	PAGER=/usr/bin/pager				\
	PERL=/usr/bin/perl				\
	R_UNZIPCMD=/usr/bin/unzip			\
	R_ZIPCMD=/usr/bin/zip				\
	R_PRINTCMD=/usr/bin/lpr				\
	LIBnn=lib					\
	AWK=/usr/bin/awk                                \
	CC="ccache gcc"					\
	CFLAGS="-ggdb -pipe -std=gnu99 -Wall -pedantic" \
	CXX="ccache g++"				\
	CXXFLAGS="-ggdb -pipe -Wall -pedantic" 		\
	FC="ccache gfortran"	 	  		\
	F77="ccache gfortran"				\
	MAKE="make -j4"					\
	./configure 					\
   		--prefix=/usr/local/lib/R-devel 	\
   		 --enable-R-shlib 			\
    		--with-blas 				\
    		--with-lapack 				\
    		--with-readline 			\
    		--without-recommended-packages          \
                --disable-openmp                        \
	&& make \
	&& make install \
	&& make clean

## Set Renviron to get libs from base R install
RUN export R_LIBS_SITE=${R_LIBS_SITE-'/usr/lib/R-devel/lib/R/library:/usr/local/lib/R/site-library:/usr/lib/R/site-library::/usr/lib/R/library'}
RUN export PATH="/usr/local/lib/R-devel/bin:$PATH"
RUN cp /usr/local/lib/R-devel/bin/R /usr/bin/.
RUN cp /usr/local/lib/R-devel/bin/Rscript /usr/bin/.

RUN pip install MySQL-python

# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite


# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php5/apache2/php.ini
 
# Manually set up the apache environment variables
ENV PATH=$PATH:/usr/local/bin/dolphin-bin
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV DOLPHIN_PARAMS_SECTION=Docker


EXPOSE 80
EXPOSE 3306
EXPOSE 3838

#Install R Packages
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN R -e 'install.packages(c("ggvis", "ggplot2", "RColorBrewer", "DT", "gplots", "data.table", "devtools", "V8"), dependencies = TRUE )'
RUN R -e 'source("http://bioconductor.org/biocLite.R"); biocLite("debrowser");'
#RUN R -e 'source("http://bioconductor.org/biocLite.R"); biocLite("methylKit");'

# Update the default apache site with the config we created.
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

RUN echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/fqdn.conf
RUN a2enconf fqdn
RUN echo "export DOLPHIN_PARAMS_SECTION="${DOLPHIN_PARAMS_SECTION} >> /etc/apache2/envvars

RUN mkdir -p /var/www/.java/.systemPrefs
RUN mkdir /var/www/.java/.userPrefs
RUN chmod -R 755 /var/www/.java
RUN chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /var/www
RUN echo "export JAVA_OPTS=\"-Djava.util.prefs.systemRoot=/var/www/.java Djava.util.prefs.userRoot=/var/www/.java/.userPrefs\"" >> /etc/apache2/envvars

ENV RSTUDIO_VER=rstudio-server-1.0.136-amd64.deb
RUN wget https://download2.rstudio.org/${RSTUDIO_VER}
RUN gdebi -n ${RSTUDIO_VER}
RUN rm ${RSTUDIO_VER}
#RUN echo 'LANG=en_US.UTF-8\nLC_ALL=en_US.UTF-8' > /etc/default/locale
RUN echo 'server-app-armor-enabled=0' > /etc/rstudio/rserver.conf
RUN ln -s  /usr/lib/rstudio-server/extras/init.d/debian/rstudio-server /etc/init.d/.

ENV SHINY_VER=shiny-server-1.5.2.837-amd64.deb
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/${SHINY_VER}
RUN gdebi -n ${SHINY_VER}
RUN rm ${SHINY_VER}
RUN ln -s /opt/shiny-server/config/init.d/debian/shiny-server /etc/init.d/.

RUN pip install -U boto
RUN pip install numpy

# Install phpMyAdmin

RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && \
    service apache2 start && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install phpmyadmin && \ 
    zcat /usr/share/doc/phpmyadmin/examples/create_tables.sql.gz|mysql -uroot

RUN sed -i "s#// \$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#g" /etc/phpmyadmin/config.inc.php 
RUN ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-enabled/phpmyadmin.conf
RUN php5enmod mcrypt

 
# Copy site into place.
ENV GITUSER=UMMS-Biocore
ADD bin /usr/local/bin
RUN git clone https://github.com/${GITUSER}/dolphin-bin /usr/local/bin/dolphin-bin
RUN cd /usr/local/bin/dolphin-bin/MACS2 && python setup.py install
RUN cd /usr/local/bin/dolphin-bin/RSeQC-2.6.2 && python setup.py install
RUN make -C /usr/local/bin/dolphin-bin/RSEM-1.2.29
RUN git clone https://github.com/${GITUSER}/dolphin-tools /usr/local/share/dolphin_tools
RUN git clone https://github.com/rmccue/Requests.git /usr/local/share/Requests
RUN wget http://hgwdev.cse.ucsc.edu/~galt/encode3/validatePackage/validateEncode3-latest.tgz -P /usr/local/share/validateEncode
RUN tar -xvzf /usr/local/share/validateEncode/validateEncode3-latest.tgz -C /usr/local/share/validateEncode

RUN git clone https://github.com/${GITUSER}/dolphin-ui.git /var/www/html/dolphin
RUN git clone https://github.com/${GITUSER}/debrowser.git /srv/shiny-server/debrowser
RUN R CMD INSTALL /srv/shiny-server/debrowser
RUN sed -i "s/#library/library/" /srv/shiny-server/debrowser/R/server.R
RUN mkdir -p /var/www/html/dolphin/tmp/files /var/www/html/dolphin/tmp/logs /export/tmp/logs
RUN chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /var/www/html/dolphin
RUN chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /usr/local/share/dolphin_tools

RUN apt-get -y autoremove

RUN echo "locale-gen en_US.UTF-8"
RUN echo "dpkg-reconfigure locales"

# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN curl -s https://get.nextflow.io | bash 
RUN mv /data/nextflow /usr/bin/.
