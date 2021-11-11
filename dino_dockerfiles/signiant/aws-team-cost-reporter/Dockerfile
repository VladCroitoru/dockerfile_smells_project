FROM python:3.8

RUN mkdir /src

COPY team-cost-reporter/ /src/

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python","/src/team-cost-reporter.py"]
CMD ["-h"]
