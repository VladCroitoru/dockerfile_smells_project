FROM openshift/origin:latest

MAINTAINER Diego Castro <diego.castro@getupcloud.com>

ENV \
    # Path to be used in other layers to place s2i scripts into
    HOME=/opt/eventhub \
    PATH=/opt/eventhub/bin:/opt/app-root/bin:$PATH
 
USER root

RUN INSTALL_PKGS="python-pip python-virtualenv" && \
  yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && yum clean all -y && \
  mkdir -p ${HOME}/.pki/nssdb && \
  chown -R 1001:0 ${HOME}/.pki && \
  useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
      -c "Default Application User" default && \
  chown -R 1001:0 /opt/eventhub

# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH
COPY bin/ /usr/bin/
COPY src/ $HOME/

WORKDIR ${HOME}

RUN build

RUN fix-permissions ./

USER 1001

ENTRYPOINT ["container-entrypoint"]
CMD ["run"]