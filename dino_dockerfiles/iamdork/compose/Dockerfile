FROM  alpine:3.3
RUN   apk -U add python py-pip git
ADD . /source
RUN pip install -e /source
ENTRYPOINT ["dork-compose"]
