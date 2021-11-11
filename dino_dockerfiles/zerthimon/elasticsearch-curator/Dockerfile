FROM python:2.7.12

RUN useradd -d /home/curator -m curator \
    && pip install elasticsearch-curator

COPY curator.yml /home/curator/.curator/curator.yml

RUN chown -R curator:curator /home/curator/.curator

USER curator

WORKDIR /home/curator

ENTRYPOINT [ "/usr/local/bin/curator" ]
