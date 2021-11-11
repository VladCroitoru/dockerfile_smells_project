# Custom boot2docker image with https://github.com/gewo/living-in-a-box.
FROM boot2docker/boot2docker

ENV ADDITIONAL_TCZ_DEPS readline ncurses bash

RUN for dep in $ADDITIONAL_TCZ_DEPS; do \
  echo "Download $TCL_REPO_BASE/tcz/$dep.tcz" &&\
  curl -L -o /tmp/$dep.tcz $TCL_REPO_BASE/tcz/$dep.tcz &&\
  unsquashfs -f -d $ROOTFS /tmp/$dep.tcz &&\
  rm -f /tmp/$dep.tcz ;\
done

RUN \
  git clone https://github.com/gewo/living-in-a-box.git $ROOTFS/opt/living-in-a-box &&\
  ln -s /opt/living-in-a-box/bin/dev $ROOTFS/usr/local/bin/dev

RUN /make_iso.sh

CMD ["cat", "/boot2docker.iso"]
