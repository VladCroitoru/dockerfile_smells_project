### Storage container.
#       This container does nothing but store files.
#       /bin/sh has been replaced with an asm program that simply ...
#
#               mov    rax,34 ; pause() syscall
#               syscall

FROM fedora:latest AS builder
RUN sudo dnf -y update
RUN sudo dnf -y install nasm binutils
COPY pause.asm /pause.asm
RUN nasm -f elf64 /pause.asm && \
    ld -s -o /pause /pause.o

FROM scratch
MAINTAINER frameloss
COPY --from=builder /pause /bin/sh
VOLUME /share
COPY share/ /share/
USER 65535
CMD ['']

