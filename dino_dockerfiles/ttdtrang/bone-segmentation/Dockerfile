FROM python:3.4.6
RUN pip install nibabel scikit-image
COPY bone-segmentation.py /bone-segmentation.py
ENTRYPOINT ["python", "/bone-segmentation.py"]
