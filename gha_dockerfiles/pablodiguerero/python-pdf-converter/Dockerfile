FROM duruo850/pyppeteer-python3.8.0-ubuntu18.04
RUN apt-get update && apt-get -y install python3 python3-pip curl

COPY ./src /app
RUN pip3 install -r /app/requirements.txt
RUN pip3 install uvicorn gunicorn

WORKDIR /app
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn_conf.py", "main:app"]
EXPOSE 80
