FROM buildpack-deps:jessie
MAINTAINER Lionel Roche
RUN mkdir -p work

WORKDIR work 

#Install fastexport tool:
RUN mkdir -p /usr/local/src \
    && cd /usr/local/src \
    && git clone https://github.com/frej/fast-export.git
    
RUN cd /work
COPY hg2git.sh .
RUN chmod +x hg2git.sh

ENTRYPOINT ["/work/hg2git.sh"]

