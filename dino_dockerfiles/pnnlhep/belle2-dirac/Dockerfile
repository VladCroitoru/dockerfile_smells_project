FROM pnnlhep/osg-ce:latest
MAINTAINER Malachi Schram "malachi.schram@pnnl.gov”

## Create Belle user in docker ##
RUN groupadd -r belle -g 700
RUN useradd -r -g belle -u 700 -c "belle service account" \
    -s /sbin/nologin -d /home/belle belle

## Create DIRAC user in docker ##
RUN groupadd -r dirac -g 50000
RUN useradd -r -g dirac -u 50000 -c "dirac service account" \
    -s /sbin/nologin -d /home/dirac dirac

## Preparing DIRAC directories ##
RUN echo “Installing DIRAC”
ADD ./FakeSiteDirector.cfg /srv/dirac/FakeSiteDirector.cfg
ADD ./my_install_dirac.sh /srv/dirac/my_install_dirac.sh
ADD ./condor.patch /tmp/condor.patch
RUN mkdir -p /opt/dirac; \
    chown -R belle.belle /opt/dirac; \
    mkdir -p /srv/dirac; \
    chown -R belle.belle /srv/dirac; \
    cd /srv/dirac; \
    wget -O dirac-install 'https://github.com/DIRACGrid/DIRAC/raw/integration/Core/scripts/dirac-install.py' || exit ;\
    chmod +x dirac-install; \
    chmod +x /srv/dirac/my_install_dirac.sh; \
    ./my_install_dirac.sh; \
    cd /; patch -p0 < /tmp/condor.patch; \
    rm -f /tmp/condor.patch

# Add the setup scripts to finish install/cfg DIRAC using docker_compose
ADD ./final_install.sh /opt/dirac/sbin/final_install.sh
## Belle 2 hack 
ADD ./LocalComputingElement-v6r17.py /opt/dirac/pro/DIRAC/Resources/Computing/LocalComputingElement.py
ADD ./SiteDirector-v6r17.py /opt/dirac/pro/DIRAC/WorkloadManagementSystem/Agent/SiteDirector.py


