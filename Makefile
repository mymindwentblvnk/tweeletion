env:
	rm -R venv && virtualenv -p python3 venv;
	. venv/bin/activate && pip install -r requirements.txt && deactivate;
	if [ ! -f settings.py ]; then cp rename_to_settings.py settings.py; fi

run:
	if [ ! -d venv || ! -f settings.py ]; then make env; fi
	. venv/bin/activate && python run.py && deactivate
