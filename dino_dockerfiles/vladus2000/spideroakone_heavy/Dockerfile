FROM vladus2000/arch-base-yay
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /

RUN /install-devel.sh && \
	su - evil -c 'yay -S --needed --noconfirm lftp python2-boto python2-gobject deja-dup duply borg openssh python-llfuse spideroak-one su-exec procps' && \
	chmod +x /startup.sh /runit.sh && \
	/rm-devel.sh

CMD /bin/bash -c /startup.sh

