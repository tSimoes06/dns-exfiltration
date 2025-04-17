#!/usr/bin/env python3
import os
import sys
import signal
import subprocess
import time

def cleanup_processes():
    """Find and terminate any running DNS server processes"""
    print("Cleaning up processes...")
    
    # Find all Python processes running dns_server.py
    try:
        if sys.platform == 'win32':
            # Windows
            result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq python.exe', '/FO', 'CSV'],
                                  capture_output=True, text=True)
            processes = [line.split(',')[1].strip('"') for line in result.stdout.split('\n')[1:] if line]
        else:
            # Unix-like systems
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            processes = [line.split()[1] for line in result.stdout.split('\n') 
                        if 'dns_server.py' in line and not 'cleanup.py' in line]
        
        # Terminate each process
        for pid in processes:
            try:
                pid = int(pid)
                print(f"Terminating process {pid}...")
                os.kill(pid, signal.SIGTERM)
                time.sleep(1)  # Give process time to terminate
                
                # If process is still running, force kill it
                try:
                    os.kill(pid, 0)  # Check if process exists
                    print(f"Process {pid} still running, forcing termination...")
                    os.kill(pid, signal.SIGKILL)
                except OSError:
                    pass  # Process already terminated
                    
            except (ValueError, OSError) as e:
                print(f"Error terminating process {pid}: {e}")
                
    except Exception as e:
        print(f"Error finding processes: {e}")

def cleanup_files():
    """Remove log files and other temporary files"""
    print("Cleaning up files...")
    files_to_remove = [
        'dns_queries.log',
        'dns_queries.json',
        'dns_query_frequency.png'
    ]
    
    for file in files_to_remove:
        try:
            if os.path.exists(file):
                os.remove(file)
                print(f"Removed {file}")
        except Exception as e:
            print(f"Error removing {file}: {e}")

def main():
    print("Starting cleanup...")
    
    # Clean up processes
    cleanup_processes()
    
    # Clean up files
    cleanup_files()
    
    print("Cleanup complete!")

if __name__ == '__main__':
    main() 