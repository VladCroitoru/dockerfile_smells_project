FROM   ubuntu:latest
MAINTAINER Ivan Pedrazas <ipedrazas@gmail.com>

RUN apt-get update && apt-get install -y \
    python-software-properties \
    software-properties-common \
    dbus-x11 \
    --no-install-recommends

RUN add-apt-repository -y ppa:rael-gc/scudcloud && \
    apt-get update && \
    apt-get install scudcloud -y

ENV QT_X11_NO_MITSHM=1

CMD ["/usr/bin/scudcloud"]
