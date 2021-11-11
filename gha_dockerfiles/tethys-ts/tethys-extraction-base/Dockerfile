FROM python:3.8-slim

# ENV TZ='Pacific/Auckland'

# RUN apt-get update && apt-get install -y unixodbc-dev gcc g++ libspatialindex-dev python-rtree

# Install base dependencies
COPY requirements_base.txt ./
RUN pip install --no-cache-dir -r requirements_base.txt

# Install Tethys packages - these change more frequently than the base ones
COPY requirements_tethys.txt ./
RUN pip install --no-cache-dir -r requirements_tethys.txt

# COPY ts_data.py ./

CMD ["python"]
