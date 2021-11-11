FROM ubuntu:14.04
RUN groupadd -g 1001 firefox
RUN useradd -d /home/firefox -u 1001 -g 1001 -m -s /bin/bash firefox
USER firefox
ENV HOME /home/firefox
ADD aspera-connect-3.6.2.112845-linux-64.sh /tmp/aspera-connect-3.6.2.112845-linux-64.sh
#This is a beta version of the aspera connect plugin which fix the sh: 1: lsof: not found issue.
#And this version works with firefox version 40.0
#ADD http://download.asperasoft.com/download/sw-private/connect/3.6.2/E5D528D3-1ED0-451F-BE7F-A88FFB6EFB5E/aspera-connect-3.6.2.112845-linux-64.sh /tmp/aspera-connect-3.6.2.112845-linux-64.sh
RUN sh /tmp/aspera-connect-3.6.2.112845-linux-64.sh


