FROM python:3
MAINTAINER Robert (robert@nigma.org)

WORKDIR /root/

# Installing vim and nano
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install nano vim nano -y

# Installing python modules
RUN DEBIAN_FRONTEND=noninteractive pip install requests tabulate

# Git clone the learning material
RUN DEBIAN_FRONTEND=noninteractive git clone https://github.com/CiscoDevNet/apicem-1.3-LL-sample-codes.git

# Adding ENV to config.py and lab1 if using your own apic-em.
COPY apicem_config.py /root/apicem-1.3-LL-sample-codes/basic-labs
COPY lab1-1-post-ticket.py /root/apicem-1.3-LL-sample-codes/basic-labs
COPY apicem_config.py /root/apicem-1.3-LL-sample-codes/path-trace-labs
COPY apicem_config.py /root/apicem-1.3-LL-sample-codes/policy-labs

# Adding a nice motd
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/motd' >> /etc/bash.bashrc
COPY motd /etc/

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Start bash in /root/ folder
CMD /bin/bash
