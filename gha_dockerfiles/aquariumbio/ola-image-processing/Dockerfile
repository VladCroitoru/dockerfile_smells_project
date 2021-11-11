# For more information, please refer to https://aka.ms/vscode-docker-python
ARG PYTHON_VERSION=3.9
ARG PLATFORM=slim-buster
FROM python:${PYTHON_VERSION}-${PLATFORM} AS ola_python

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
