FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt
RUN pip install fastapi --upgrade
RUN chmod 750 /app
ENV LOG_LEVEL=warning
ENV ACCESS_LOG=
# Expose ports
EXPOSE 80