FROM openjdk:8
MAINTAINER Ivan Pereira <ivan@zivan.org>

RUN mkdir -p /opt/local
WORKDIR /opt/local

RUN curl -L https://drive.google.com/uc\?id\=0B7YOzDQMt_TmS2lNMlpndnJndDA -o SMPPSim.tar.gz && \
    tar -xzf SMPPSim.tar.gz && \
    rm /opt/local/SMPPSim.tar.gz


EXPOSE 88 2775 2776

WORKDIR /opt/local/SMPPSim
RUN chmod +x startsmppsim.sh

VOLUME ["/opt/local/SMPPSim/conf"]

CMD /opt/local/SMPPSim/startsmppsim.sh
