FROM python:latest

RUN apt update
RUN apt install -y ghostscript python3-tk python3-opencv
RUN pip3 install "camelot-py[cv]"

RUN mkdir /mhlw_pdf
COPY mhlw_pref_pdf_to_text.py /root/
COPY latest_pdf_to_text.sh /root/
