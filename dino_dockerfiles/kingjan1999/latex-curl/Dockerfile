FROM debian:buster-slim

RUN apt-get update && apt-get install -y \
		biber \
		latexmk \
		make \
		texlive-full \
	&& rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y \
		curl python python-pygments python3-pygments wget lmodern fonts-lmodern python-pip \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /root

RUN wget https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
RUN texlua /root/install-getnonfreefonts
RUN getnonfreefonts --sys --all

RUN wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-1-amd64.deb && \
    dpkg -i pandoc-*-amd64.deb && \
    wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.4.1a/linux-pandoc_2_7_3.tar.gz -q -O - | tar xz && \
    mv pandoc-crossref /usr/bin/ && \
    pip install pandocfilters && \
    apt-get clean -y && \
rm -rf pandoc-*-amd64.deb /var/lib/apt/lists/* /tmp/* /var/tmp/*
