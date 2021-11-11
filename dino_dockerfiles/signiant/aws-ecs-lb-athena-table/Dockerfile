FROM python:2.7-alpine

RUN apk --no-cache add ca-certificates

RUN mkdir /src

COPY src/ /src/

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python","/src/aws-ecs-lb-athena-table.py"]
CMD ["-h"]
