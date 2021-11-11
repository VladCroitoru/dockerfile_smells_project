FROM ubuntu:16.04

ENV PACKER_VERSION=1.1.3
ENV PACKER_SHA256SUM=b7982986992190ae50ab2feb310cb003a2ec9c5dcba19aa8b1ebb0d120e8686f

ENV OVFTOOL_VERSION 4.1.0-2459827
ENV OVFTOOL_INSTALLER vmware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle
# checksum verified at https://my.vmware.com/group/vmware/details?downloadGroup=OVFTOOL410&productId=491
ENV OVFTOOL_SHA1SUM=b907275c8d744bb54717d24bb8d414b19684fed4

RUN apt-get update && apt-get -y install unzip && apt-get clean

ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip ./
RUN echo "${PACKER_SHA256SUM} packer_${PACKER_VERSION}_linux_amd64.zip" | sha256sum -c -

RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip

ADD https://storage.googleapis.com/mortarchive/pub/ovftool/${OVFTOOL_INSTALLER} ./
RUN echo "${OVFTOOL_SHA1SUM} ${OVFTOOL_INSTALLER}" | sha1sum -c -

RUN sh ${OVFTOOL_INSTALLER} -p /usr/local --console --eulas-agreed --required
RUN rm ${OVFTOOL_INSTALLER}

ENTRYPOINT ["/bin/packer"]
