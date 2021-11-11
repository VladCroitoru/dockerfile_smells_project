FROM python:3

RUN pip install django \
  django-extensions \
  requests \
  bs4

# COPY ./aorta /aorta
WORKDIR /python

CMD ["python", "AortaBOT.py"]
# CMD ["bash"]
