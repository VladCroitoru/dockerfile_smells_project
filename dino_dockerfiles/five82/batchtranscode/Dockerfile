# Use five82/ffmpeg-git as a base image
FROM five82/ffmpeg-git

# Environment variables
ENV encoder=x265 \
    bitdepth=10 \
    audioencoder=libopus \
    stereobitrate=128k \
    surrfiveonebitrate=384k \
    surrsevenonebitrate=512k \
    uhdcrf=20 \
    hdcrf=21 \
    sdcrf=20 \
    preset=medium \
    cropblackbars=true \
    enablelogging=true

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN \
# Add required packages
apt update -qq && \
apt install -y --no-install-recommends rsync && \
# Set transcode script as executable
chmod +x /app/transcode.sh

# Run transcode.sh when the container launches
CMD ["/app/transcode.sh"]
