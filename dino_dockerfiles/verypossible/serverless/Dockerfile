FROM python:3.6.6

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y \
    groff \
    nodejs \
    postgresql \
    libpq-dev

RUN mkdir /root/.aws

RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
RUN pip install \
    awscli \
    pep8 \
    pipenv \
    pytest \
    pytest-cov \
    pytest-mock \
    pytest-watch \
    boto3

ARG SERVERLESS_VERSION
RUN npm install -g \
    serverless@${SERVERLESS_VERSION}

ARG YARN_VERSION
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version ${YARN_VERSION}

RUN echo "alias ll='ls -alFh --color=auto'" >> /root/.bashrc
RUN echo "alias l='ls -alFh --color=auto'" >> /root/.bashrc

# assuming that your serverless python libs live here
RUN echo "export PYTHONPATH=/code/serverless/lib" >> /root/.bashrc

RUN mkdir /code
WORKDIR /code
