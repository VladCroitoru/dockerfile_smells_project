FROM docker-registry.prozorro.gov.ua/docker/images/python:3.8-alpine3.14
WORKDIR /app
RUN apk --no-cache add gcc build-base git openssl-dev libffi-dev
ADD requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./src/prozorro_auction /app/prozorro_auction
ENV API_OPT_FIELDS="status,procurementMethodType"
ENTRYPOINT ["python", "-m"]
CMD ["prozorro_auction.api.main"]