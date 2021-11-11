FROM ubuntu:16.04

RUN apt-get update && apt-get install -y curl python-pip
RUN pip install --pre pygments pygments-markdown-lexer

ARG HUGO_VERSION=0.25.1

RUN curl -Ls https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.deb -o /tmp/hugo.deb && \
    dpkg -i /tmp/hugo.deb && \
    rm /tmp/hugo.deb

WORKDIR /app

EXPOSE 1313

CMD ["hugo", "server", "-w", "--bind", "0.0.0.0"]
