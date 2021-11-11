FROM chuckus/python-2.7-alpine-pandas

RUN apk add --no-cache --virtual=build_dependencies musl-dev gcc python-dev make autoconf postgresql-dev && \
    apk add --no-cache postgresql && \
    pip install psycopg2==2.6.1 && \
    pip install Django==1.9.2 && \
    pip install djangorestframework==3.3.2 && \
    pip install psycopg2==2.6.1 && \
    pip install pycrypto==2.6.1 && \
    apk del build_dependencies && \
    apk add --no-cache libstdc++

# RUN python -c "from Crypto.Cipher import AES"
# RUN python -c "import psycopg2"
