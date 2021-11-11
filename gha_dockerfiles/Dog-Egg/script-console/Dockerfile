FROM node:12 as builder

WORKDIR /code

COPY web .

RUN yarn && npm run build

FROM python:3.6

WORKDIR /code

ENV SC_SCRIPTS_DIR="/scripts"
ENV SC_DATA_DIR="/data"

COPY . .
COPY --from=builder /code/build ./web/build

RUN pip install -r requirements.txt

VOLUME /scripts

EXPOSE 8310

CMD ["python", "webservice.py"]