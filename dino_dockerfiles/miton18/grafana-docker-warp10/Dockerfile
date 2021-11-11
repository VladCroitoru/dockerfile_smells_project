FROM grafana/grafana:4.0.2

COPY ./run.sh /run.sh   

RUN apt-get update && apt-get install -yq git

RUN git clone https://github.com/cityzendata/grafana-warp10.git

ENTRYPOINT ["/run.sh"]
