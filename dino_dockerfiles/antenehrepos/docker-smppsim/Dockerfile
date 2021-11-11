FROM java:8

MAINTAINER Anteneh Aklilu "reachanteneh@gmail.com"

RUN curl -L -o /usr/local/SMPPSim.tar.gz 'https://www.dropbox.com/s/tma8b8psjtwge3r/SMPPSim.tar.gz?dl=0' && \
    tar xzf /usr/local/SMPPSim.tar.gz && \
    rm -f /usr/local/SMPPSim.tar.gz

COPY conf/smppsim.props SMPPSim/conf/

EXPOSE 88 2775 2776

WORKDIR SMPPSim

RUN chmod +x startsmppsim.sh
CMD ./startsmppsim.sh