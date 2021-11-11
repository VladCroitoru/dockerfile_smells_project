FROM python:3.9

# Setup a mount point for volumes
RUN mkdir /serve && chmod 777 /serve

# Install dependencies
WORKDIR /restfileserver
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/restfileserver"

# Copy in the rest of the module files
COPY . .

ENTRYPOINT ["python", "-m", "restfileserver"]
