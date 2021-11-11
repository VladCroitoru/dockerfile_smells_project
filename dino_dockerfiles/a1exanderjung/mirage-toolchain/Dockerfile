FROM centos:7

ENV WORKSPACE /opam/app

RUN yum groupinstall -y 'Development Tools'
RUN yum install -y sudo git patch texinfo wget ocaml ocaml-camlp4-devel \
    ocaml-ocamldoc
RUN git clone -b 1.2 git://github.com/ocaml/opam /tmp/opam
RUN bash -c "cd /tmp/opam && make cold && make prefix=\"/usr\" install && rm -rf /tmp/opam"
RUN sed -i.bak '/LC_TIME LC_ALL LANGUAGE/aDefaults env_keep += "OPAMYES OPAMJOBS OPAMVERBOSE"' /etc/sudoers
RUN echo 'opam ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/opam
RUN chmod 440 /etc/sudoers.d/opam && chown root:root /etc/sudoers.d/opam
RUN sed -i.bak 's/^Defaults.*requiretty//g' /etc/sudoers
RUN rm -Rfv /opam && mkdir /opam
RUN useradd -d /opam -s /bin/bash opam
RUN chown -R opam:opam /opam
RUN passwd -l opam
RUN su - opam -c 'opam init -y && opam switch 4.03.0'
RUN su - opam -c 'opam install -y \
    mirage \
    mirage-block \
    mirage-block-lwt \
    mirage-block-ramdisk \
    mirage-block-solo5 \
    mirage-block-unix \
    mirage-block-xen \
    mirage-bootvar-solo5 \
    mirage-bootvar-xen \
    mirage-btrees \
    mirage-channel \
    mirage-channel-lwt \
    mirage-clock \
    mirage-clock-freestanding \
    mirage-clock-lwt \
    mirage-clock-unix \
    mirage-console \
    mirage-console-lwt \
    mirage-console-solo5 \
    mirage-console-unix \
    mirage-console-xen \
    mirage-console-xen-proto \
    mirage-device \
    mirage-entropy \
    mirage-flow \
    mirage-flow-lwt \
    mirage-flow-rawlink \
    mirage-flow-unix \
    mirage-fs \
    mirage-fs-lwt \
    mirage-fs-unix \
    mirage-kv \
    mirage-kv-lwt \
    mirage-logs \
    mirage-net \
    mirage-net-flow \
    mirage-net-lwt \
    mirage-net-solo5 \
    mirage-net-unix \
    mirage-net-xen \
    mirage-os-shim \
    mirage-profile \
    mirage-protocols \
    mirage-protocols-lwt \
    mirage-random \
    mirage-runtime \
    mirage-solo5 \
    mirage-stack \
    mirage-stack-lwt \
    mirage-time \
    mirage-time-lwt \
    mirage-types \
    mirage-types-lwt \
    mirage-unix \
    mirage-vnetif \
    mirage-xen \
    tcpip \
    depext'

VOLUME $WORKSPACE
WORKDIR $WORKSPACE
ADD exec.sh /opam
ENTRYPOINT ["/opam/exec.sh"]
USER opam:opam
