FROM ubuntu:16.04
MAINTAINER Phusion <info@phusion.nl>

ADD . /bd_build

RUN chmod +x /bd_build/prepare.sh && \
	chmod +x /bd_build/system_services.sh && \
	chmod +x /bd_build/utilities.sh && \
	chmod +x /bd_build/fix_pam_bug.sh && \
	chmod +x /bd_build/cleanup.sh

RUN /bd_build/prepare.sh && \
	/bd_build/system_services.sh && \
	/bd_build/utilities.sh && \
	/bd_build/fix_pam_bug.sh && \
	/bd_build/cleanup.sh

CMD ["/sbin/my_init"]
