FROM        progrium/busybox
MAINTAINER  Steve Mayne <steve.mayne@gmail.com>

RUN opkg-install uhttpd
RUN printf '#!/bin/sh\nset -e\n\nchmod 755 /www\nexec /usr/sbin/uhttpd $*\n' > /usr/sbin/run_uhttpd && chmod 755 /usr/sbin/run_uhttpd

VOLUME ["/www"]

RUN sed -i 's/#\s\+option no_dirlists\s\+0/option no_dirlists      1/g' /etc/config/uhttpd

EXPOSE 80

CMD ["/usr/sbin/run_uhttpd", "-f", "-p", "80", "-h", "/www"]
