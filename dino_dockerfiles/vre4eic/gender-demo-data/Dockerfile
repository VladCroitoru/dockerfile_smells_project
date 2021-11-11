FROM debian:stretch-slim
RUN useradd vre4eic_data
RUN mkdir /data
RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/vre4eic/gender-toe-data.git /data/toe; cd data/toe; git checkout V1.0.1
COPY passwd /data
ADD rdf.tgz /data
ADD gitty.tgz /data

RUN chown -R vre4eic_data.vre4eic_data /data && \
    chown -R root /data/config-enabled && \
    chmod -R ug+rwX /data/data
