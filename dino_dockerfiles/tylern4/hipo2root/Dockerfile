FROM rootproject/root-ubuntu16
USER root

COPY . /usr/local/hipo2root
WORKDIR /usr/local/hipo2root

RUN ./make_hipo2root.py --json bankdefs/rec_particle.json \
    && make \
    && cp hipo2root /usr/local/bin/

WORKDIR /tmp
ENTRYPOINT ["/usr/local/bin/hipo2root"]
