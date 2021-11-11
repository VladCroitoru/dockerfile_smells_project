# For more information, please refer to https://aka.ms/vscode-docker-python
FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10 as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

# Install pre-requirements
RUN apk add build-base

RUN pip install --prefix=/install -r /requirements.txt

FROM base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pre-requirements
RUN apk add build-base

# Install pip requirements
COPY --from=builder /install /usr/local

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 3000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "parsimony:api", "--host", "0.0.0.0", "--port", "3000"]
