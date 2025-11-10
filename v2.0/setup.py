import sys
from cx_Freeze import setup, Executable

# Replace "my_script.py" with the actual name of your Python script
target_script = "login.py"

# Create the executable
executables = [Executable(target_script)]

# Specify any additional dependencies
# (optional, modify as per your project's requirements)
options = {
    'build_exe': {
        'packages': [],
        'excludes': [],
        'include_files': []
    }
}

# Setup configuration
setup(
    name="MyScript",
    version="1.0",
    description="My Script",
    options=options,
    executables=executables
)