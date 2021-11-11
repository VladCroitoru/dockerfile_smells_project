FROM python:3.9

# Environment.
WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
RUN python -m venv env && \
    ./env/bin/python -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    ./env/bin/python -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# App.
COPY ./config ./config
COPY ./innonymous ./innonymous
COPY ./entrypoint.sh ./entrypoint.sh

# Run.
EXPOSE 8000
ENTRYPOINT ["sh", "./entrypoint.sh"]
