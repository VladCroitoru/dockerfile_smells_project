
# Analogous to jupyter/systemuser, but based on SLC6 and inheriting directly from cernphsft/notebook.
# Run with the DockerSpawner in JupyterHub.

FROM cernphsft/notebook:v2.4

MAINTAINER Enric Tejedor Saavedra <enric.tejedor.saavedra@cern.ch>

# Disable requiretty and secure path - required by systemuser.sh
RUN yum -y install sudo && \
    sed -i'' '/Defaults \+requiretty/d'  /etc/sudoers && \
    sed -i'' '/Defaults \+secure_path/d' /etc/sudoers

# Install ROOT prerequisites
RUN yum -y install \
    libXpm \
    libXft

# Install bs4 - required by sparkconnector.serverextension
RUN pip3 install bs4

# Install tk - required by matplotlib
RUN yum -y install tk

# Install Cloudera dependencies - required by IT Spark clusters
RUN yum -y  install \
            alsa-lib \
            at \
            bc \
            cronie \
            cronie-anacron \
            crontabs \
            cvs \
            db4-cxx \
            db4-devel \
            ed \
            file \
            gdbm-devel \
            gettext \
            jpackage-utils \
            libXi \
            libXtst \
            man \
            passwd \
            pax \
            perl-CGI \
            perl-ExtUtils-MakeMaker \
            perl-ExtUtils-ParseXS \
            perl-Test-Harness \
            perl-Test-Simple \
            perl-devel \
            redhat-lsb-core \
            rsyslog \
            time \
            xz \
            xz-lzma-compat

# Install openmotif - required by Geant4 (libXm)
RUN yum -y install openmotif

# Install libaio - required by Oracle
RUN yum -y install libaio

# Install cern-get-sso-cookie and update CERN CA certs - ATLAS TDAQ, UCA-63
RUN yum -y install cern-get-sso-cookie && \
    yum -y update CERN-CA-certs

# Create truststore for NXCALS Spark connection
RUN yum -y install java-1.8.0-openjdk && \
    keytool -import -alias cerngridCA -file /etc/pki/tls/certs/CERN_Grid_Certification_Authority.crt \
        -keystore /etc/pki/tls/certs/truststore.jks -storepass 'password' -noprompt && \
    keytool -import -alias cernRootCA2 -file /etc/pki/tls/certs/CERN_Root_Certification_Authority_2.crt \
        -keystore /etc/pki/tls/certs/truststore.jks -storepass 'password' -noprompt && \
    yum -y erase java-1.8.0-openjdk && \
    rm -rf /usr/lib/jvm/

# Install HEP_OSlibs - includes atlas blas
RUN yum -y install HEP_OSlibs_SL6

# WORKAROUND
# Hide from Jupyter the Python3 kernel by hand
RUN mv /usr/local/lib/python3.6/site-packages/ipykernel /usr/local/lib/python3.6/site-packages/ipykernelBACKUP && \
    mv /usr/local/share/jupyter/kernels /usr/local/share/jupyter/kernelsBACKUP

# Add ipykernel and its dependencies to an isolated place referenced by PYTHONPATH in user env (Py3)
# Needed to prevent updated Jupyter code to break with older LCG versions (this way it picks always the correct pkgs)
RUN mkdir /usr/local/lib/swan && \
    pip3 install 'ipykernel==4.8.2' -t /usr/local/lib/swan

RUN yum clean all && \
    rm -rf /var/cache/yum

EXPOSE 8888

ENV SHELL /bin/bash

ADD systemuser.sh /srv/singleuser/systemuser.sh
ADD userconfig.sh /srv/singleuser/userconfig.sh
WORKDIR /root
CMD ["sh", "/srv/singleuser/systemuser.sh"]
