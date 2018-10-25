web: python run.py
web: gunicorn run:app

# For python, run.py is the name of the file with the __init__ like structure.
# It is the first file that is run (that runs all other files)
# 
# For Gunicorn, the default name is "app:app", but the main file name should
# replace the first "app" if it is not called app.py, so "run:app" for example
# if the __init__ file is called run.py
