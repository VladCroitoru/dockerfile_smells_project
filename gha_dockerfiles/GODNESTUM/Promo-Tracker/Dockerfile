# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN pip install virtualenv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . /app

# Expose Port
ENV PORT 8501
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "promo.py"]

# Straemlit/specific commands for config Not needed generally
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e' "\
[general]\n\
email = \"\"n\
" > /root/.streamlit/config.toml'

RUN bash -c 'echo -e' "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

