"""
Example from the specification

14.2. Splice_Insert

"""

import threefive


HEX = "0xFC302F000000000000FFFFF014054800008F7FEFFE7369C02EFE0052CCF500000000000A0008435545490000013562DBA30A"
B64 = "/DAvAAAAAAAA///wFAVIAACPf+/+c2nALv4AUsz1AAAAAAAKAAhDVUVJAAABNWLbowo="

# Using Hex

hex2cue = threefive.Cue(HEX)


# Using Base64
# (output should be the same as above)

base642cue=threefive.Cue(B64)

threefive.blue("Cue from Hex")
hex2cue.show()

threefive.blue("Cue from Base64")
base642cue.show()
