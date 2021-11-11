ARG image_tag=latest
FROM elifesciences/pattern-library_ui-builder:${image_tag} AS ui-builder

FROM nginx:1.15.0-alpine
COPY --from=ui-builder /public/ /usr/share/nginx/html/
