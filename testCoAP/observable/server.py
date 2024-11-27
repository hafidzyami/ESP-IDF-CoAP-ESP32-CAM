import asyncio
import time
from aiocoap import Context, Message
from aiocoap.resource import ObservableResource, Site

class ObservableTemperatureResource(ObservableResource):
    def __init__(self):
        super().__init__()
        self._temperature = 25.0  # Default temperature

    async def render_get(self, request):
        return Message(payload=f"Temperature: {self._temperature}°C".encode())

    async def set_temperature(self, new_temperature):
        self._temperature = new_temperature
        self.updated_state()  # Notify observers about the change

async def main():
    # Create a resource and add it to the site
    root = Site()
    temperature_resource = ObservableTemperatureResource()
    root.add_resource(('temperature',), temperature_resource)

    # Explicitly bind the server to localhost (IPv4)
    context = await Context.create_server_context(root, bind=('127.0.0.1', None))
    print("CoAP server is running on 127.0.0.1...")

    # Simulate temperature changes
    while True:
        await asyncio.sleep(5)
        new_temp = 20.0 + 5.0 * (time.time() % 5)  # Simulated temperature
        print(f"Setting new temperature: {new_temp}°C")
        await temperature_resource.set_temperature(new_temp)

if __name__ == "__main__":
    asyncio.run(main())
