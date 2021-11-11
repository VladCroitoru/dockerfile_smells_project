FROM python:3.7-slim

RUN adduser matrixexplorer --disabled-password

WORKDIR /home/matrixexplorer

COPY --chown=matrixexplorer:matrixexplorer . /home/matrixexplorer/

RUN pip install --no-cache-dir -r requirements.txt && \
    find /usr/local/lib/python3.7 -name '*.c' -delete && \
    find /usr/local/lib/python3.7 -name '*.pxd' -delete && \
    find /usr/local/lib/python3.7 -name '*.pyd' -delete && \
    find /usr/local/lib/python3.7 -name '__pycache__' | xargs rm -r

USER matrixexplorer

EXPOSE 8080

CMD gunicorn -b 0.0.0.0:8080 --access-logfile - --error-logfile - --worker-class gevent --workers 3 index:server
