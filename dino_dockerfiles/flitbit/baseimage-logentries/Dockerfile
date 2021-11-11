# Use phusion/baseimage which is ubuntu "fixed" for docker,
#   described at https://github.com/phusion/baseimage-docker.
FROM phusion/baseimage:0.9.15

ADD logentries-conf-template /var/logentries/logentries-conf-template
ADD logentries-message-template /var/logentries/logentries-message-template

ADD 00_fix_logentries_conf.sh /etc/my_init.d/00_fix_logentries_conf.sh
RUN chmod +x /etc/my_init.d/00_fix_logentries_conf.sh
