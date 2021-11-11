FROM armbuild/ubuntu:latest

# PREPARE IMAGE
ADD qemu-arm-static/qemu-arm-static /usr/bin/qemu-arm-static
ADD wrapper/wrapper-i386 /bin/sh
ADD ld_wrapper/ld_wrapper.so /bin/ld_wrapper.so
ADD binproxy /binproxy
ENV PATH /binproxy
#ENV LD_PRELOAD /bin/ld_wrapper.so

# STANDARD COMMANDS
RUN sh -c 'echo Hello World !'
RUN echo Hello World !
RUN echo Hello World !
RUN echo Hello World !
RUN date
RUN /bin/date
RUN /bin/bash -c /bin/date
RUN bash -c /bin/date
RUN /bin/sh -c /bin/date
RUN sh -c /bin/date
# RUN apt-get install -y cowsay # -> failing with: Failed to exec method /usr/lib/apt/methods/http
CMD ["bash"]

# CLEAN IMAGE
# FIXME: clean the /bin/sh (we should add an option to the wrapper that will take care of this
# RUN env --unset=PATH
ENV PATH /bin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/sbin
