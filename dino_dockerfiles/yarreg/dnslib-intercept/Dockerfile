FROM python:2.7.13-alpine3.6

RUN pip --no-cache-dir install dnslib==0.9.7    

ENTRYPOINT ["python", "/usr/local/lib/python2.7/site-packages/dnslib/intercept.py"]