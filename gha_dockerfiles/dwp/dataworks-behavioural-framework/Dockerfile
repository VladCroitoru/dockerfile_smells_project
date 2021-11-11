FROM dwpdigital/python-boto-behave

RUN apk add libffi-dev openssl-dev python3-dev rust

RUN mkdir /src

COPY assume_role.sh /
COPY requirements.txt /
COPY src/ /src/

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PATH=$PATH:/root/.local/bin
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --user

WORKDIR /src
RUN chmod -R +x runners/

WORKDIR /src/runners
ENV E2E_FEATURE_TAG_FILTER=
ENV RUNNER_SCRIPT=./run-ci.sh

ENTRYPOINT ["sh"]
CMD ["./run-ci.sh"]
