#
# Dockerfile for tesseract
#

FROM debian:jessie
MAINTAINER Jan Thurau <jan@syslabs.it>

RUN apt-get update && apt-get install -y autoconf build-essential libtool git wget libpng12-dev \
 libtiff5-dev zlib1g-dev zlibc



RUN wget http://leptonica.com/source/leptonica-1.73.tar.gz \
		&& tar xvfz leptonica-1.73.tar.gz \
		&& cd leptonica-1.73 \
		&& ./configure \
		&& make \
		&& make install \
		&& cd ..

RUN git clone https://github.com/tesseract-ocr/tesseract.git \
			&& cd tesseract \
			&& git checkout 3.04.01 \
			&& ./autogen.sh \
			&& ./configure \
			&& make \
			&& make install \
			&& cd .. \
		&& git clone https://github.com/tesseract-ocr/tessdata.git \
			&& cd tessdata \
		    && git checkout 3.04.00 \
			&& mv * /usr/local/share/tessdata/ \
			&& cd .. \
		&& rm -rf tesseract tessdata /var/cache/apk/*

ENV PATH /usr/local/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/lib
