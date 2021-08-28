#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
# Start nginx service
# Run in the foreground of the Docker container
nginx -g 'daemon off;'