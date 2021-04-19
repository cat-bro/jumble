venv_name='.watchdog'

if [ ! -d $venv_name ]; then
    virtualenv -p python3 $venv_name
    . $venv_name/bin/activate
    pip3 install -r requirements.txt
else
    . $venv_name/bin/activate
fi

python run_watch.py "$1"