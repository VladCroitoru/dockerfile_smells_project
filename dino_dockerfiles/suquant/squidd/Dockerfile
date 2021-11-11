FROM alpine:3.6
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk add --no-cache squid


#/ # squid -h
#Usage: squid [-cdhvzCFNRVYX] [-n name] [-s | -l facility] [-f config-file] [-[au] port] [-k signal]
#       -a port   Specify HTTP port number (default: 3128).
#       -d level  Write debugging to stderr also.
#       -f file   Use given config-file instead of
#                 /etc/squid/squid.conf
#       -h        Print help message.
#       -k reconfigure|rotate|shutdown|restart|interrupt|kill|debug|check|parse
#                 Parse configuration file, then send signal to
#                 running copy (except -k parse) and exit.
#       -n name   Specify service name to use for service operations
#                 default is: squid.
#       -s | -l facility
#                 Enable logging to syslog.
#       -u port   Specify ICP port number (default: 3130), disable with 0.
#       -v        Print version.
#       -z        Create missing swap directories and then exit.
#       -C        Do not catch fatal signals.
#       -D        OBSOLETE. Scheduled for removal.
#       -F        Don't serve any requests until store is rebuilt.
#       -N        No daemon mode.
#       -R        Do not set REUSEADDR on port.
#       -S        Double-check swap during rebuild.
#       -X        Force full debugging.
#       -Y        Only return UDP_HIT or UDP_MISS_NOFETCH during fast reload.

EXPOSE 3128/TCP 3130/UDP

ENTRYPOINT ["/usr/sbin/squid", "-N", "-a", "3128", "-u", "3130"]
CMD ""
