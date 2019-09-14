. venv/bin/activate

export FLASK_APP=api
export FLASK_ENV=development
export APP_SETTINGS="config.DevelopmentConfig"

echo "Running development server"

flask run