FROM texlive/texlive:TL2019-historic as build
COPY . . 

RUN make
RUN mkdir build/output 
RUN make copy

FROM nginx:1.16.0-alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm /usr/share/nginx/html/index.html
RUN rm /usr/share/nginx/html/50x.html
COPY --from=build build/output /usr/share/nginx/html
RUN nginx -t