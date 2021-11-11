FROM perl

RUN apt-get update

RUN apt-get install -y \ 
    netcat-openbsd 

ADD http://sourceforge.net/projects/simple-evcorr/files/sec/2.7.10/sec-2.7.10.tar.gz /sec

EXPOSE 11111

# ENTRYPOINT ["/usr/local/bin/uwsgi"]
# CMD ["--yaml", "uwsgi.yaml"]
