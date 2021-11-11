FROM python:alpine

ADD setup.* README.rst /build/
ADD emcli /build/emcli

RUN \
apk add --no-cache jq ;\
cd /build ;\
python setup.py install ;\
rm -rf /build

ENTRYPOINT []
CMD ["envmgr"]
