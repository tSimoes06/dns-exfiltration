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
    else:
        venv_python = os.path.join(venv_dir, 'bin', 'python3')
    
    return venv_python

def install_dependencies(venv_python):
    """Install required Python packages"""
    print("\nInstalling required packages...")
    try:
        # First upgrade pip
        print("Upgrading pip...")
        subprocess.run([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'],
                      check=True, capture_output=True, text=True)
        
        # Then install requirements
        print("Installing project dependencies...")
        result = subprocess.run([venv_python, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                              check=True, capture_output=True, text=True)
        print("Successfully installed all dependencies")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies:")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

def main():
    print("Starting DNS Exfiltration Tool installation...")
    
    # Create virtual environment
    venv_python = create_venv()
    
    # Install dependencies
    if not install_dependencies(venv_python):
        print("Installation failed. Please check the error messages above.")
        sys.exit(1)
    
    print("\nInstallation complete!")
    print("\nTo activate the virtual environment:")
    if sys.platform == 'win32':
        print("venv\\Scripts\\activate")
    else:
        print("source venv/bin/activate")
    
    print("\nAfter activation, you can run the test as described in the README.md file.")

if __name__ == '__main__':
    main() 