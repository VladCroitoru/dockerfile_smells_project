FROM poum/distzilla

RUN cpanm install \
        Moose \
        DBIx::Class \
        && rm -rf /root/.cpanm /tmp/*

CMD [ "dzil" ]

