import statistics
import numpy as np
import pandas as pd


class ExtractFeatures:
    def __init__(self, host_ip):
        self.destination_port = 0
        self.host_ip = host_ip
        self.bwd_timestamps = []
        self.fwd_lengths = []
        self.bwd_lengths = []
        self.fwd_segment_lengths = []
        self.bwd_segment_lengths = []
        self.syn_flag_count = 0
        self.push_flag_count = 0
        self.urg_flag_count = 0

    def addPacket(self, packet):
        self.destination_port = packet.destination_port
        self.bwd_timestamps.append(packet.timestamp)

        if self.host_ip == packet.dst_ip:
            self.fwd_lengths.append(int(packet.length))
            self.fwd_segment_lengths.append(int(packet.segment_length))
        else:
            self.bwd_lengths.append(int(packet.length))
            self.bwd_segment_lengths.append(int(packet.segment_length))

        return self.toSeries()

    def _get_total_length_of_fwd_packets(self):
        return sum(self.fwd_lengths)

    def _get_fwd_packet_length_max(self):
        if len(self.fwd_lengths) == 0:
            return 0
        return max(self.fwd_lengths)

    def _get_fwd_packet_length_mean(self):
        if len(self.fwd_lengths) == 0:
            return 0
        return np.mean(self.fwd_lengths)

    def _get_fwd_packet_length_std(self):
        if len(self.fwd_lengths) <= 2:
            return 0
        return statistics.stdev(self.fwd_lengths)

    def _get_bwd_packet_length_max(self):
        if len(self.bwd_lengths) < 1:
            return 0
        return max(self.bwd_lengths)

    def _get_bwd_packet_length_min(self):
        if len(self.bwd_lengths) < 1:
            return 0
        return min(self.bwd_lengths)

    def _get_bwd_packet_length_mean(self):
        if len(self.bwd_lengths) == 0:
            return 0
        return np.mean(self.bwd_lengths)

    def _get_bwd_packet_length_std(self):
        if len(self.bwd_lengths) <= 2:
            return 0
        return statistics.stdev(self.bwd_lengths)

    def _get_bwd_iat_total(self):
        if len(self.bwd_timestamps) < 2:
            return 0
        return sum(np.diff(self.bwd_timestamps))

    def _get_bwd_iat_mean(self):
        if len(self.bwd_timestamps) < 2:
            return 0
        return np.mean(np.diff(self.bwd_timestamps))

    def _get_bwd_iat_std(self):
        if len(self.bwd_timestamps) <= 2:
            return 0
        return statistics.stdev(np.diff(self.bwd_timestamps))

    def _get_bwd_iat_max(self):
        diff = np.diff(self.bwd_timestamps)
        if len(diff) == 0:
            return 0
        return max(np.diff(self.bwd_timestamps))

    def _get_min_packet_length(self):
        new_list = self.fwd_lengths + self.bwd_lengths
        if len(new_list) < 1:
            return 0
        return min(new_list)

    def _get_max_packet_length(self):
        new_list = self.fwd_lengths + self.bwd_lengths
        if len(new_list) == 0:
            return 0
        return max(new_list)

    def _get_packet_length_mean(self):
        new_list = self.fwd_lengths + self.bwd_lengths
        if len(new_list) == 0:
            return 0
        return np.mean(new_list)

    def _get_packet_length_std(self):
        new_list = self.fwd_lengths + self.bwd_lengths
        if len(new_list) <= 2:
            return 0
        return statistics.stdev(new_list)

    def _get_packet_length_variance(self):
        new_list = self.fwd_lengths + self.bwd_lengths
        if len(new_list) < 2:
            return 0
        return np.var(new_list)

    def _get_syn_flag_count(self):
        return self.syn_flag_count

    def _get_psh_flag_count(self):
        return self.push_flag_count

    def _get_urg_flag_count(self):
        return self.urg_flag_count

    def _get_down_up_ratio(self):
        if sum(self.bwd_lengths) == 0:
            return 0
        return sum(self.fwd_lengths)/sum(self.bwd_lengths)

    def _get_avg_fwd_segment_size(self):
        if len(self.fwd_segment_lengths) == 2:
            return 0
        return np.mean(self.fwd_segment_lengths)

    def _get_avg_bwd_segment_size(self):
        if len(self.bwd_segment_lengths) == 0:
            return 0
        return np.mean(self.bwd_segment_lengths)

    def _get_min_seg_size_forward(self):
        new_list = self.fwd_segment_lengths + self.bwd_segment_lengths
        if len(new_list) == 0:
            return 0
        return min(new_list)

    def toSeries(self):
        return pd.DataFrame({
            'destination port': self.destination_port,
            'total length of fwd packets': self._get_total_length_of_fwd_packets(),
            'fwd packet length max': self._get_fwd_packet_length_max(),
            'fwd packet length mean': self._get_fwd_packet_length_mean(),
            'fwd packet length std': self._get_fwd_packet_length_std(),
            'bwd packet length max': self._get_bwd_packet_length_max(),
            'bwd packet length min': self._get_bwd_packet_length_min(),
            'bwd packet length mean': self._get_bwd_packet_length_mean(),
            'bwd packet length std': self._get_bwd_packet_length_std(),
            'bwd iat total': self._get_bwd_iat_total(),
            'bwd iat mean': self._get_bwd_iat_mean(),
            'bwd iat std': self._get_bwd_iat_std(),
            'bwd iat max': self._get_bwd_iat_max(),
            'min packet length': self._get_min_packet_length(),
            'max packet length': self._get_max_packet_length(),
            'packet length mean': self._get_packet_length_mean(),
            'packet length std': self._get_packet_length_std(),
            'packet length variance': self._get_packet_length_variance(),
            'syn flag count': self._get_syn_flag_count(),
            'psh flag count': self._get_psh_flag_count(),
            'urg flag count': self._get_urg_flag_count(),
            'down/up ratio': self._get_down_up_ratio(),
            'avg fwd segment size': self._get_avg_fwd_segment_size(),
            'avg bwd segment size': self._get_avg_bwd_segment_size(),
            'min_seg_size_forward': self._get_min_seg_size_forward()
        }, index=[0])


