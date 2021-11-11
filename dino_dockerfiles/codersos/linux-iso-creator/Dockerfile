FROM codersos/ubuntu-remix

RUN apt-get -qq -y install squashfs-tools && apt-get clean

#RUN apt-get -qq update && \
#    apt-get --yes upgrade && \
#    apt-get -y -qq install --no-install-recommends syslinux squashfs-tools genisoimage && \
#    apt-get -y -qq install --no-install-recommends ubuntu-standard casper lupin-casper discover laptop-detect os-prober linux-generic && \
#    apt-get -y -qq install --no-install-recommends network-manager && \
#    apt-get clean

RUN mkdir /toiso
#ADD toiso/configuration.sh /toiso/configuration.sh
#ADD toiso/remove_linux_kernels.sh /toiso/remove_linux_kernels.sh
#RUN /toiso/remove_linux_kernels.sh
#ADD toiso/clean_up.sh /toiso/clean_up.sh
#RUN /toiso/clean_up.sh
#ADD toiso/download_iso.sh /toiso/download_iso.sh
#RUN /toiso/download_iso.sh
ADD toiso/* /toiso/

CMD /toiso/command.sh
