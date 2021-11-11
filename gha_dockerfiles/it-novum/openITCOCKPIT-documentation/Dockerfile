FROM alpine:latest

RUN apk update && apk add python3 py3-pip git
RUN pip install mkdocs && \
pip install mkdocs-material && \
pip install markdown-include && \
pip install git+https://github.com/it-novum/mkdocs-featherlight.git


EXPOSE 8000

CMD ["/usr/bin/mkdocs", "serve"]

