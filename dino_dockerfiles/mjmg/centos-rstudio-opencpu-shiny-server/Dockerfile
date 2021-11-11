FROM mjmg/centos-r-base:latest

ENV OPENCPU_VERSION 2.0.6-26.1
ENV RAPACHE_VERSION 1.2.7-2.1
ENV RSTUDIO_SERVER_VERSION 1.1.383
ENV SHINY_SERVER_VERSION 1.5.5.872
ENV FEDORA_VERSION 27

RUN \
  yum clean all && \
  yum update -y && \
  yum install -y yum-utils \
                 rpmdevtools \
                 make \
                 R-devel \
                 httpd-devel \
                 libapreq2-devel \
                 libcurl-devel \
                 protobuf-devel \
                 openssl-devel \
                 libpng-devel \
                 libtiff-devel \
                 libjpeg-turbo-devel \
                 fftw-devel \
                 mesa-libGLU-devel \
                 ed \
                 netcdf-devel \
                 tk-devel \
                 git \
                 NLopt-devel

RUN \
  useradd -ms /bin/bash mockbuild

USER mockbuild

RUN \
  rpmdev-setuptree

USER mockbuild

RUN \
  cd /home/mockbuild/ && \
  wget http://download.opensuse.org/repositories/home:/jeroenooms:/opencpu-2.0/Fedora_$FEDORA_VERSION/src/rapache-$RAPACHE_VERSION.src.rpm && \ 
  wget http://download.opensuse.org/repositories/home:/jeroenooms:/opencpu-2.0/Fedora_$FEDORA_VERSION/src/opencpu-$OPENCPU_VERSION.src.rpm

USER root

RUN \
  yum-builddep -y --nogpgcheck /home/mockbuild/opencpu-$OPENCPU_VERSION.src.rpm

RUN \
  yum-builddep -y --nogpgcheck /home/mockbuild/rapache-$RAPACHE_VERSION.src.rpm


USER mockbuild

RUN \
  cd ~ && \
  rpm -ivh rapache-$RAPACHE_VERSION.src.rpm && \
  rpmbuild -ba ~/rpmbuild/SPECS/rapache.spec

RUN \
  cd ~ && \
  rpm -ivh opencpu-$OPENCPU_VERSION.src.rpm && \
  rpmbuild -ba ~/rpmbuild/SPECS/opencpu.spec
  
USER root

RUN \
  yum install -y MTA mod_ssl /usr/sbin/semanage && \
  yum install -y /home/mockbuild/rpmbuild/RPMS/x86_64/rapache-*.rpm && \
  yum install -y /home/mockbuild/rpmbuild/RPMS/x86_64/opencpu-lib-*.rpm && \
  yum install -y /home/mockbuild/rpmbuild/RPMS/x86_64/opencpu-server-*.rpm 

# Cleanup
RUN \
  rm -rf /home/mockbuild/* && \
  userdel mockbuild && \
  yum erase mock -y && \
  yum autoremove -y

# Configure default shiny user with password shiny
RUN \
  useradd -m shiny && \
  echo "shiny:shiny" | chpasswd

USER root

WORKDIR /tmp

RUN \
  wget https://download2.rstudio.org/rstudio-server-rhel-$RSTUDIO_SERVER_VERSION-x86_64.rpm && \
  wget https://download3.rstudio.org/centos5.9/x86_64/shiny-server-$SHINY_SERVER_VERSION-rh5-x86_64.rpm


RUN \
  echo "Installing shiny from CRAN" && \
  Rscript -e "install.packages('shiny', repos='https://cloud.r-project.org/')"

#RUN \
#  echo "Installing shiny from MRAN" && \
#  Rscript -e "install.packages('shiny')"

# Add default root password with password r00tpassw0rd
RUN \
  echo "root:r00tpassw0rd" | chpasswd

RUN \
  yum install -y --nogpgcheck /tmp/shiny-server-$SHINY_SERVER_VERSION-rh5-x86_64.rpm && \
  rm -f /tmp/shiny-server-$SHINY_SERVER_VERSION-rh5-x86_64.rpm

RUN \
  yum install -y --nogpgcheck /tmp/rstudio-server-rhel-$RSTUDIO_SERVER_VERSION-x86_64.rpm && \
  rm -f /tmp/rstudio-server-rhel-$RSTUDIO_SERVER_VERSION-x86_64.rpm


# Server ports
EXPOSE 80 443 9001


# Add supervisor conf files
ADD \
  ./etc/supervisor/conf.d/rstudio-server.conf /etc/supervisor/conf.d/rstudio-server.conf
ADD \
  ./etc/supervisor/conf.d/opencpu-server-httpd.conf /etc/supervisor/conf.d/opencpu-server-httpd.conf
ADD \
  ./etc/supervisor/conf.d/shiny-server.conf /etc/supervisor/conf.d/shiny-server.conf

# Update rstudio server configuration
RUN \
  rm -f /etc/httpd/conf.d/rstudio.conf
ADD \
  ./etc/httpd/conf.d/rstudio-server.conf /etc/httpd/conf.d/rstudio-server.conf
# Use SSL and password protect shiny-server with shiny:shiny
ADD \
  ./etc/httpd/conf.d/shiny-httpd.conf /etc/httpd/conf.d/shiny-httpd.conf
ADD \
  ./etc/httpd/conf.d/shinypasswd /etc/httpd/conf.d/shinypasswd
# Force SSL for everything
ADD \
  ./etc/httpd/conf.d/force-ssl.conf /etc/httpd/conf.d/force-ssl.conf

RUN \
  mkdir -p /var/log/shiny-server && \
  chown shiny:shiny /var/log/shiny-server && \
  mkdir /srv/shiny-server/apps/ && \
  mkdir /srv/shiny-server/rmd/ && \
  chown shiny:shiny -R /srv/shiny-server && \
  chmod 777 -R /srv/shiny-server && \
  chown shiny:shiny -R /opt/shiny-server/ && \
  chmod 777 -R /opt/shiny-server/samples/sample-apps

USER shiny

RUN \
  mkdir /home/shiny/shiny-server/ && \
  ln /srv/shiny-server/apps /home/shiny/shiny-server/apps -s && \
  ln /srv/shiny-server/rmd /home/shiny/shiny-server/rmd -s

#ADD \
#  .Rprofile /home/shiny/.Rprofile

USER root

# install useful R packages
ADD \
  installRpackages.sh /tmp/installRpackages.sh
RUN \
  chmod +x /tmp/installRpackages.sh && \
  sync && \
  /tmp/installRpackages.sh


# install Chemometrics R packages
#ADD \
#  installChempackages.sh /tmp/installChempackages.sh
#RUN \
#  chmod +x /tmp/installChempackages.sh && \
#  /tmp/installChempackages.sh


# install useful machine learning packages
#ADD \
#  installMLpackages.sh /tmp/installMLpackages.sh
#RUN \
#  chmod +x /tmp/installMLpackages.sh && \
#  /tmp/installMLpackages.sh


# Define default command.
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]


