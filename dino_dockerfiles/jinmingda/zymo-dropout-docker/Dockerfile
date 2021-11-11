FROM hunterchung/zymo-docker
MAINTAINER Mingda Jin <mjin@zymoresearch.com>

RUN apt-get update && apt-get install -y \
    emboss \
    ncbi-blast+ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y

VOLUME /usr/share/dropout-report
ENTRYPOINT ["python", "/usr/share/TargetedSequencing_py/dropout-report/dropout_pipeline.py", "-u"]
