FROM nginx:1.12.1-alpine
MAINTAINER 	Mario Vejlupek <mario@vejlupek.cz>

ENV service_id=change_service_id_var
ENV service_host=change_service_host_var
ENV service_location=change_service_location_var

COPY entrypoint.sh /
COPY nginx-proxy-gen.sh /

ENTRYPOINT ["/entrypoint.sh"]

