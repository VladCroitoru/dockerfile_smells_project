FROM condaforge/miniforge3

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED 1

ENV USERNAME=panoptes
ENV BASE_DIR=/images

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      gphoto2

# Create user, image directory, and update permissions for usb.
RUN useradd --no-create-home -G plugdev ${USERNAME} && \
    mkdir -p "${BASE_DIR}" && chmod 777 "${BASE_DIR}" && \
    mkdir -p /app && chmod 777 /app

COPY environment.yaml .
RUN conda update -n base conda && \
    conda-env update -n base -f environment.yaml && \
    conda clean -tipsy && \
    conda clean -y --force-pkgs-dirs && \
    chown -R "${USERNAME}:${USERNAME}" /opt/conda

WORKDIR /app
USER "${USERNAME}"
COPY main.py .

EXPOSE 6565

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6565"]