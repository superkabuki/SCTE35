"""
srtscte35.py
helper functions for parsing srt streams
used by threefive.Stream class
"""

import sys
import time

try:
    from srtfu import datagramer
except:
    print("srtfu is not available")

PKTSZ = 188
ROLLOVER = 95443.717678
SIDECAR = "sidecar.txt"
SPIN = True
SYNC_BYTE = b"G"
ZERO = b"\x00"


def has_sync_byte(stuff):
    """
    has_sync_byte check stuff for sync_byte
    """
    return stuff[0:1] == SYNC_BYTE


def at_least_a_packet(stuff):
    """
    at_least_a_packet  check if stuff  is at least PACKETSIZE
    """
    return len(stuff) >= PKTSZ


def calculate_sidecar_pts(scte35):
    """
    calculate_sidecar_pts determine pts
    for the sidecar file entry.
    """
    pts = 0.001  # 0.0 may cause a problem.
    if scte35.packet_data.pts:
        pts = scte35.packet_data.pts
    if scte35.command.pts_time:
        pts = (scte35.command.pts_time + scte35.info_section.pts_adjustment) % ROLLOVER
    return pts


def add_scte35_to_sidecar(scte35):
    """
    add_scte35_to_sidecar
    generates a sidecar file with the
    SCTE-35 Cues
    """
    pts = calculate_sidecar_pts(scte35)
    data = f"{pts},{scte35.encode()}\n"
    with open(SIDECAR, "a") as sidecar:
        sidecar.write(data)


def check_for_scte35(packet, strm):
    """
    check a packet for scte35
    """
    scte35 = strm._parse(packet)
    if scte35:
        scte35.show()
        add_scte35_to_sidecar(scte35)


def parse_packet(packet, strm):
    """
    parse_packet check mpegts packet for scte35
    """
    if verify_packet(packet):
        check_for_scte35(packet, strm)


def verify_packet(packet):
    if at_least_a_packet(packet):
        if has_sync_byte(packet):
            return True
    return False


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


def big_fat(bigfatbuff, strm):
    """
    big_fat  trims bigfatbuff to start on a sync byte,
    and slices off a packet to be parsed.

    """
    bigfatbuff = bigfatbuff[bigfatbuff.index(SYNC_BYTE) :]
    packet, bigfatbuff = bigfatbuff[:PKTSZ], bigfatbuff[PKTSZ:]
    parse_packet(packet, strm)
    return bigfatbuff, strm


def parse_datagram(datagram, bigfatbuff,strm):
    """
    parse datagram parse datagram into bigfatbuff
    """
    bigfatbuff += datagram.rstrip(ZERO)
    while SYNC_BYTE in bigfatbuff:
        bigfatbuff, strm = big_fat(bigfatbuff, strm)
    return bigfatbuff,strm    


def srt_parse2(srt_url, strm):
    """
    srt_parse parse srt stream for SCTE35
    strm is a Stream instance
    srt_url  like srt://1.2.3.4:9000
    """
    lc = 0
    bigfatbuff = b""
    for datagram in datagramer(srt_url):
        lc = spinner(lc)
        bigfatbuff,strm= parse_datagram(datagram, bigfatbuff,strm)

