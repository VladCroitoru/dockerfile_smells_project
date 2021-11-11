FROM jitsusama/lets-do-dns

# Set the stage
WORKDIR /opt/hostel-huptainer

# Install hostel-huptainer requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install hostel-huptainer package
COPY . ./
RUN pip install --no-cache-dir .

# Reset WORKDIR to certbot's default
WORKDIR /opt/certbot
