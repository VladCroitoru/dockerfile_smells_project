FROM python:2.7-alpine

RUN mkdir /src

COPY jenkins-artifact-view-cleaner.py /src/

WORKDIR /src

ENTRYPOINT ["python","/src/jenkins-artifact-view-cleaner.py"]
CMD ["-h"]