class Packet:
    def __init__(self, packet):
        new_packet = TCPPacket(
            packet) if 'tcp' in packet else UDPPacket(packet)

        self.destination_port = new_packet.destination_port
        self.push_flag = new_packet.push_flag
        self.syn_flag = new_packet.syn_flag
        self.urg_flag = new_packet.urg_flag
        self.length = new_packet.length
        self.src_ip = new_packet.src_ip
        self.dst_ip = new_packet.dst_ip
        self.segment_length = new_packet.segment_length
        self.timestamp = new_packet.timestamp


class TCPPacket:
    def __init__(self, packet):
        self.destination_port = int(packet.tcp.dstport)
        self.push_flag = int(packet.tcp.flags_push)
        self.syn_flag = int(packet.tcp.flags_syn)
        self.urg_flag = int(packet.tcp.flags_urg)
        self.length = int(packet.length)
        self.src_ip = packet.ip.src
        self.dst_ip = packet.ip.dst
        self.segment_length = int(packet.tcp.len)
        self.timestamp = packet.sniff_time.timestamp()


class UDPPacket:
    def __init__(self, packet):
        self.destination_port = int(packet.udp.dstport)
        self.push_flag = 0
        self.syn_flag = 0
        self.urg_flag = 0
        self.length = int(packet.length)
        self.src_ip = packet.ip.src
        self.dst_ip = packet.ip.dst
        self.segment_length = int(packet.udp.length)
        self.timestamp = packet.sniff_time.timestamp()


remove = [
    'average_packet_size',
    'avg_fwd_segment_size'
]
