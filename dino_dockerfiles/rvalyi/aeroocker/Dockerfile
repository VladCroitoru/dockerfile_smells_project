FROM ubuntu-debootstrap:14.04
MAINTAINER rvalyi "rvalyi@akretion.com"

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git python3-uno libreoffice-writer libreoffice-calc python3-pip xvfb supervisor openjdk-7-jre && \
    apt-get clean

RUN pip3 install jsonrpc2
RUN pip3 install daemonize

RUN git clone https://github.com/aeroo/aeroo_docs.git /opt/aeroo_docs

EXPOSE 8989

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf
