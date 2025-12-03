#!/usr/bin/env python3

import sys
import time
from srtfu import datagramer
# from .stream import Stream


PACKETSIZE = 188
SYNC_BYTE = b"G"
SPIN = True


def has_sync_byte(stuff):
    """
    has_sync_byte check stuff for sync_byte
    """
    return stuff[0:1] == SYNC_BYTE


def at_least_a_packet(stuff):
    """
    at_least_a_packet  check if stuff  is at least PACKETSIZE
    """
    return len(stuff) >= PACKETSIZE


def calculate_sidecar_pts(scte35):
    """
    calculate_sidecar_pts determine pts
    for the sidecar file entry.
    """
    rollover = 95443.717678
    pts = 0.001
    if scte35.packet_data.pts:
        pts = scte35.packet_data.pts
    if scte35.command.pts_time:
        pts = (scte35.command.pts_time + scte35.info_section.pts_adjustment) % rollover
    return pts


def add_scte35_to_sidecar(scte35):
    """
    add_scte35_to_sidecar
    generates a sidecar file with the
    SCTE-35 Cues
    """
    scte35.show()
    pts = calculate_sidecar_pts(scte35)
    data = f"{pts},{scte35.encode()}\n"
    with open("sidecar.txt", "a") as sidecar:
        sidecar.write(data)


def check_for_scte35(packet,strm):
    """
    check a packet for scte35 
    """
    scte35 = strm._parse(packet)
    if scte35:
        add_scte35_to_sidecar(scte35)


def parse_packet(packet, strm):
    """
    parse_packet check mpegts packet for scte35
    """
    if at_least_a_packet(packet):
        if has_sync_byte(packet):
            check_for_scte35(packet,strm)


def packetize(datagram):
    """
    packetize split datagram into mpegts packets
    """
    return [datagram[i : i + PACKETSIZE] for i in range(0, len(datagram), PACKETSIZE)]


def parse_datagram(datagram, strm):
    """
    parse_datagram test datagram and parse.
    """
    _ = [parse_packet(packet, strm) for packet in packetize(datagram)]


def spinner(lc):
    """
    spinner show me things are working,
    it only spins when it's parsing data.
    """
    spins = ["|", "\\", "-", "/"]
    if SPIN:
        lc %= len(spins)
        print(spins[lc], file=sys.stderr, end="\r")
        lc += 1
    return lc

def srt_parse(srt_url, strm):
    lc=0
    for datagram in datagramer(srt_url):
        lc = spinner(lc)
        parse_datagram(datagram, strm)    


if __name__ == "__main__":
    lc = 0
#    strm = Stream(tsdata=None)
    for datagram in datagramer(sys.argv[1]):
        lc = spinner(lc)
        parse_datagram(datagram, strm)
