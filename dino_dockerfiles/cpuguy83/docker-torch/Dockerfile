FROM golang:1.6

RUN go get github.com/uber/go-torch github.com/crosbymichael/docker-stress
RUN git clone --depth=1 https://github.com/brendangregg/FlameGraph.git /opt/flamegraph
RUN mkdir -p /opt/docker-torch
ADD torch.go /opt/docker-torch/
RUN cd /opt/docker-torch && go build
ENV PATH $PATH:/opt/flamegraph:/opt/docker-torch
WORKDIR /data
ENTRYPOINT ["docker-torch"]
