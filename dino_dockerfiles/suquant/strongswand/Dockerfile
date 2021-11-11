FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk add --no-cache strongswan iptables

ENTRYPOINT ["ipsec"]
CMD ["start", "--nofork"]


EXPOSE 1812/udp 1813/udp 3799/udp

# Usage: starter [--nofork] [--auto-update <sec>]
#                [--debug|--debug-more|--debug-all|--nolog]
#                [--attach-gdb] [--daemon <name>]
#                [--conf <path to ipsec.conf>]