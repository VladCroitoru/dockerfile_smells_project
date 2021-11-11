FROM gliderlabs/alpine
RUN apk --update add curl bash
ENV USER root
ENV NUM_NIXBUILDERS 10
ADD docker-provision.sh /tmp/
RUN /tmp/docker-provision.sh
CMD ["/bin/bash"]
