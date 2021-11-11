FROM        python:slim
MAINTAINER  Inonit AS <support@inonit.no>

RUN         pip install redis
RUN         pip install https://github.com/mher/flower/zipball/master

EXPOSE 5555
ENTRYPOINT ["flower", "--url_prefix=flower", "--port=5555"]
