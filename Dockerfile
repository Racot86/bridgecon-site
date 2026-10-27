# Bridge Con website: static pages served by nginx. In Coolify choose the
# Dockerfile build pack; the container listens on port 80.
FROM python:3.12-alpine AS build
WORKDIR /site
COPY build.py ./
COPY src ./src
RUN python3 -I build.py

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /site/public /usr/share/nginx/html
EXPOSE 80
