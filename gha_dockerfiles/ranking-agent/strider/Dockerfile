FROM python:3.9

# Add image info
LABEL org.opencontainers.image.source https://github.com/ranking-agent/strider

# set up requirements
WORKDIR /app

# Install requirements
ADD requirements-lock.txt .
RUN pip install -r requirements-lock.txt

# Copy in files
ADD . .

# Set up base for command and any variables
# that shouldn't be modified
ENTRYPOINT ["gunicorn", "strider.server:APP", "-k", "uvicorn.workers.UvicornWorker"]

# Variables that can be overriden
CMD [ "--bind", "0.0.0.0:5781", "--workers", "4", "--threads", "3"]
