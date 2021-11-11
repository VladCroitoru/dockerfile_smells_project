FROM python:3
ENV ANSIBLE_PYTHON_INTERPRETER /usr/local/bin/python
ENV PYTHONUNBUFFERED 1

LABEL Name="Ansible runner"
LABEL Version="1.0"

RUN apt-get update && apt-get install --no-install-recommends -y \
  bash-completion \
  keychain \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN echo 'source /usr/share/bash-completion/bash_completion' >> /etc/bash.bashrc

RUN pip install --no-cache-dir -U pip setuptools && rm -rf /root/.cache/pip
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -rf /root/.cache/pip

RUN ansible-galaxy collection install community.general

WORKDIR /ansible-galaxy/roles
RUN ansible-galaxy install --roles-path . nickhammond.logrotate

WORKDIR /ansible-common
COPY playbooks playbooks
COPY roles roles

WORKDIR /app
