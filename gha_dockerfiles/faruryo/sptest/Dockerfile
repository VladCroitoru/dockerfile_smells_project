# Extract the pip module from poetry.toml
FROM python:3.9.7 as builder

RUN pip install --no-cache-dir poetry==1

WORKDIR /work

COPY poetry.lock pyproject.toml ./

RUN poetry export --without-hashes -f requirements.txt -o requirements.txt
RUN poetry export --dev --without-hashes -f requirements.txt -o requirements-dev.txt

# -----------------------------------------------------------------------------
FROM python:3.9.7 as runbase

ENV PYTHONUNBUFFERED=1

WORKDIR /work

COPY --from=builder /work/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

RUN groupadd -r app && \
    useradd -r -g app app && \
    chown -R app:app /app

# -----------------------------------------------------------------------------
FROM runbase as tester

COPY --from=builder /work/requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements-dev.txt

WORKDIR /app

USER app

COPY sptest/ ./sptest/
COPY tests/ ./tests/

CMD ["pytest", "-s", "--cov"]

# -----------------------------------------------------------------------------
FROM runbase as runner

WORKDIR /app

USER app

COPY sptest/ ./sptest/