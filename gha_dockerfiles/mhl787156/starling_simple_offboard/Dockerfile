ARG VERSION=latest
ARG REGISTRY
FROM ${REGISTRY}uobflightlabstarling/starling-controller-base:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libboost-system-dev \
        git \
        wget \
        python3-pip \
        libgeographic-dev \
        geographiclib-tools \
    && rm -rf /var/lib/apt/lists/*

## Ensure geographiclib is properly installed with FindGeographicLib available
RUN wget https://raw.githubusercontent.com/mavlink/mavros/ros2/mavros/scripts/install_geographiclib_datasets.sh \
    && bash install_geographiclib_datasets.sh \
    && ln -s /usr/share/cmake/geographiclib/FindGeographicLib.cmake /usr/share/cmake-3.16/Modules/

COPY simple_offboard /ros_ws/src/simple_offboard
COPY simple_offboard_msgs /ros_ws/src/simple_offboard_msgs
COPY .git /ros_ws/src/.git
COPY .gitmodules /ros_ws/src/.gitmodules

# Build the package
RUN . /opt/ros/${ROS_DISTRO}/setup.sh \
    && export CMAKE_PREFIX_PATH=$AMENT_PREFIX_PATH:$CMAKE_PREFIX_PATH \
    && cd /ros_ws \
    && colcon build --packages-select simple_offboard_msgs simple_offboard \
    && rm -r build

COPY run.sh .

CMD ["./run.sh"]