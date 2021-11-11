FROM python:2.7-alpine

LABEL maintainer "Sergey Ugdyzhekov, sergey@ugdyzhekov.org"

RUN pip install requests
COPY app /usr/local/lib/scalet_backup

CMD ["/usr/local/lib/scalet_backup/backup_scalets.py"]