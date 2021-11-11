FROM asciidoctor/docker-asciidoctor

MAINTAINER Raymond Yee  <raymond.yee@gmail.com>

RUN yum makecache fast
RUN yum install -y automake autoconf libtool libxslt git zip

# download

RUN mkdir /htmlbook
RUN git clone https://github.com/rdhyee/asciidoctor-htmlbook.git /htmlbook/asciidoctor-htmlbook
RUN git clone https://github.com/rdhyee/HTMLBook /htmlbook/HTMLBook

# checkout specific versions of the repos (for the moment)

RUN cd /htmlbook/asciidoctor-htmlbook && \
    git checkout c28bb54943735fa474e94ae6e76b38b3ea72cea5
    
RUN cd /htmlbook/HTMLBook && \
    git checkout 547a4d356fb78189a7590a9bb7352ac0c723e525

ENV PATH /:$PATH

ADD a2epub.sh /a2epub.sh
