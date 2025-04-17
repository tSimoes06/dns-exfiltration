#!/usr/bin/env python3
import subprocess
import sys
import os
import venv
import time

def create_venv():
    """Create a virtual environment if it doesn't exist"""
    print("Setting up virtual environment...")
    venv_dir = 'venv'
    
    if not os.path.exists(venv_dir):
        print("Creating new virtual environment...")
        venv.create(venv_dir, with_pip=True)
        print("Virtual environment created successfully")
    else:
        print("Virtual environment already exists")
    
    # Get the path to the virtual environment's Python interpreter
    if sys.platform == 'win32':
        venv_python = os.path.join(venv_dir, 'Scripts', 'python.exe')
        pip_executable = os.path.join(venv_dir, 'Scripts', 'pip')
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate')
    else:
        venv_python = os.path.join(venv_dir, 'bin', 'python3')
        pip_executable = os.path.join(venv_dir, 'bin', 'pip')
        activate_script = os.path.join(venv_dir, 'bin', 'activate')
    
    # Activate the virtual environment
    if sys.platform == 'win32':
        activate_command = f'call {activate_script}'
    else:
        activate_command = f'source {activate_script}'
    
    print("\nActivating virtual environment...")
    try:
        # Using shell=True because source/call is a shell built-in
        subprocess.run(activate_command, shell=True, check=True)
        print("Virtual environment activated successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error activating virtual environment. You may need to activate it manually.")
        print(f"To activate, run: {activate_command}")
    
    return venv_python, pip_executable

def install_dependencies(venv_python, pip_executable):
    """Install required Python packages"""
    print("\nInstalling required packages...")
    try:
        # First upgrade pip using the venv's pip directly
        print("Upgrading pip...")
        subprocess.run([pip_executable, 'install', '--upgrade', 'pip'],
                      check=True, capture_output=True, text=True)
        
        # Install each requirement individually to better handle errors
        with open('requirements.txt', 'r') as f:
            requirements = [line.strip() for line in f if line.strip()]
        
        print("Installing project dependencies...")
        for req in requirements:
            try:
                print(f"Installing {req}...")
                subprocess.run([pip_executable, 'install', req],
                             check=True, capture_output=True, text=True)
                print(f"Successfully installed {req}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {req}:")
                print(f"stdout: {e.stdout}")
                print(f"stderr: {e.stderr}")
                return False
        
        print("Successfully installed all dependencies")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during installation:")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def main():
    print("Starting DNS Exfiltration Tool installation...")
    
    # Create and activate virtual environment
    venv_python, pip_executable = create_venv()
    
    # Install dependencies
    if not install_dependencies(venv_python, pip_executable):
        print("\nInstallation failed. Please try the following manual steps:")
        print("1. Activate the virtual environment:")
        if sys.platform == 'win32':
            print("   venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("2. Install requirements manually:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    print("\nInstallation complete!")
    print("\nThe virtual environment should now be activated.")
    print("If not, you can manually activate it with:")
    if sys.platform == 'win32':
        print("venv\\Scripts\\activate")
    else:
        print("source venv/bin/activate")
    
    print("\nAfter activation, you can run the test as described in the README.md file.")

if __name__ == '__main__':
    main() 