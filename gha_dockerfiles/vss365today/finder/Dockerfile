FROM python:3.9-alpine

# Set any env values we need
ENV PYTHONPATH=/app

# Copy the app files into the container
RUN mkdir -p /app
COPY [ "get-requirements.py", "poetry.lock", "pyproject.toml", "/app/" ]
WORKDIR /app

# Install required deps
RUN python3 -m pip install pip --upgrade && \
    pip3 install --no-cache-dir toml && \
    python3 ./get-requirements.py && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm ./requirements.txt

# Start the app
ENTRYPOINT [ "python", "./finder.py" ]
