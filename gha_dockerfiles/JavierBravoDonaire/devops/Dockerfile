FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY --chown=1000 . /code

USER 1000

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

WORKDIR /code
ENV WORKON_HOME /tmp

RUN python3 -m venv .venv && \
    .venv/bin/pip install -U pip && \
    .venv/bin/pip install -r requirements.txt --no-cache-dir

ENV PATH=".venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
