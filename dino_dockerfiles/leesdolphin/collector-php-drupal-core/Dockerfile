FROM python:3.6

# add a non-root user and give them ownership
RUN useradd -u 9000 app && \
    # user home directory
    mkdir /home/app && \
    chown -R app:app /home/app && \
    # repo
    mkdir /repo && \
    chown -R app:app /repo && \
    # collector code
    mkdir /usr/src/collector && \
    chown -R app:app /usr/src/collector

COPY ["requirements.txt", "/tmp/"]
RUN pip install -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt

# run everything from here on as non-root
USER app

COPY ["entrypoint.py", "/usr/src/collector/"]

WORKDIR /repo

ENTRYPOINT ["python", "/usr/src/collector/entrypoint.py"]

LABEL io.dependencies.allow-write="False"
