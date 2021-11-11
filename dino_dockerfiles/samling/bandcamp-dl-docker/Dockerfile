FROM samling/docker-python-base

# Clone latest version of bandcamp-dl
RUN git clone --depth 1 https://github.com/iheanyi/bandcamp-dl /app

# Move requirements.txt into folder
ADD requirements.txt /app/

# Set permissions
RUN chown -R root /app

# Create downloads directory
RUN mkdir /downloads

# Install requirements via pip
RUN pip install -r /app/requirements.txt

# Run script with python binary
ENTRYPOINT ["/usr/bin/python", "/app/bandcamp-dl/bandcamp-dl.py", "--overwrite", "--base-dir=/downloads"] 
