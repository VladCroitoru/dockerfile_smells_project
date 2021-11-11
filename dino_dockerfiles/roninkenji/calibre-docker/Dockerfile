FROM roninkenji/slackware-base:latest
MAINTAINER roninkenji

RUN slackpkg -batch=on -default_answer=yes install glibc-2.17 cxxlibs python-2.7
RUN mkdir -p /opt/Library
RUN wget -nv -O/tmp/linux-installer.py --no-check-certificate https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py
RUN python -c "import sys; main=lambda x,y:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main('/opt', True)" < /tmp/linux-installer.py

EXPOSE 8080
# ENTRYPOINT ["/etc/rc.d/rc.mysqld", "start"]
ENTRYPOINT ["/opt/calibre/calibre-server"]
CMD ["--with-library", "/opt/Library", "--url-prefix", "/Library"]

