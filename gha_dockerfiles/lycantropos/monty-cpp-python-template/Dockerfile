ARG IMAGE_NAME
ARG IMAGE_VERSION

FROM ${IMAGE_NAME}:${IMAGE_VERSION}

RUN pip install --upgrade pip setuptools

WORKDIR /opt/{{project}}

COPY requirements-setup.txt .
COPY requirements-tests.txt .
RUN pip install -r requirements-tests.txt

COPY README.md .
COPY pytest.ini .
COPY setup.py .
COPY {{project}} {{project}}/
COPY src/ src/
COPY tests/ tests/

RUN pip install -e .
