from src.physical_layer import PhysicalLayer
from src.data_link_layer import DataLinkLayer
from src.network_layer import NetworkLayer
from src.transport_layer import TransportLayer
from src.session_layer import SessionLayer
from src.presentation_layer import PresentationLayer
from src.application_layer import ApplicationLayer
from src.mock_route import MockRoute

def main():
    # Create instances of the layers
    physical_layer = PhysicalLayer()
    data_link_layer = DataLinkLayer()
    network_layer = NetworkLayer()
    transport_layer = TransportLayer()
    session_layer = SessionLayer()
    presentation_layer = PresentationLayer()
    application_layer = ApplicationLayer()

    # Simulate sending some data
    data = "Hello, world!"
    print(f"Original data: {data}")

    # Create a mock route
    mock_route = MockRoute()
    mock_route.destination = "192.168.1.1"
    mock_route.next_hop = "192.168.1.2"
    network_layer.add_route(mock_route.destination, mock_route.next_hop)

    # Use the layers to process the data
    application_layer.send(data)
    encoded_data = presentation_layer.encode(data)
    session_id = "1234"
    session_layer.establish(session_id)
    segmented_data = transport_layer.segment(encoded_data, 5)
    bitstream = ""
    for segment in segmented_data:
        framed_data = data_link_layer.frame(segment)
        # print(f"Transmitting framed data: {framed_data}")
        bitstream += physical_layer.transmit(framed_data)
        # Here you would actually send the bitstream over the network

    # Simulate receiving the same data
    # print(f"Received bitstream: {bitstream}")

    # Use the layers to process the data
    framed_data = physical_layer.receive(bitstream)
    segment = data_link_layer.unframe(framed_data)
    segmented_data = [segment] 
    encoded_data = transport_layer.reassemble(segmented_data)
    session_layer.terminate(session_id)
    data = presentation_layer.decode(encoded_data)
    application_layer.receive(data)

if __name__ == "__main__":
    main()