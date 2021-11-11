FROM docker:latest

LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"

RUN apk add --purge --no-cache --update \
      python3 py3-pip

RUN pip install --ignore-installed --isolated --no-input --compile --exists-action=a --disable-pip-version-check --no-cache-dir \
      awscli

CMD ["awscli"]
