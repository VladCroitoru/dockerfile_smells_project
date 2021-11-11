FROM fedora

RUN dnf -y --setopt=tsflags=nodocs install tar bzip2 fontconfig libstdc++ && dnf -y clean all

RUN curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | \
    tar -xjf - -C /opt

ADD run.sh /opt/phantomjs-2.1.1-linux-x86_64/bin/

RUN chmod -R 777 /opt/phantomjs-2.1.1-linux-x86_64/

EXPOSE 4444

WORKDIR /opt/phantomjs-2.1.1-linux-x86_64/bin/

ENTRYPOINT [ "./run.sh" ]

