FROM node:4
MAINTAINER Rogier Slag <Rogier@magnet.me>

VOLUME ["/opt/nagios"]
RUN npm install -g nagios-status-parser

CMD ["nagios-status-parser", "/opt/nagios/status.dat"]

