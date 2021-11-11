FROM python:2.7-alpine
RUN apk add --no-cache git &&\
    cd /home &&\
    git clone https://github.com/ssut/py-googletrans.git &&\
    cd py-googletrans &&\
    python setup.py install &&\
    cd /home &&\
    rm -rf py-googletrans &&\
    apk del git
CMD cd /home/a && python gen-locales.py
