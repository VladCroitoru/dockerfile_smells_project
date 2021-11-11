FROM amazonlinux AS base

RUN yum install -y python36-pip shadow-utils

RUN pip-3.6 install --no-cache-dir pygithub sh

FROM base as test_base

RUN yum install -y gcc python36-devel && \
    pip-3.6 install --no-cache-dir pytest mypy

FROM test_base as tests

COPY test_sync_github_users.py /usr/bin/
COPY sync_github_users.py /usr/bin/

RUN mypy --ignore-missing-imports /usr/bin/sync_github_users.py
RUN pytest -v /usr/bin/test_sync_github_users.py

FROM base

COPY sync_github_users.py /usr/bin/

CMD ["python3.6", "/usr/bin/sync_github_users.py"]
