# poetryからpipモジュールを取り出す
FROM python:3.9.7 as builder

RUN pip install --no-cache-dir poetry==1

WORKDIR /work

COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt -o requirements.txt
RUN poetry export --dev -f requirements.txt -o requirements-dev.txt

# 実行環境ベース
FROM python:3.9.7 as runbase

ENV PYTHONUNBUFFERED=1

WORKDIR /work

COPY --from=builder /work/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

RUN groupadd -r app && \
    useradd -r -g app app && \
    chown -R app:app /app

# テスト環境
FROM runbase as tester

COPY --from=builder /work/requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements-dev.txt

WORKDIR /app

USER app

COPY kakeibo_exporter/ ./kakeibo_exporter/
COPY tests/ ./tests/

CMD ["pytest", "-s", "--cov"]

# 実行環境
FROM runbase as runner

WORKDIR /app

USER app

COPY kakeibo_exporter/ ./kakeibo_exporter/