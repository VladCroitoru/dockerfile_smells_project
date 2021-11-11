FROM python:3.7.4-alpine3.10

WORKDIR /app

COPY requirements.local.txt .
COPY requirements.txt .

RUN python -m pip install --requirement requirements.local.txt && \
    python -m pip install sphinx-autobuild && \
    rm requirements.local.txt && \
    rm requirements.txt

# Ignored files should be the auto generated json files in  _static/api directory,
# but it doesn't look like sphinx-autobuild allows such fine grained control over what is ignored.
CMD ["sphinx-autobuild", "--host", "0.0.0.0", "--port", "8080", "--ignore", "*.json", "/app", "/home/python/docs/_build/html"]
