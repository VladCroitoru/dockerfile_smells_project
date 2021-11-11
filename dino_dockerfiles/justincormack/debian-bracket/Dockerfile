FROM justincormack/debian-pkgsrc

MAINTAINER Justin Cormack <justin@specialbusservice.com>

RUN cd /usr/pkgsrc/misc/py-anita && bmake
RUN cd /usr/pkgsrc/emulators/qemu && bmake
RUN cd /usr/pkgsrc/net/rsync && bmake
#RUN cd /usr/pkgsrc/graphics/py-matplotlib && bmake
RUN cd /usr/pkgsrc/textproc/libxslt && bmake
RUN cd /usr/pkgsrc/textproc/py-expat && bmake
RUN cd /usr/pkgsrc/lang/perl5 && bmake
RUN cd /usr/pkgsrc/www/lighttpd && bmake
RUN cd /usr/pkgsrc/devel/scmcvs && bmake
