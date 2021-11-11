ARG IMAGE_NAME
ARG IMAGE_VERSION

FROM ${IMAGE_NAME}:${IMAGE_VERSION}

RUN pip install --upgrade pip setuptools

WORKDIR /opt/cppbuiltins

COPY requirements-setup.txt .
COPY README.md .
COPY setup.py .
COPY src/ src/
RUN pip install -e .

COPY requirements-tests.txt .
RUN pip install -r requirements-tests.txt
COPY pytest.ini .
COPY tests/ tests/
