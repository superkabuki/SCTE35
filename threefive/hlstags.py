"""
hlstags.py

"""

from .stuff import pif, ERR
from .words import (
    minusone,
    zero,
    one,
    two,
    colon,
    comma,
    equalsign,
    dblquote,
    octothorpe,
    space,
    nothing,
)

BASIC_TAGS = (
    "#EXTM3U",
    "#EXT-X-VERSION",
    "#EXT-X-ALLOW-CACHE",
)

MULTI_TAGS = (
    "#EXT-X-INDEPENDENT-SEGMENTS",
    "#EXT-X-START",
    "#EXT-X-DEFINE",
)

MEDIA_TAGS = (
    "#EXT-X-TARGETDURATION",
    "#EXT-X-MEDIA-SEQUENCE",
    "#EXT-X-DISCONTINUITY-SEQUENCE",
    "#EXT-X-PLAYLIST-TYPE",
    "#EXT-X-I-FRAMES-ONLY",
    "#EXT-X-PART-INF",
    "EXT-X-SERVER-CONTROL",
)

SEGMENT_TAGS = (
    "#EXT-X-PUBLISHED-TIME",
    "#EXT-X-PROGRAM-DATE-TIME",
)

HEADER_TAGS = BASIC_TAGS + MULTI_TAGS + MEDIA_TAGS  # + SEGMENT_TAGS


class TagParser:
    """
    TagParser parses all HLS Tags as of the latest RFC.
    Custom tags will also be parsed if possible.
    Parsed tags are stored in the Dict TagParser.tags.
    TagParser is used by the Segment class.


    Example 1:

      #EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=2030321,BANDWIDTH=2127786,
      CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=768x432,CLOSED-CAPTIONS="text"

      TagParser.tags["#EXT-X-STREAM-INF"]= { "CLOSED-CAPTIONS": "text",
                                             "RESOLUTION": "768x432",
                                             "CODECS": "avc1.4D401F,mp4a.40.2",
                                             "BANDWIDTH": 2127786,
                                             "AVERAGE-BANDWIDTH": 2030321}
    Example 2:

      #EXT-X-CUE-OUT-CONT:ElapsedTime=21.000,Duration=30,
      SCTE35=/DAnAAAAAAAAAP/wBQb+AGb/MAARAg9DVUVJAAAAAn+HCQA0AALMua1L

      TagParser.tags["#EXT-X-CUE-OUT-CONT"] = {
              "SCTE35": "/DAnAAAAAAAAAP/wBQb+AGb/MAARAg9DVUVJAAAAAn+HCQA0AALMua1L",
            "Duration": 30,
            "ElapsedTime": 21.0}
    """

    def __init__(self, lines=None):
        self.tags = {}
        for line in lines:
            self.parse_tags(line)

    @staticmethod
    def _strip_last_comma(tail):
        return tail.rstrip(",")

    def _oated(self, tag, line):
        vee = line.split(comma, one)[zero]
        self.tags[tag] = vee

    @staticmethod
    def _starts_with_octothorpe(line):
        return line[zero] == octothorpe

    @staticmethod
    def _colon_in_line(line):
        return colon in line

    def precheck(self, line):
        """
        precheck precheck that a line has tags
        """
        line = line.replace(space, nothing)
        if not line:
            return False
        if not self._starts_with_octothorpe(line):
            return False
        if not self._colon_in_line(line):
            self.tags[line] = None
            return False
        return line

    def parse_tags(self, line):
        """
        _parse_tags parses tags and
        associated attributes
        """
        line = self.precheck(line)
        if not line:
            return
        tag, tail = line.split(colon, one)
        self.tags[tag] = {}
        if tag in ["#EXT-OATCLS-SCTE35"]:
            self._oated(tag, tail)
            return
        self._split_tail(tag, tail)

    def _split_tail(self, tag, tail):
        """
        _split_tail splits key=value pairs from tail.
        """
        while tail:
            tail = self._strip_last_comma(tail)
            if equalsign not in tail:
                self.tags[tag] = pif(tail)
                return
            tail, value = self._split_value(tag, tail)
            tail = self._split_key(tail, tag, value)
        return

    def _split_key(self, tail, tag, value):
        """
        _split_key splits off the last attribute key
        """
        if tail:
            splitup = tail.rsplit(comma, one)
            if len(splitup) == two:
                tail, key = splitup
            else:
                key = splitup[zero]
                tail = None
            if equalsign in key:
                key, value = key.split(equalsign, one)
            self.tags[tag][key] = value
        return tail

    def _split_value(self, tag, tail):
        """
        _split_value does a right split
        off tail for the value in a key=value pair.
        """
        if tail[minusone:] == dblquote:
            tail, value = self._quoted(tag, tail)
        else:
            tail, value = self._unquoted(tag, tail)
        return tail, value

    def _quoted(self, tag, tail):
        """
        _quoted handles quoted attributes
        """
        value = None
        try:
            tail, value = tail[:minusone].rsplit(equalsign + dblquote, one)
        except ERR:
            self.tags[tag]
            value = tail.replace(dblquote, nothing)
            tail = None
        return tail, value

    def _unquoted(self, tag, tail):
        """
        _unquoted handles unquoted attributes
        """
        value = None
        hold = ""
        # = is only allowed as a suffix in base64
        while tail.endswith(equalsign):
            hold += tail[minusone]
            tail = tail[:minusone]
        try:
            tail, value = tail.rsplit(equalsign, one)
            value += hold
            value = pif(value)
        except ERR:
            tail = None
        return tail, value
