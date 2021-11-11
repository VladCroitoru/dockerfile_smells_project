FROM golang:1.7

ENV GLIDE_VERSION v0.12.3

RUN curl -L -o glide.tar.gz https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-amd64.tar.gz \
        && tar -zxf glide.tar.gz \
	&& mv linux-amd64/glide /usr/local/bin/ \
	&& rm -rf linux-amd64 glide.tar.gz
