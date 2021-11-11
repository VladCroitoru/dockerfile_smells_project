FROM python:3.9
RUN mkdir slide
RUN cd slide
COPY fetchSlide.py .
COPY requirement.txt .
RUN pip install -r requirement.txt
ENTRYPOINT ["python", "./fetchSlide.py"]
