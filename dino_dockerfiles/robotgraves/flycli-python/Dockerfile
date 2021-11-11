FROM robotgraves/virtualpython

ENV PATH /usr/local/bin:$PATH

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    	ca-certificates build-essential wget curl zip

RUN wget -O /tmp/fly https://github.com/concourse/concourse/releases/download/v3.2.1/fly_linux_amd64 && \
    mv /tmp/fly /usr/local/bin/fly && \
chmod +x /usr/local/bin/fly