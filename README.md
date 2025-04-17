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

## Troubleshooting

If you encounter any issues:
1. Make sure the virtual environment is activated
2. Check that the DNS server is running before running the exfiltrator
3. Ensure port 5300 is available and not blocked by a firewall
4. Run the cleanup script if processes get stuck

## Security Note

This tool is for educational purposes only. Do not use it for malicious purposes or on systems without proper authorization.

## License

MIT License - See LICENSE file for details 