FROM centos:7

RUN yum install -y gcc glibc-static make \
    && yum -y install tmux which \
    && yum install -y git \
    && cd /usr/src/ \
    && git clone git://github.com/c9/core.git c9sdk \
    && cd c9sdk \
    && scripts/install-sdk.sh \
    && yum install -y python-setuptools python-devel gcc-c++ \
    && easy_install pip \
    && pip install -U virtualenv \
    && virtualenv --python=python2 /root/.c9/python2 \
    && source /root/.c9/python2/bin/activate \
    && mkdir /tmp/codeintel \
    && pip download -d /tmp/codeintel codeintel==0.9.3 \
    && cd /tmp/codeintel \
    && tar xf CodeIntel-0.9.3.tar.gz \
    && mv CodeIntel-0.9.3/SilverCity CodeIntel-0.9.3/silvercity \
    && tar czf CodeIntel-0.9.3.tar.gz CodeIntel-0.9.3 \
    && pip install -U --no-index --find-links=/tmp/codeintel codeintel \
    && yum remove -y gcc cpp glibc-devel glibc-headers kernel-headers libmpc mpfr glibc-static make \
    && rm -rf /tmp/codeintel \
    && yum remove -y git fipscheck fipscheck-lib groff-base less libedit libgnome-keyring openssh \
    openssh-clients perl perl-Carp perl-Encode perl-Error perl-Exporter perl-File-Path perl-File-Temp \
    perl-Filter perl-Getopt-Long perl-Git perl-HTTP-Tiny perl-PathTools perl-Pod-Escapes perl-Pod-Perldoc \
    perl-Pod-Simple perl-Pod-Usage perl-Scalar-List-Utils perl-Socket perl-Storable perl-TermReadKey \
    perl-Text-ParseWords perl-Time-HiRes perl-Time-Local perl-constant perl-libs perl-macros perl-parent \
    perl-podlators perl-threads perl-threads-shared rsync
    
    
ENV WORKSPACE_DIR /root/
ENV C9_IP 0.0.0.0
ENV C9_PORT 8080
ENV USERNAME ""
ENV PASSWORD ""

WORKDIR /usr/src/c9sdk
EXPOSE 8080

CMD /root/.c9/node/bin/node server.js -l $C9_IP -p $C9_PORT -w $WORKSPACE_DIR -a $USERNAME:$PASSWORD --packed
