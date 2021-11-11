FROM jupyter/scipy-notebook:dc9744740e12

LABEL maintainer="Kristof Ostir"

# Install from Conda GDAL, rasterio, geopandas, descartes
# Install from Conda-Forge folium, geojson, contextily, geoplot

RUN conda install --quiet --yes \
    'gdal' \
    'rasterio' \
    'geopandas' && \
    conda install -c conda-forge --quiet --yes \
    'folium' \
    'contextily' \
    'geoplot' \
    'geojson' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER