FROM frolvlad/alpine-glibc
MAINTAINER He Bai <bai.he@outlook.com>

# Install python related packages
RUN apk add --no-cache python3-dev && \
    apk add --no-cache libstdc++ && \
    apk add --no-cache --virtual .build-deps g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    apk add --no-cache postgresql-dev && \
    apk add --no-cache mariadb-dev && \
    apk add --no-cache freetype-dev && \
    pip3 --no-cache-dir install --upgrade pip && \
    pip3 --no-cache-dir install requests && \
    pip3 --no-cache-dir install XlsxWriter && \
    pip3 --no-cache-dir install SQLAlchemy && \
    pip3 --no-cache-dir install psycopg2 && \
    pip3 --no-cache-dir install mysqlclient && \
    pip3 --no-cache-dir install numpy && \
    pip3 --no-cache-dir install pandas && \
    pip3 --no-cache-dir install matplotlib && \
    pip3 --no-cache-dir install jupyter && \
    apk del .build-deps && \
    rm -rf /tmp/glibc*apk /var/cache/apk/* /root/.cache/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Install the jupyter notebook
RUN adduser -D jupy
USER jupy

RUN mkdir -p /home/jupy/notebooks
VOLUME /home/jupy/notebooks

EXPOSE 9999
ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--port=9999", "--notebook-dir=/notebooks"]

