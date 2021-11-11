FROM ubuntu:latest
RUN mkdir test_dir
WORKDIR /test_dir
RUN apt-get update && apt-get install -y libnet1-dev protobuf-c-compiler libprotobuf-c0-dev protobuf-compiler libprotobuf-dev:amd64 gcc build-essential bsdmainutils python git-core asciidoc make htop git curl supervisor cgroup-lite libapparmor-dev libseccomp-dev libprotobuf-dev libprotobuf-c0-dev protobuf-c-compiler protobuf-compiler python-protobuf libnl-3-dev libcap-dev libaio-dev apparmor
RUN git clone https://github.com/checkpoint-restore/criu.git
RUN cd criu && make clean && make && make install

ADD . /experiment

ENTRYPOINT ["configs/avida"]
