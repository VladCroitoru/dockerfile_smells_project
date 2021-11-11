FROM golang

RUN go get github.com/yudai/gotty

RUN apt-get update && \
    apt-get install -y \
	tmux \
	libncurses5-dev \
	libncursesw5-dev \
	locales
    
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
    locale-gen en_US.UTF-8

COPY gotty.conf /root/.gotty

ENTRYPOINT ["gotty"]

CMD ["--help"]
