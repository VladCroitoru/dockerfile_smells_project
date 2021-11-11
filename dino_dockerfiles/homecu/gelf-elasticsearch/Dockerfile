FROM jmayfield/shellish:v4.1
RUN pip install aiohttp
COPY . src
WORKDIR src
ENTRYPOINT ["python", "./gelf_elasticsearch.py"]
