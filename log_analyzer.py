#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
from datetime import datetime
import base64
import re

def load_logs():
    try:
        with open('dns_queries.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No log file found. Please run the DNS server first.")
        return []

def analyze_queries(queries):
    if not queries:
        return
    
    # Basic statistics
    total_queries = len(queries)
    unique_domains = len(set(q['query_name'] for q in queries))
    unique_clients = len(set(q['client_ip'] for q in queries))
    
    print(f"\nAnalysis Results:")
    print(f"Total queries: {total_queries}")
    print(f"Unique domains: {unique_domains}")
    print(f"Unique clients: {unique_clients}")
    
    # Extract potential exfiltrated data
    exfil_data = []
    for query in queries:
        # Look for base64-like patterns in subdomains
        subdomain = query['query_name'].split('.')[0]
        if re.match(r'^[A-Za-z0-9+/]+$', subdomain):
            try:
                # Try to decode the base64
                decoded = base64.b64decode(subdomain + '=' * (-len(subdomain) % 4))
                exfil_data.append(decoded.decode('utf-8', errors='ignore'))
            except:
                pass
    
    if exfil_data:
        print("\nPotential exfiltrated data found:")
        print("First few chunks:")
        for chunk in exfil_data[:5]:
            print(f"  {chunk[:50]}...")
    
    # Plot query frequency over time
    timestamps = [datetime.fromisoformat(q['timestamp']) for q in queries]
    plt.figure(figsize=(12, 6))
    plt.hist(timestamps, bins=50)
    plt.title('DNS Query Frequency Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Queries')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('dns_query_frequency.png')
    print("\nQuery frequency plot saved as 'dns_query_frequency.png'")

def main():
    queries = load_logs()
    analyze_queries(queries)

if __name__ == '__main__':
    main() 