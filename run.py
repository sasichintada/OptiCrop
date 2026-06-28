# run.py - Launcher for OptiCrop
import os
import sys
import subprocess

# Run the app from the new Application folder location
app_dir = os.path.join(os.path.dirname(__file__), '5.Project_Development_Phase', 'Application')
os.chdir(app_dir)

# Run app.py
subprocess.run([sys.executable, 'app.py'])