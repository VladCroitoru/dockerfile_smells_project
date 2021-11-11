FROM perl:5.24

COPY cpanfile .
COPY hp-msa.pl .

RUN set -e && \
    cpanm --installdeps . && \
    rm -rf /root/.cpanm

ENTRYPOINT ["perl", "hp-msa.pl"]
