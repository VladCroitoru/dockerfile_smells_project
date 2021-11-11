FROM progrium/busybox
RUN opkg-install curl bash git lsof strace

RUN mkdir /busybox && \
    cp -r /bin /busybox && \
    cd /usr/bin && \
    cp curl git lsof strace opkg-cl opkg-install opkg-key /busybox/ && \
    cp -r /usr/lib /busybox/lib

VOLUME ["/busybox"]

CMD ["/bin/bash"]
