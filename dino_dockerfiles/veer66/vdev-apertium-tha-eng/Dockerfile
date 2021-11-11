FROM debian:10

RUN mkdir /wrk && \
    apt-get update && \
    apt-get upgrade -y && apt-get install -y subversion build-essential pkg-config gawk libxml2 libxml2-dev libxml2-utils xsltproc flex automake libtool libpcre3-dev zlib1g-dev libboost-dev libgoogle-perftools-dev libicu-dev cmake python locales && \
    echo "th_TH.UTF-8 UTF-8" >  /etc/locale.gen && locale-gen && \    
    svn checkout https://svn.code.sf.net/p/apertium/svn/trunk/lttoolbox && \
    svn checkout https://svn.code.sf.net/p/apertium/svn/trunk/apertium && \
    svn checkout https://svn.code.sf.net/p/apertium/svn/trunk/apertium-lex-tools && \
    svn co http://beta.visl.sdu.dk/svn/visl/tools/vislcg3/trunk vislcg3 && \
    svn co  https://svn.code.sf.net/p/apertium/svn/incubator/apertium-tha && \
    svn co  https://svn.code.sf.net/p/apertium/svn/incubator/apertium-tha-eng

ENV LD_RUN_PATH=/usr/local/lib:/usr/local/lib/x86_64-linux-gnu/
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib/x86_64-linux-gnu/
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig 
ENV LC_ALL=th_TH.UTF-8
ENV LANG=th_TH.UTF-8

RUN cd /lttoolbox && ./autogen.sh && make && make install && \
    cd /apertium && ./autogen.sh && make && make install && \
    cd /apertium-lex-tools && ./autogen.sh && ./configure && make && make install && \
    cd /vislcg3 && ./cmake.sh && make -j3 && make install && \
    cd /apertium-tha && ./autogen.sh && make && \
    cd /apertium-tha-eng && ./autogen.sh --with-lang1=/apertium-tha && make

RUN useradd -r -m -d /home/apertium -s /bin/bash -u 1000 apertium
RUN mkdir /home/apertium/.ssh && chown apertium:apertium /home/apertium/.ssh && chmod 700 /home/apertium/.ssh

RUN apt-get install -y openssh-server
RUN mkdir /run/sshd

CMD ["/usr/sbin/sshd", "-D"]