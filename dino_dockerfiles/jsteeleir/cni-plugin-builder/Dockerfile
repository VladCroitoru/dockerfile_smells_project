FROM golang

COPY build-cni.sh .
RUN chmod u+x build-cni.sh

RUN mkdir -p /opt/cni/bin
VOLUME /opt/cni/bin

CMD ["./build-cni.sh"]
