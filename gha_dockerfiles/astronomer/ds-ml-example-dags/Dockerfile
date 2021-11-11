FROM quay.io/astronomer/ap-airflow:2.1.3-1-buster-onbuild

ENV AIRFLOW__CORE__XCOM_BACKEND=include.gcs_xcom_backend.GCSXComBackend

USER root

# Required for some ML/DS dependencies
RUN apt-get update -y
RUN apt-get install libgomp1 -y

USER astro