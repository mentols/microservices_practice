FROM nginx:alpine

#RUN nginx -s reload
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
