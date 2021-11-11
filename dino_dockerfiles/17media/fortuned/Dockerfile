FROM    allanlei/python:3.5.2-onbuild

ENV     GUNICORN_WORKER_CLASS=aiohttp.worker.GunicornUVLoopWebWorker

RUN     apk --no-cache add -X http://dl-cdn.alpinelinux.org/alpine/edge/community \
          fortune
COPY    config/gunicorn.conf.py .
COPY    data/ /usr/share/fortune/

EXPOSE  8000/tcp
CMD     ["gunicorn", "app:make_app()", "-c", "config/gunicorn.conf.py", "-b", "0.0.0.0:8000"]
