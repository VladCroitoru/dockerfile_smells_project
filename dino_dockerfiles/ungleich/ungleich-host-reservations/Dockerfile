FROM ungleich/cdist
MAINTAINER Carlos Ortigoza "carlos.ortigoza@ungleich.ch"

RUN apt-get update && apt-get install -y libpq-dev python3-pip
RUN pip3 install --upgrade pip && pip3 install psycopg2
COPY print-mac-ip-from-kea.py /

ENTRYPOINT ["python3", "/print-mac-ip-from-kea.py"]
