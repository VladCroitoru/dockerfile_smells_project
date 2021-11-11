FROM python:2.7-alpine

RUN apk add --no-cache --virtual=build_dependencies musl-dev gcc python-dev make cmake g++ gfortran && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip install numpy && \
    pip install pandas==0.22.0 && \
    apk del build_dependencies && \
    apk add --no-cache libstdc++ && \
    rm -rf /var/cache/apk/*

RUN python -c "import pandas; df = pandas.DataFrame()"
CMD python -c "import time; time.sleep(999999)"
