FROM ubuntu:16.04
MAINTAINER goboten temp1414@gmail.com

# Include dist
ADD dist/ /root/dist/

# Install 
RUN apt-get update -y && \ 
    apt-get install -y python-dev python-pip python-virtualenv && \
    
    cd /opt && \
    virtualenv opencanary && \
    . opencanary/bin/activate && \
    
    apt-get install -y sudo && \
    pip install opencanary && \
    
    apt-get install -y libpcap-dev && \
    pip install scapy pcapy  && \
    
    apt-get install -y build-essential libssl-dev libffi-dev python-dev  && \
    pip install rdpy  && \

    apt-get install -y samba && \
    apt-get install -y rsyslog && \
    
# Supply configs
    mv /root/dist/smb.conf /etc/samba/ && \ 
    echo '$FileCreateMode 0644' >> /etc/rsyslog.conf && \
    echo "local7.*        /var/log/samba-audit.log" >> /etc/rsyslog.conf && \

# Clean up
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Start dionaea
CMD ["bash","/root/dist/start.sh"]

