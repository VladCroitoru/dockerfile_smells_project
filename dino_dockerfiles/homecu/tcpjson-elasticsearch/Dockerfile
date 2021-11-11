FROM jmayfield/shellish
RUN pip install aiohttp
COPY . src
WORKDIR src
ENTRYPOINT ["python", "./tcpjson_elasticsearch.py"]
