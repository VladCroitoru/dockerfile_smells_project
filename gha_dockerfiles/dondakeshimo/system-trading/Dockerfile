From python:3.9.5 AS builder

WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv lock -r > requirements.txt


FROM python:3.9.5-slim

WORKDIR /src

COPY --from=builder /src/requirements.txt .

RUN pip install -r requirements.txt

COPY ./systrad ./systrad

CMD ["python", "-m", "systrad"]
