FROM python:3.7-slim-buster

RUN useradd --create-home --shell /bin/bash LCPB
WORKDIR /home/LCPB

ENV QT_QUICK_BACKEND=software

RUN apt-get update && apt-get install -y --no-install-recommends \
libglib2.0-0 \
python3-pyqt5.qtopengl libxcb-xinerama0 \
evince nano

COPY . ./AMi_Image_Analysis
RUN chown -R LCPB ./AMi_Image_Analysis
RUN chgrp -R LCPB ./AMi_Image_Analysis

USER LCPB
WORKDIR /home/LCPB/AMi_Image_Analysis
RUN python3 Setup.py

RUN /home/LCPB/python/venvs/AMI_IMAGE_ANALYSIS_TENSORFLOW1/bin/python \
-m pip cache purge

WORKDIR /home/LCPB
ENV PATH="/home/LCPB/AMi_Image_Analysis/bin:$PATH"
RUN echo 'alias manual="evince /home/LCPB/AMi_Image_Analysis/Manual_AMi_Image_Analysis.pdf &"' >> ~/.bashrc
RUN echo 'echo 'TO DISPLAY the manual type "manual"'' >> ~/.bashrc

CMD ["bash"]
