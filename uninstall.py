#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import platform

def remove_venv():
    """Remove the virtual environment directory"""
    print("Removing virtual environment...")
    venv_dir = 'venv'
    
    if os.path.exists(venv_dir):
        try:
            shutil.rmtree(venv_dir)
            print("Virtual environment removed successfully")
        except Exception as e:
            print(f"Error removing virtual environment: {e}")
            return False
    else:
        print("Virtual environment not found")
    
    return True

def uninstall_packages():
    """Uninstall the packages installed for this project"""
    print("\nUninstalling packages...")
    packages = ['dnslib', 'dnspython', 'matplotlib']
    
    for package in packages:
        try:
            print(f"Uninstalling {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'uninstall', '-y', package],
                         check=True, capture_output=True, text=True)
            print(f"Successfully uninstalled {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling {package}:")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")
    
    return True

def cleanup_files():
    """Remove any remaining project files"""
    print("\nCleaning up project files...")
    files_to_remove = [
        'dns_queries.log',
        'dns_queries.json',
        'dns_query_frequency.png',
        '__pycache__'
    ]
    
    for file in files_to_remove:
        try:
            if os.path.exists(file):
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.remove(file)
                print(f"Removed {file}")
        except Exception as e:
            print(f"Error removing {file}: {e}")

def main():
    print("Starting DNS Exfiltration Tool uninstallation...")
    
    # Remove virtual environment
    if not remove_venv():
        print("Failed to remove virtual environment")
        sys.exit(1)
    
    # Uninstall packages
    uninstall_packages()
    
    # Clean up files
    cleanup_files()
    
    print("\nUninstallation complete!")
    print("All project components have been removed.")
    print("\nNote: If you want to completely remove the project, you can now delete the project directory.")

if __name__ == '__main__':
    main() 