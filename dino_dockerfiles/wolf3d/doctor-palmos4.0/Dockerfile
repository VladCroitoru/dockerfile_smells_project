# Pull base image
FROM wolf3d/palmos.sdk.4.0

RUN mkdir -p /root/build
ADD hello.c /root/build/hello.c

RUN cd /root/build && m68k-palmos-gcc hello.c -o hello && \
    m68k-palmos-obj-res hello && \
    build-prc hello.prc "Hello, World" WRLD *.hello.grc
CMD ["/bin/bash"]
