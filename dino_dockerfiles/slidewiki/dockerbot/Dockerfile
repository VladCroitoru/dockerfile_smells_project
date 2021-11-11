FROM python:2-onbuild
ENV PYTHONUNBUFFERED 1

# install gettext (has envsubst)
RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get autoremove -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

ADD . /app/

# ensure requirements are met
RUN pip install -r /app/requirements.txt

# install our application
RUN pip install .

CMD ["sh", "/app/entrypoint.sh"]
