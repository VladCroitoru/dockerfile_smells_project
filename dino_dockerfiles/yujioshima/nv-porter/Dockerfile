FROM  nvidia/cuda:8.0-devel
ENV GOLANG_VERSION 1.9
RUN apt update && apt install -y --no-install-recommends\
		ca-certificates \
		git \
		g++ \
		gcc \
		libc6-dev \
		make \
		pkg-config \
		wget && \
	rm -rf /var/lib/apt/lists/*
RUN set -eux; \
	dpkgArch="$(dpkg --print-architecture)"; \
	case "${dpkgArch##*-}" in \
		amd64) goRelArch='linux-amd64'; goRelSha256='d70eadefce8e160638a9a6db97f7192d8463069ab33138893ad3bf31b0650a79' ;; \
		armhf) goRelArch='linux-armv6l'; goRelSha256='f52ca5933f7a8de2daf7a3172b0406353622c6a39e67dd08bbbeb84c6496f487' ;; \
		arm64) goRelArch='linux-arm64'; goRelSha256='0958dcf454f7f26d7acc1a4ddc34220d499df845bc2051c14ff8efdf1e3c29a6' ;; \
		i386) goRelArch='linux-386'; goRelSha256='7cccff99dacf59162cd67f5b11070d667691397fd421b0a9ad287da019debc4f' ;; \
		ppc64el) goRelArch='linux-ppc64le'; goRelSha256='10b66dae326b32a56d4c295747df564616ec46ed0079553e88e39d4f1b2ae985' ;; \
		s390x) goRelArch='linux-s390x'; goRelSha256='e06231e4918528e2eba1d3cff9bc4310b777971e5d8985f9772c6018694a3af8' ;; \
		*) goRelArch='src'; goRelSha256='a4ab229028ed167ba1986825751463605264e44868362ca8e7accc8be057e993'; \
			echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a corresponding Go binary release; will be building from source"; echo >&2 ;; \
	esac; \
	url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
	wget --no-check-certificate -O go.tgz "$url"; \
	echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
	tar -C /usr/local -xzf go.tgz; \
	rm go.tgz; \
	if [ "$goRelArch" = 'src' ]; then \
		echo >&2; \
		echo >&2 'error: UNIMPLEMENTED'; \
		echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP (and uninstall after build)'; \
		echo >&2; \
		exit 1; \
	fi; \
	export PATH="/usr/local/go/bin:$PATH"; \
	go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
RUN ln -s /usr/local/cuda/lib64/stubs/libnvidia-ml.so /usr/local/cuda/lib64/stubs/libnvidia-ml.so.1
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64/stubs
WORKDIR $GOPATH
RUN go get github.com/tankbusta/nvidia_exporter
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all
ENTRYPOINT ["nvidia_exporter"]
