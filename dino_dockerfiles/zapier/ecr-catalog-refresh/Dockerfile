from python:3.6-onbuild

ADD refresh-catalog.py /bin/ecr-refresh-catalog

ENTRYPOINT /bin/ecr-refresh-catalog --catalog-file /opt/catalog/repos.json

