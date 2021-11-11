FROM python:2.7.13

ADD bin /app/bin
ADD server /app/server
ADD requirements.dev.txt /app
ADD requirements.txt /app
ADD runtime.txt /app
ADD sample_event.json /app
ADD setup.py /app

ENV ERP_SERVICE http://lw-erp:8080
ENV OPENWHISK_PACKAGE=lwr

ENV PORT 8080
EXPOSE 8080

RUN cd /app && pip install -r requirements.dev.txt

WORKDIR "/app"
CMD [ "gunicorn", "-w", "4", "bin.start_web:application" ]
