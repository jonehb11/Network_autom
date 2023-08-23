import json
import ipaddress

with open('ip-ranges.json') as file:
    data = json.load(file)   

inp = input("Enter an IP address (or press enter to search by AWS service): ")

# Function to determine if an IP address is within a given IP prefix (subnet)
def ip_in_subnet(ip, subnet):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet)

# If the user enters an IP
if inp:
    found = False
    for i in data['prefixes']:
        if 'ip_prefix' in i and ip_in_subnet(inp, i['ip_prefix']):
            print(i)
            found = True
    if not found:
        print("No matching subnet found for the provided IP.")
else:
    services = [
        "AMAZON", "AMAZON_APPFLOW", "AMAZON_CONNECT", "API_GATEWAY",
        "CHIME_MEETINGS", "CHIME_VOICECONNECTOR", "CLOUD9", "CLOUDFRONT", 
        "CLOUDFRONT_ORIGIN_FACING", "CODEBUILD", "DYNAMODB", "EBS", "EC2", 
        "EC2_INSTANCE_CONNECT", "GLOBALACCELERATOR", "KINESIS_VIDEO_STREAMS", 
        "ROUTE53", "ROUTE53_HEALTHCHECKS", "ROUTE53_HEALTHCHECKS_PUBLISHING", 
        "ROUTE53_RESOLVER", "S3", "WORKSPACES_GATEWAYS"
    ]
    print("\nAvailable AWS services:")
    for service in services:
        print(service)
    
    chosen_service = input("\nEnter the AWS service you want to search for: ").strip().upper()
    
    if chosen_service in services:
        for i in data['prefixes']:
            if 'service' in i and i['service'] == chosen_service:
                print(i)
    else:
        print("Invalid service chosen.")
