#!/bin/bash

celery --app=my_app_new.background_tasks.celery_task:celery_app flower
