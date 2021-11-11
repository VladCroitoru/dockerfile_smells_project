FROM python:3
ENTRYPOINT ["/usr/local/bin/cwlogs_env_runner"]
CMD []

RUN pip install --use-wheel --upgrade pip wheel

# Install dependencies first, so this layer is cached
COPY requirements.txt /usr/local/src/requirements.txt
RUN mkdir -p /etc/cloudwatch /run/cloudwatch /var/log/cloudwatch
RUN pip install --use-wheel -r /usr/local/src/requirements.txt && \
    rm -rf /root/.pip/cache && \
    aws configure set plugins.cwlogs cwlogs

COPY MANIFEST.in requirements* setup.py /usr/local/src/cloudwatch_logs_environment/
COPY cloudwatch_logs_environment/ /usr/local/src/cloudwatch_logs_environment/cloudwatch_logs_environment/
RUN cd /usr/local/src/cloudwatch_logs_environment; python setup.py bdist_wheel
RUN pip install /usr/local/src/cloudwatch_logs_environment/dist/*.whl
