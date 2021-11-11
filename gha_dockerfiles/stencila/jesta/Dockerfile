# A Dockerfile for Jesta
#
# Get help:
#
#    docker run -it --rm stencila/jesta
#
# Execute a document in the current working directory:
#
#    docker run -it --rm -v$PWD:/work -w/work stencila/jesta execute document.json
#
# Whilst, in theory, the built binary should be able to run in an image
# that is `FROM scratch` or `FROM alpine`. That couldn't get made to work.
# In any case, since most of our images are based off `ubuntu` there should
# be good cache sharing.

FROM ubuntu:20.04
COPY bin/jesta-linux /usr/bin/jesta
RUN useradd -m guest
USER guest
ENTRYPOINT ["jesta"]
