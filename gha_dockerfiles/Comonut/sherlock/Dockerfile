FROM python:3.6
COPY ./sherlock/* ./
COPY ./sherlock/resources ./resources
RUN pip3 install -r ./requirements.txt
ENTRYPOINT [ "uvicorn","gql:app","--host", "0.0.0.0"] 