FROM boggart/alpine-apk-static-32bit
MAINTAINER Boggart "github.com/Boggart"
RUN ["/sbin/apk.static", "add", "--update", "alpine-base", "pwgen", "xvfb", "wine", "linux-pam", "wget"]
RUN wget --no-check-certificate "https://dl.dropboxusercontent.com/u/83869314/ShareX/2015/05/glibc-2.21-r4.apk" && \
    apk.static add --allow-untrusted glibc-2.21-r4.apk && \
    wget --no-check-certificate "https://dl.dropboxusercontent.com/u/83869314/ShareX/2015/05/glibc-bin-2.21-r4.apk" && \
    apk.static add --allow-untrusted glibc-bin-2.21-r4.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
    rm -rf /var/cache/apk/* && \
    wget --no-check-certificate https://bintray.com/artifact/download/tigervnc/stable/tigervnc-Linux-i686-1.4.3.tar.gz && tar zxf tigervnc-Linux-i686-1.4.3.tar.gz ./usr -C / && rm tigervnc-Linux-i686-1.4.3.tar.gz && \
    wget --no-check-certificate http://winetricks.org/winetricks && chmod +x winetricks && mv winetricks /usr/bin/winetricks && \
    adduser -D -s /bin/bash winer
USER winer
CMD ["/usr/local/bin/startwine.sh"]

