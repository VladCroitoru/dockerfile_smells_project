# FROM gcr.io/cloud-datalab/datalab:latest
FROM gcr.io/cloud-datalab/datalab:commit-latest-master-build

WORKDIR /custom

COPY ./custom/install.sh ./
COPY ./custom/requirements.txt ./
RUN ./install.sh

COPY ./custom/install-snorkel.sh ./
RUN ./install-snorkel.sh

COPY ./custom/install-janome.sh ./
RUN ./install-janome.sh

COPY ./custom/entrypoint.sh ./
