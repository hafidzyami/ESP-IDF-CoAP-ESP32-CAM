import asyncio
from aiocoap import Context, Message, PUT

async def coap_put():
    # Define the target CoAP server
    uri = "coap://172.20.10.2/Espressif"  # Replace with actual IP and port
    
    # Create the CoAP PUT request
    payload = "Hello, CoAP!"
    request = Message(code=PUT, uri=uri, payload=payload.encode('utf-8'))
    
    # Create the CoAP context and send the request
    context = await Context.create_client_context()
    try:
        response = await context.request(request).response
        print(f"Response Code: {response.code}")
        print(f"Response Payload: {response.payload.decode('utf-8')}")
    except Exception as e:
        print(f"Request failed: {e}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(coap_put())
