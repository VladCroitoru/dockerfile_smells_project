FROM gcr.io/nectar-bazaar/py-ci:latest
WORKDIR /app
ADD . /app
RUN pipenv lock -r > requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/py-ci/start.sh"]