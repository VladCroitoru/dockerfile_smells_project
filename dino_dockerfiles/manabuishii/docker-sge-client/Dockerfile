FROM ubuntu:14.04.4
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq ; apt-get upgrade ; \
    apt-get install -y gridengine-client ; \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# dummy user account
RUN useradd -m dummy
RUN echo "dummy:dummy" | chpasswd
#
ADD setup.sh /usr/local/bin/setup.sh
RUN chmod +x /usr/local/bin/setup.sh

#
ENTRYPOINT ["/usr/local/bin/setup.sh"]

