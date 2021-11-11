FROM mwaeckerlin/boar-data
MAINTAINER mwaeckerlin
env TERM=xterm

env INPUT_DIR=/home/ftp/upload
env ROTATE_DIR=/home/ftp/rotate
env PASS_DIR=/home/ftp/pass
env ROTATEPASS_DIR=/home/ftp/rotate-pass
env OUTPUT_DIR=/data/dokumente
env CONFIG_DIR=/data/configs/scan
env TMP_DIR=/tmp
env LANGUAGE=deu
env RESOLUTION=300
env OPTIONS="-quiet -rgb -enforcehocr2pdf -sloppy_text"
env MAXPIXELS=40000000

USER root
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
       pdfsandwich pdftk libjpeg-progs \
       inotify-tools poppler-utils tesseract-ocr-.*

ADD ocr.sh /ocr.sh
ADD start.sh /start.sh
CMD /start.sh
