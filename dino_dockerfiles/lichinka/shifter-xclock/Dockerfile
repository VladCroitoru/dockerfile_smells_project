FROM python:2-slim

# make sure the system packages are installed
RUN set -x \
    && apt-get update \
    && apt-get install -y xauth          \
                          x11-apps       \
                       --no-install-recommends

CMD ["/usr/bin/xclock"]
