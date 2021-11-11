FROM python:3

RUN mkdir -p /src/project

COPY project/ /src/project

WORKDIR /src

RUN pip install -r project/config/requirements.txt

ENTRYPOINT ["python3","-m","project.main"]
CMD ["-h"]
