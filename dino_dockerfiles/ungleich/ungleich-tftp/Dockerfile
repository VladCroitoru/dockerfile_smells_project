FROM ungleich/ungleich-ipxe

MAINTAINER Carlos Ortigoza "carlos.ortigoza@ungleich.ch"

RUN apt-get update \
	&& apt-get install --no-install-recommends -y tftpd-hpa \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

VOLUME /var/lib/tftpboot

EXPOSE 69/udp

ENTRYPOINT ["/root/ipxe_script_builder.sh"]
