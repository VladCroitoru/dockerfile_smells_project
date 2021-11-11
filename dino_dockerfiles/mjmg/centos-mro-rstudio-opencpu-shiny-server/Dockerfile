
FROM mjmg/centos-mro-base:latest

ENV MRO_VERSION 3.5.3
ENV MRO_HOME /opt/microsoft/ropen/$MRO_VERSION/lib64/R
# ENV MAKEFLAGS "-j$(nproc/2)"

ENV OPENCPU_VERSION 2.1.7-16.1
ENV RAPACHE_VERSION 1.2.7-2.1

ENV FEDORA_VERSION 32
ENV TCL_VERSION 8.6.10-1
ENV TK_VERSION 8.6.10-3

ENV RSTUDIO_SERVER_VERSION 1.3.959
ENV SHINY_SERVER_VERSION 1.5.13.944



RUN \
  dnf install -y dnf-plugins-core && \
  dnf config-manager --set-enabled PowerTools && \
  dnf clean all && \
  dnf update -y
  
RUN \
  dnf install -y yum-utils \
                 rpmdevtools \
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
                 git \
                 bzip2-devel \
                 libxml2-devel \
                 libssh2-devel \
                 libicu-devel \
                 tar \
                 curl \
                 mock \
                 #NLopt-devel \
                 https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/n/NLopt-2.4.2-2.el7.x86_64.rpm \
                 https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/n/NLopt-devel-2.4.2-2.el7.x86_64.rpm \
                 ncurses-compat-libs \
                 unixODBC-devel \
                 tcl-devel \
                 tk-devel


RUN \
  useradd -ms /bin/bash mockbuild

USER mockbuild

RUN \
  rpmdev-setuptree

COPY \
  R-fake.spec /tmp/R-fake.spec

RUN \
  rpmbuild -bb /tmp/R-fake.spec

USER root

RUN \
  cd /home/mockbuild/rpmbuild/RPMS/noarch/ && \
  rpm -ivh /home/mockbuild/rpmbuild/RPMS/noarch/R-fake*.rpm

USER mockbuild

RUN \
  cd /home/mockbuild/ && \
  wget http://download.opensuse.org/repositories/home:/jeroenooms:/opencpu-2.1/Fedora_$FEDORA_VERSION/src/rapache-$RAPACHE_VERSION.src.rpm && \ 
  wget http://download.opensuse.org/repositories/home:/jeroenooms:/opencpu-2.1/Fedora_$FEDORA_VERSION/src/opencpu-$OPENCPU_VERSION.src.rpm && \
  wget http://dl.fedoraproject.org/pub/fedora/linux/releases/$FEDORA_VERSION/Everything/source/tree/Packages/t/tcl-$TCL_VERSION.fc$FEDORA_VERSION.src.rpm && \
  wget http://dl.fedoraproject.org/pub/fedora/linux/releases/$FEDORA_VERSION/Everything/source/tree/Packages/t/tk-$TK_VERSION.fc$FEDORA_VERSION.src.rpm

USER root

#RUN \
#  rm /etc/yum.repos.d/CentOS-Sources.repo

RUN \
  dnf builddep -y --nogpgcheck /home/mockbuild/opencpu-$OPENCPU_VERSION.src.rpm

RUN \
  dnf builddep -y --nogpgcheck /home/mockbuild/rapache-$RAPACHE_VERSION.src.rpm

RUN \
  dnf builddep -y --nogpgcheck /home/mockbuild/tcl-$TCL_VERSION.fc$FEDORA_VERSION.src.rpm

RUN \
  ln $MRO_HOME/share/ /usr/share/R -s && \
  ln $MRO_HOME/lib/ /usr/lib/R -s && \
  ln $MRO_HOME/include /usr/lib/R/include -s

RUN \
  echo "$MRO_HOME/lib" >> /etc/ld.so.conf.d/microsoft-r-lib.conf && \
  ldconfig

USER mockbuild

RUN \
  cd ~ && \
  rpm -ivh rapache-$RAPACHE_VERSION.src.rpm && \
  QA_RPATHS=$[0x0001|0x0002] rpmbuild -ba ~/rpmbuild/SPECS/rapache.spec

RUN \
  cd ~ && \
  rpm -ivh opencpu-$OPENCPU_VERSION.src.rpm && \
  rpmbuild -ba ~/rpmbuild/SPECS/opencpu.spec

