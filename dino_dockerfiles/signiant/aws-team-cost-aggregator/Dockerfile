FROM python:2.7-alpine

RUN apk --no-cache add ca-certificates

RUN mkdir /src

COPY team-cost-aggregator/ /src/

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python","/src/team-cost-aggregator.py"]
CMD ["-h"]
