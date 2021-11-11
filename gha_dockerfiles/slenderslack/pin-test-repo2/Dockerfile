FROM ubuntu:devel
ARG REVISION
ARG SOURCE
LABEL org.opencontainers.image.revision=$REVISION
LABEL org.opencontainers.image.source=$SOURCE
RUN echo '{:repo "pin-test-repo2" :base "base2" :version 66}' > dog.json
CMD ["cat", "dog.json"]
