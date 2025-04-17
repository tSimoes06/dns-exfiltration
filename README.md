# DNS Exfiltration Tool

A Python-based tool for demonstrating DNS exfiltration techniques. This project includes a DNS server, client, and analysis tools to simulate and analyze DNS-based data exfiltration. ONLY FOR STUDY PURPOSES!!

## Features

- DNS server that logs all incoming queries
- DNS client for data exfiltration
- Log analysis and visualization tools
- Base64 encoding for data transmission
- Process management and cleanup utilities

## Requirements

- Python 3.6 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dns-exfiltration.git
cd dns-exfiltration
```

2. Run the installation script:
```bash
python3 install.py
```

3. Activate the virtual environment:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. To deactivate the virtual environment when you're done:
```bash
deactivate
```

## Running the Test

The test consists of three main components that need to be run in sequence:

1. Start the DNS server (in a separate terminal):
```bash
python3 dns_server.py
```
The server will start on port 5300 and begin logging DNS queries.

2. Run the exfiltration test (in a new terminal):
```bash
python3 dns_exfiltrator.py
```
This will send a test message through DNS queries to the server.

3. Analyze the results (in a new terminal):
```bash
python3 log_analyzer.py
```
This will analyze the logged queries and generate visualizations.

4. Clean up when done:
```bash
python3 cleanup.py
```
This will stop the DNS server and clean up log files.

## Uninstallation

To completely remove the project and all its components:

1. If the virtual environment is active, deactivate it:
```bash
deactivate
```

2. Run the uninstallation script:
```bash
python3 uninstall.py
```
This will:
- Remove the virtual environment
- Uninstall all project dependencies
- Clean up log files and generated data

3. (Optional) Delete the project directory:
```bash
cd .. && rm -rf dns-exfiltration
```

Note: If you encounter any errors during uninstallation:
- Make sure you've deactivated the virtual environment first
- If you get permission errors, you might need to close any programs using the project files
- On some systems, you might need to manually delete the virtual environment directory:
  ```bash
  rm -rf venv
  ```

## Test Results

After running the test, you should see:
- A log file (`dns_queries.log`) containing all DNS queries
- A JSON file (`dns_queries.json`) with structured query data
- A visualization (`dns_query_frequency.png`) showing query patterns

## Project Structure

- `dns_server.py`: DNS server implementation
- `dns_exfiltrator.py`: Client for data exfiltration
- `log_analyzer.py`: Analysis and visualization tools
- `cleanup.py`: Process and file cleanup utilities
- `requirements.txt`: Project dependencies
- `install.py`: Installation script
- `uninstall.py`: Uninstallation script

## Troubleshooting

If you encounter any issues:
1. Make sure the virtual environment is activated
2. Check that the DNS server is running before running the exfiltrator
3. Ensure port 5300 is available and not blocked by a firewall
4. Run the cleanup script if processes get stuck
5. If problems persist, try running the uninstallation script and reinstalling

## Security Note

This tool is for educational purposes only. Do not use it for malicious purposes or on systems without proper authorization.

## License

MIT License - See LICENSE file for details 