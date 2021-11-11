FROM certbot/certbot

# Set the stage
WORKDIR /var/lets-do-dns

# Install lets-do-dns requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install lets-do-dns package
COPY . ./
RUN pip install --no-cache-dir .

# Reset WORKDIR to certbot's default
WORKDIR /opt/certbot
