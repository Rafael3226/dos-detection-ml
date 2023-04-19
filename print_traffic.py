import pyshark


def print_packet(packet):
    print(packet)


interface = 'Wi-Fi'

if __name__ == '__main__':
    # Create a PyShark capture object on the specified network interface
    capture = pyshark.LiveCapture(interface=interface)

    # Start capturing packets and process each packet using the callback function
    capture.apply_on_packets(print_packet)
