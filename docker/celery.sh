#!/bin/sh

celery --app=my_app_new.background_tasks.celery_task:celery_app worker -l INFO

