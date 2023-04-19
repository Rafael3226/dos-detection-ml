import pyshark
import pickle
import ExtractFeatures

models = {
    1: './models/logistic_regression_model.pkl',
    2: './models/decision_tree_model.pkl',
    3: './models/random_forest_model.pkl',
    4: './models/neural_network_model.pkl',
}
interface = 'Wi-Fi'
host_ip = '10.24.22.152'
broadcast = '224.77.77.77'
ip_list = {}

# Load the decision tree model using pickle
with open(models[2], 'rb') as f:
    model = pickle.load(f)

# Define a function to extract relevant features from each packet


def extract_features(packet):
    global ip_list
    global host_ip
    parsed_packet = ExtractFeatures.Packet(packet)
    dst_ip = packet.ip.dst
    src_ip = packet.ip.src
    ip_lable = src_ip if host_ip == dst_ip else dst_ip
    try:
        if dst_ip in ip_list:
            return ip_list[ip_lable].addPacket(parsed_packet)
        else:
            ip_list[ip_lable] = ExtractFeatures.ExtractFeatures(host_ip)
            return ip_list[ip_lable].addPacket(parsed_packet)
    except Exception as e:
        print(e)
        return []


# Define a callback function to process each captured packet
def packet_callback(packet):
    # extract features from the packet
    features = extract_features(packet)
    # classify the packet using the loaded model
    if len(features):
        result = model.predict(features)[0]
        # print True or False based on the classification result
        print(result)


def print_packet(packet):
    print(packet)


if __name__ == '__main__':
    # Create a PyShark capture object on the specified network interface
    capture = pyshark.LiveCapture(
        interface=interface, display_filter=f'(ip.src == {host_ip} || ip.dst == {host_ip}) && (ip.src != {broadcast} || ip.dst != {broadcast})')

    # Start capturing packets and process each packet using the callback function
    capture.apply_on_packets(packet_callback)
