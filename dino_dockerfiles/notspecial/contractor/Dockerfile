FROM notspecial/amivtex

# Ensure the de_CH.utf-8 locale exists, needed for weekday mapping
RUN apt-get update && apt-get install -y locales && \
    echo "de_CH.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen && \
    rm -rf /var/lib/apt/lists/*

# Create user with home directory and no password and change workdir
RUN useradd -md /contractor contractor
WORKDIR /contractor
# Run on port 8080 (does not require priviledge to bind)
EXPOSE 8080
# Environment variable for config, use path for docker secrets as default
ENV CONTRACTOR_CONFIG=/run/secrets/contractor_config

# Install bjoern and dependencies for install (we need to keep libev)
RUN apt-get update && apt-get install -y \
        musl-dev python-dev gcc libev-dev && \
    pip install bjoern

# Copy files to /contractor directory, install requirements
COPY ./ /contractor
RUN pip install -r /contractor/requirements.txt

# Switch user
USER contractor

# Start bjoern
CMD ["python3", "server.py"]
