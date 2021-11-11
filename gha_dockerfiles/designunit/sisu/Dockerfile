FROM python:2.7.18-alpine3.11
WORKDIR ./app
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "tests"]

