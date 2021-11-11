FROM python:3.6-alpine

RUN pip install --no-cache-dir \
  mkdocs \
  mkdocs-material \
  pygments \
  pymdown-extensions

ENTRYPOINT ["mkdocs"]
CMD ["--help"]
