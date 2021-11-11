FROM ubuntu:15.10

RUN apt-get -y update && apt-get install -y \
	python3 \
	python3-pip \
	python3-pytest \
	git

RUN pip3 install mock beer

RUN mkdir -p /src/ && cd /src/ && \
	git clone https://github.com/monprin/Beer.git 

ENTRYPOINT ["/bin/bash"]
