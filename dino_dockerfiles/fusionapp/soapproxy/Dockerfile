FROM pypy:2
RUN pip install virtualenv
RUN virtualenv /appenv
RUN . /appenv/bin/activate \
 && pip install --no-cache-dir --upgrade pip setuptools wheel
COPY . /application
RUN . /appenv/bin/activate && cd /application && pip install --no-cache-dir .
ENTRYPOINT ["/appenv/bin/twistd", "--nodaemon", "--pidfile", "", "soap-proxy"]
CMD ["--help"]
