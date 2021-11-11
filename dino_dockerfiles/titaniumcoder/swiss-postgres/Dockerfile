FROM postgres:13.3
RUN localedef -i de_CH -c -f UTF-8 -A /usr/share/locale/locale.alias de_CH.UTF-8
ENV LANG de_CH.utf8
ENV POSTGRES_INITDB_ARGS "-E UTF-8 --locale de_CH.UTF-8"