#RUN \
#  cd ~ && \
#  rpm -ivh tcl-$TCL_VERSION.fc$FEDORA_VERSION.src.rpm && \
#  rpmbuild -ba ~/rpmbuild/SPECS/tcl.spec

#USER root

#RUN \
#  dnf erase -y tcl tk && \
#  dnf install -y /home/mockbuild/rpmbuild/RPMS/x86_64/tcl-devel-$TCL_VERSION.el7.x86_64.rpm /home/mockbuild/rpmbuild/RPMS/x86_64/tcl-$TCL_VERSION.el7.x86_64.rpm

#RUN \
#  dnf builddep -y --nogpgcheck /home/mockbuild/tk-$TK_VERSION.fc$FEDORA_VERSION.src.rpm


#USER mockbuild

#RUN \
#  cd ~ && \
#  rpm -ivh tk-$TK_VERSION.fc$FEDORA_VERSION.src.rpm && \
#  rpmbuild -ba ~/rpmbuild/SPECS/tk.spec

USER root

RUN \
  dnf install -y MTA mod_ssl /usr/sbin/semanage && \
  dnf install -y /home/mockbuild/rpmbuild/RPMS/x86_64/rapache-*.rpm && \
  dnf install -y /home/mockbuild/rpmbuild/RPMS/x86_64/opencpu-lib-*.rpm && \
  dnf install -y /home/mockbuild/rpmbuild/RPMS/x86_64/opencpu-server-*.rpm 
  # && \
#  dnf install -y /home/mockbuild/rpmbuild/RPMS/x86_64/tk-devel-$TK_VERSION.el8.x86_64.rpm /home/mockbuild/rpmbuild/RPMS/x86_64/tk-$TK_VERSION.el8.x86_64.rpm

# Cleanup
RUN \
  rm -rf /home/mockbuild/* && \
  userdel mockbuild && \
  dnf erase mock -y && \
  dnf autoremove -y

# Configure default shiny user with password shiny
RUN \
  useradd -m shiny && \
  echo "shiny:shiny" | chpasswd

USER root

WORKDIR /tmp

RUN \
  wget https://download2.rstudio.org/server/centos8/x86_64/rstudio-server-rhel-$RSTUDIO_SERVER_VERSION-x86_64.rpm && \
  wget https://download3.rstudio.org/centos6.3/x86_64/shiny-server-$SHINY_SERVER_VERSION-x86_64.rpm

#RUN \
#  echo "Installing shiny from CRAN" && \
#  Rscript -e "install.packages('shiny', repos='https://cloud.r-project.org/')"

RUN \
  echo "Installing shiny from MRAN" && \
  Rscript -e "install.packages('shiny')"

# Add default root password with password r00tpassw0rd
RUN \
  echo "root:r00tpassw0rd" | chpasswd

RUN \
  dnf install -y --nogpgcheck /tmp/shiny-server-$SHINY_SERVER_VERSION-x86_64.rpm && \
  rm -f /tmp/shiny-server-$SHINY_SERVER_VERSION-x86_64.rpm

RUN \
  dnf install -y --nogpgcheck /tmp/rstudio-server-rhel-$RSTUDIO_SERVER_VERSION-x86_64.rpm && \
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
# Update SSL configuration
RUN \
  rm -f /etc/httpd/conf.d/ssl.conf
ADD \
  ./etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf
# Password protect shiny-server with shiny:shiny
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

# Workaround for library directory in MRO 3.4.X
#ADD \
#  .Rprofile /home/shiny/.Rprofile

USER root

# Link pandoc binaries from rstudio server
# https://github.com/rstudio/rmarkdown/blob/master/PANDOC.md
RUN \
  ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin && \
  ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin

# install useful R packages
ADD \
  installRpackages.sh /tmp/installRpackages.sh
RUN \
  chmod +x /tmp/installRpackages.sh && \
  sync && \
  /tmp/installRpackages.sh

# install Chemometrics R packages
ADD \
  installChempackages.sh /tmp/installChempackages.sh
RUN \
  chmod +x /tmp/installChempackages.sh && \
  sync
#RUN \
#  /tmp/installChempackages.sh

# install useful machine learning packages
ADD \
  installMLpackages.sh /tmp/installMLpackages.sh
RUN \
  chmod +x /tmp/installMLpackages.sh && \
  sync
#RUN \
#  /tmp/installMLpackages.sh

# Define default command.
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]

