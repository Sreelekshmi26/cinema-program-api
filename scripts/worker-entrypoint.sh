#!/bin/sh

until cd /app
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A movies_api worker --beat --loglevel=info --concurrency 1 -E