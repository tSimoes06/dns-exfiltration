#!/usr/bin/env python3
from dnslib import QTYPE, RR, A
from dnslib.server import DNSServer, BaseResolver
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('dns_queries.log'),
        logging.StreamHandler()
    ]
)

class DNSLogger:
    def __init__(self):
        self.queries = []
    
    def log_query(self, request, client_ip):
        query = {
            'timestamp': datetime.now().isoformat(),
            'client_ip': client_ip,
            'query_name': str(request.q.qname),
            'query_type': QTYPE[request.q.qtype]
        }
        self.queries.append(query)
        logging.info(f"Query from {client_ip}: {query['query_name']} ({query['query_type']})")
        
        # Save to JSON file for later analysis
        with open('dns_queries.json', 'w') as f:
            json.dump(self.queries, f, indent=2)

class CustomResolver(BaseResolver):
    def __init__(self):
        self.logger = DNSLogger()
    
    def resolve(self, request, handler):
        reply = request.reply()
        self.logger.log_query(request, handler.client_address[0])
        
        # Always return a response
        reply.add_answer(RR(
            rname=request.q.qname,
            rtype=QTYPE.A,
            rclass=1,
            ttl=60,
            rdata=A("127.0.0.1")
        ))
        return reply

def main():
    resolver = CustomResolver()
    server = DNSServer(resolver, port=5300, address="0.0.0.0")
    print("Starting DNS server on port 5300...")
    server.start()

if __name__ == '__main__':
    main() 