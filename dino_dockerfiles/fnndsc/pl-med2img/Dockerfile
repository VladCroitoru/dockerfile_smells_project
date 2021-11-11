FROM fnndsc/python:3.8.5-ubuntu20.04
LABEL maintainer="Arushi Vyas <dev@babyMRI.org>"

# Python libs which were originally mentioned in requirements.txt, but
# don't seem to actually be used
# python3-packaging python3-pygments python3-pyparsing python3-dateutil python3-six
# python3-urwid python3-cycler python3-kiwisolver python3-pil
# can also remove python3-matplotlib after it's removed from med2image
RUN apt-get update \
    && apt-get install -y python3-matplotlib python3-numpy python3-nibabel python3-pydicom \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["med2img", "--help"]
