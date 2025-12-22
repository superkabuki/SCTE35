# [ threefive is the #1 SCTE35 Parser on the Planet ]  

### If you do __SCTE35__, you want to __use threefive__. 
___

### [ threefive now supports SRT](srt.md)
[<img width="1033" height="441" alt="image" src="https://github.com/user-attachments/assets/693d1d62-9304-4e32-a85e-fbafc5c2e16a" />](srt.md)
<BR>
<details><summary>Output of over four hours of threefive parsing a live SRT stream today</summary>
<pre>
a@fu:~$ threefive srt://192.168.12.247:4201
startup: ✓
ipv4int: ✓
create_socket: ✓
setsockflag: ✓
setsockflag: ✓
setsockflag: ✓
setflags: ✓
setsockflag: ✓
conlive: ✓
connect: ✓
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x6c005ea1"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 24722.499289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 19.933333,
            "segmentation_message": "Program End",
            "segmentation_type_id": 17,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210556",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 4100.909422,
        "pts": 4101.688411
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x15e1a3ba"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 24722.499289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 1200.0,
            "segmentation_message": "Program Start",
            "segmentation_type_id": 16,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 4101.009422,
        "pts": 4101.740844
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xd2124f2f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 25732.332622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 59.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 5
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 5109.509422,
        "pts": 5110.270767
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xcb5fb6f0"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 25792.365956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 59.933333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 5
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 5169.309422,
        "pts": 5170.108022
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xced0799a"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 26483.399289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.0,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 5861.409422,
        "pts": 5862.114333
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xe3d082c9"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 26693.399289,
        "break_auto_return": true,
        "break_duration": 59.966667,
        "splice_event_id": 234,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6064.909422,
        "pts": 6065.687944
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0x349866c5"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 26693.399289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.033333,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6065.309422,
        "pts": 6066.108344
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x79229335"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 26753.399289,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 236,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6130.909422,
        "pts": 6131.690756
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x3d175145"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 26753.432622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6131.009422,
        "pts": 6131.721589
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xa40a5f74"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 26753.399289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.033333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6131.309422,
        "pts": 6132.109356
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x469bc34c"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27156.965956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 209.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 3,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6535.009422,
        "pts": 6535.726011
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xd27881dd"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 27306.932622,
        "break_auto_return": true,
        "break_duration": 60.0,
        "splice_event_id": 240,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6678.909422,
        "pts": 6679.690389
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xdd90482c"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27306.932622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.066667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6679.009422,
        "pts": 6679.723333
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x6af04104"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 27366.932622,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 242,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6744.909422,
        "pts": 6745.709411
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0xd80b8d9b"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27366.965956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6745.009422,
        "pts": 6745.720611
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xf0e6c5eb"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27366.932622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 209.966667,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 3,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6745.009422,
        "pts": 6745.755778
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xdbc0ffc"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27554.132622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 239.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 4,
            "segments_expected": 2
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 6931.409422,
        "pts": 6932.141856
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x518b6fd9"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 27794.132622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 239.933333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 4,
            "segments_expected": 2
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 7171.609422,
        "pts": 7172.401344
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xabdd888f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 28192.565956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 398.433333,
            "segmentation_message": "Program End",
            "segmentation_type_id": 17,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP043112210557",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 7569.409422,
        "pts": 7570.141644
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xddc98b60"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 28192.565956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 1200.0,
            "segmentation_message": "Program Start",
            "segmentation_type_id": 16,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 7569.509422,
        "pts": 7570.270511
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xfe55919b"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 28938.565956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 59.933333,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 5
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 8316.109422,
        "pts": 8316.873767
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x1496dad0"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 28998.565956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 59.933333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 5
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 8376.909422,
        "pts": 8377.7043
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x8d35485a"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 29451.599289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.0,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 8830.909422,
        "pts": 8831.687833
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x1d21958e"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 29631.632622,
        "break_auto_return": true,
        "break_duration": 89.966667,
        "splice_event_id": 252,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9002.909422,
        "pts": 9003.6908
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xa01b251f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 29631.632622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 89.966667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9003.609422,
        "pts": 9004.399244
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x6618bc1d"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 29721.599289,
        "break_auto_return": false,
        "break_duration": 90.0,
        "splice_event_id": 254,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9098.909422,
        "pts": 9099.706911
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x581c19ec"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 29721.632622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9099.009422,
        "pts": 9099.721222
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xbdf8219a"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 29721.599289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.033333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9099.409422,
        "pts": 9100.142733
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xbd0aac46"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30078.232622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.033333,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 3,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9455.209422,
        "pts": 9455.983622
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xd79f9ecd"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 30258.265956,
        "break_auto_return": true,
        "break_duration": 89.966667,
        "splice_event_id": 2,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9628.909422,
        "pts": 9629.690911
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xda8b2d23"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30258.265956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 89.966667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9629.609422,
        "pts": 9630.337556
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x3e4d715e"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 30348.265956,
        "break_auto_return": false,
        "break_duration": 90.0,
        "splice_event_id": 4,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9724.909422,
        "pts": 9725.709411
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x6e28be1f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30348.299289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9725.009422,
        "pts": 9725.720611
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x3d79ee73"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30348.265956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.033333,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 3,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 9726.109422,
        "pts": 9726.821533
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xd281db02"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30662.832622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 269.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 4,
            "segments_expected": 2
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10039.409422,
        "pts": 10040.115611
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x74cc4e2b"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 30932.799289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 269.966667,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 4,
            "segments_expected": 2
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10310.909422,
        "pts": 10311.688044
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xa1b4885f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31316.099289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 239.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 5,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10694.909422,
        "pts": 10695.690056
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x2520386"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 31496.132622,
        "break_auto_return": true,
        "break_duration": 59.966667,
        "splice_event_id": 10,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10866.909422,
        "pts": 10867.704056
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xb9fe33a4"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31496.132622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.033333,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10867.809422,
        "pts": 10868.531822
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xf0a5b323"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 31556.099289,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 12,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10932.909422,
        "pts": 10933.688522
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0xb1e4da20"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31556.132622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10933.009422,
        "pts": 10933.739556
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x89086f2f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31556.099289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 240.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 5,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 10933.609422,
        "pts": 10934.400422
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x78a4b327"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31858.599289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 302.566667,
            "segmentation_message": "Program End",
            "segmentation_type_id": 17,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP038130830674",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 11235.509422,
        "pts": 11236.241956
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xf6cef0b9"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 31858.599289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 180.0,
            "segmentation_message": "Program Start",
            "segmentation_type_id": 16,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 11235.609422,
        "pts": 11236.406911
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x56117764"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 33200.699289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 200.0,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 10
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12578.909422,
        "pts": 12579.705944
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x5eebe9ab"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 33290.665956,
        "break_auto_return": true,
        "break_duration": 60.0,
        "splice_event_id": 18,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12659.509422,
        "pts": 12660.275644
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0x3681f3d9"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 33290.665956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.066667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12662.909422,
        "pts": 12663.6903
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xdbd5aaf2"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 33350.699289,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 20,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12728.909422,
        "pts": 12729.688233
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0xb5044450"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 33350.732622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12729.009422,
        "pts": 12729.721889
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x11ff920f"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 33400.699289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 200.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 10
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 12777.809422,
        "pts": 12778.528333
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xfd69bbb4"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 33921.132622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 210.033333,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 2,
            "segments_expected": 9
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13299.109422,
        "pts": 13299.854411
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xc57b6787"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 34041.165956,
        "break_auto_return": true,
        "break_duration": 60.0,
        "splice_event_id": 24,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13412.909422,
        "pts": 13413.6891
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0x711b4d8b"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 34041.165956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.066667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13413.209422,
        "pts": 13413.979967
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x6369dcac"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 34101.165956,
        "break_auto_return": false,
        "break_duration": 59.966667,
        "splice_event_id": 26,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13478.909422,
        "pts": 13479.701811
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x7906dbfd"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 34101.199289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13479.009422,
        "pts": 13479.723244
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x2b67f027"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 34131.165956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 210.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 2,
            "segments_expected": 9
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 13509.009422,
        "pts": 13509.739767
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x8772d62d"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 34895.065956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 210.033333,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 3,
            "segments_expected": 8
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14273.109422,
        "pts": 14273.851878
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x80e12442"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 35105.099289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 210.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 3,
            "segments_expected": 7
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14483.009422,
        "pts": 14483.720433
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x66d51d41"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 35279.865956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 199.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 5,
            "segments_expected": 6
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14657.209422,
        "pts": 14657.980144
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xb97eca45"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 35399.865956,
        "break_auto_return": true,
        "break_duration": 59.966667,
        "splice_event_id": 32,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14770.909422,
        "pts": 14771.706278
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0x2809dc8a"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 35399.865956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.033333,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14771.409422,
        "pts": 14772.140811
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xadb3b024"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 35459.832622,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 34,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14836.909422,
        "pts": 14837.6875
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x799f4699"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 35459.865956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14837.009422,
        "pts": 14837.741322
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x8204bba3"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 35479.832622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 199.966667,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 5,
            "segments_expected": 6
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 14857.609422,
        "pts": 14858.404
    }
}
^[[B{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xb8024fd8"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 37399.565956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 209.966667,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 7,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 16777.509422,
        "pts": 16778.244944
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x258338a1"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 37549.532622,
        "break_auto_return": true,
        "break_duration": 60.0,
        "splice_event_id": 38,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 16920.909422,
        "pts": 16921.7026
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0x2b39f24"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 37549.532622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.066667,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 16921.509422,
        "pts": 16922.270467
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0xc861dfb5"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 38261.932622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 210.0,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 8,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 17640.909422,
        "pts": 17641.7071
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x3b4ed318"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 38471.932622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 209.966667,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 8,
            "segments_expected": 3
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 17849.609422,
        "pts": 17850.400156
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x33dfdf69"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 38817.465956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 200.0,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 10,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18195.409422,
        "pts": 18196.137244
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x77938702"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 38937.465956,
        "break_auto_return": true,
        "break_duration": 59.966667,
        "splice_event_id": 46,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18308.909422,
        "pts": 18309.688244
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xed0c5c97"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 38937.465956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 60.033333,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18309.409422,
        "pts": 18310.110089
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0x901adcc6"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 38997.432622,
        "break_auto_return": false,
        "break_duration": 60.0,
        "splice_event_id": 48,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18350.909422,
        "pts": 18375.706222
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0xbc2597b6"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 38997.465956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18375.009422,
        "pts": 18375.721356
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x4e301f8d"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 39017.465956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 200.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 10,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18395.409422,
        "pts": 18396.114667
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x5be87abe"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 39073.365956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 55.8,
            "segmentation_message": "Program End",
            "segmentation_type_id": 17,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP026894041709",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18451.209422,
        "pts": 18451.985522
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x9d8f7713"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 39073.365956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 1200.0,
            "segmentation_message": "Program Start",
            "segmentation_type_id": 16,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 1,
            "segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 18451.409422,
        "pts": 18452.114378
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x527f8038"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 39934.299289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 59.9,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 1,
            "segments_expected": 5
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 19311.809422,
        "pts": 19312.607733
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x41517610"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 40399.699289
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.033333,
            "segmentation_message": "Break Start",
            "segmentation_type_id": 34,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 19777.509422,
        "pts": 19778.271044
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xdbbccff8"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 40579.732622,
        "break_auto_return": true,
        "break_duration": 90.0,
        "splice_event_id": 56,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 80,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "*"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 19950.909422,
        "pts": 19951.690967
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 66,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 44,
        "crc": "0xb21d3df6"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 40579.732622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 42,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 90.0,
            "segmentation_message": "Distributor Placement Opportunity Start",
            "segmentation_type_id": 54,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 1,
            "segments_expected": 1,
            "sub_segment_num": 0,
            "sub_segments_expected": 0
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 19951.809422,
        "pts": 19952.529867
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 49,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 20,
        "splice_command_type": 5,
        "descriptor_loop_length": 12,
        "crc": "0xcc7a7100"
    },
    "command": {
        "command_length": 20,
        "command_type": 5,
        "name": "Splice Insert",
        "time_specified_flag": true,
        "pts_time": 40669.732622,
        "break_auto_return": false,
        "break_duration": 89.966667,
        "splice_event_id": 58,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": false,
        "program_splice_flag": true,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 0,
        "avail_num": 0,
        "avails_expected": 0
    },
    "descriptors": [
        {
            "tag": 1,
            "identifier": "CUEI",
            "name": "DTMF Descriptor",
            "descriptor_length": 10,
            "preroll": 18,
            "dtmf_count": 4,
            "dtmf_chars": [
                "1",
                "2",
                "1",
                "#"
            ]
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 20046.909422,
        "pts": 20047.689344
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 59,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 37,
        "crc": "0x74f98fd6"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 40669.765956
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 35,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0x01",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Distributor Placement Opportunity End",
            "segmentation_type_id": 55,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 1,
            "segments_expected": 1
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 20047.009422,
        "pts": 20047.720578
    }
}
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 64,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 74825.294489,
        "cw_index": "0x00",
        "tier": "0x00",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 42,
        "crc": "0x8e7ea849"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 40669.732622
    },
    "descriptors": [
        {
            "tag": 2,
            "identifier": "CUEI",
            "name": "Segmentation Descriptor",
            "descriptor_length": 40,
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id": "0xffffffff",
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": true,
            "delivery_not_restricted_flag": true,
            "segmentation_duration": 270.0,
            "segmentation_message": "Break End",
            "segmentation_type_id": 35,
            "segmentation_upid_length": 20,
            "segmentation_upid_type": 1,
            "segmentation_upid_type_name": "Type 0x01 is deprecated, use MPU type 0x0C",
            "segmentation_upid": "msnbc_EP027437401652",
            "segment_num": 2,
            "segments_expected": 4
        }
    ],
    "packet_data": {
        "pid": 258,
        "program": 1,
        "pcr": 20047.509422,
        "pts": 20048.271511
    }
}
                                                                                    


</pre>


</details>

<BR> _checkout [SRTfu](https://github.com/superkabuki/srtfu)_

___
# [ Latest threefive version is v3.0.69 ]
* __live SRT support is now stable for decoding__.
* live SRT streaming support has been  integrated, no special handling required.
* srtfu now build libsrt automatically the first time you use it.
* __threefive functions with or without SRT support.__ 

# [ Features ]
<samp>

* __Decode SCTE-35__  MPEGTS ✔ Base64 ✔ Bytes ✔ Hex ✔ Integers ✔ JSON ✔ XML ✔ XML+Binary ✔ DASH ✔  Dicts ✔  
* __Encodes SCTE-35__ MPEGTS ✔ Base64 ✔ Bytes ✔ Hex ✔ Integers ✔ JSON ✔ XML ✔ XML+Binary ✔

* __threefive parses SCTE35 from Pipes, Files,  HTTP(s), Multicast, UDP, and now SRT__.  

* __Automatic AES decryption__ for __MPEGTS__ and __HLS__. ✔

* __Built-in Multicast Sender__ and __Receiver__. ✔

* __Injects SCTE-35 Packets__ into __MPEGTS__ video ✔.

___

#  [ Tip Of The Week ]
If you want to have a Segmentation Descriptor without a UPID <BR>
set __segmentation_upid_length__= __0__ <BR>
set __segmentation_upid_type__= __0__
___



# [ Documentation ]
	
* [__Install__](#-install-) 
* [SCTE-35 Decoding __Quick Start__ ](#-quick-start-) _threefive makes decoding SCTE-35 fast and easy_
* [SCTE-35 __Examples__](https://github.com/superkabuki/threefive/tree/main/examples) _examples of all kinds of SCTE-35 stuff_
* [SCTE-35 __Cli__](#-the-cli-tool-) _decode SCTE-35 on the command line_
* [Using the __threefive lib__](#-using-the-library-) _decode SCTE-35 with less than ten lines of code_
* [SCTE-35 __HLS__](https://github.com/superkabuki/threefive/blob/main/hls.md) _parse SCTE-35 in HLS__
* [SCTE-35 __XML__ ](https://github.com/superkabuki/SCTE-35/blob/main/xml.md) and [More __XML__](node.md) _threefive can parse and encode SCTE-35 xml_
* [__Encode__ SCTE-35](https://github.com/superkabuki/threefive/blob/main/encode.md) _threefive can encode SCTE-35 in every SCTE-35 format_
* [SCTE-35 __Sidecar Files__](https://github.com/superkabuki/SCTE-35_Sidecar_Files) _threefive supports SCTE-35 sidecar files_
* [__SuperKabuki__ SCTE-35 MPEGTS __Packet Injection__](inject.md) _inject SCTE-35 into MPEGTS streams_ 
* [threefive __Classes__](#classes) _threefive is OO, made to subclass_
	* [__Cue__ Class](https://github.com/superkabuki/threefive/blob/main/cue.md) _this class you'll use often_ 
	* [__Stream__ Class](https://github.com/superkabuki/threefive/blob/main/stream.md) _this is the class for parsing MPEGTS_
* [Use threefive to stream __Multicast__](#stream-multicast-with-the-threefive-cli-its-easy) _threefive is a multicast client and server_
* [SCTE-35 __Online Parser__](https://iodisco.com/scte35) _powered by threefive, hosted on my server_
* [SCTE-35 __As a Service__](sassy.md) _if you can make an http request, you can parse SCTE-35, no install needed._
* [Make your __threefive__ script an executable with __cython__](cython.md) _threefive is compatible with all python tools_
</samp>


##  [ Install ]
* python3 via pip
```rebol
python3 -mpip install threefive
```
* pypy3 
```rebol
pypy3 -mpip install threefive
```
* from the git repo
```rebol
git clone https://github.com/superkabuki/scte35.git
cd threefive
make install
```
___


## [ Quick Start ] 


* Most of the stuff in threefive all works the same way.

### [cli tool]

* The default action is to read a input and write a SCTE-35 output.

  *  __Inputs:__  mpegts, base64, hex, json,and xml, and xmlbin.

  *  __Outputs:__ base64, bytes, hex, int, json, xml, and xmlbin.

  *  __Sources:__ SCTE35 can read from  strings, files, stdin, http(s), multicast,srt and udp.

|Input     |Output     |Example                                                  |
|----------|-----------|---------------------------------------------------------|
|__mpegts__|__base64__ | threefive https://example.com/video.ts  __base64__      |
|          |           |                                                         |
|__base64__|__hex__    | threefive '/DAWAAAAAAAAAP/wBQb+AKmKxwAACzuu2Q==' __hex__|
|          |           |                               |                     |
|__xmlbin__|__int__    | threefive   < xmlbin.xml __int__                        |
|          |           |                                                         |
|__xml__   |__json__   | threefive   < xml.xml                                   |
|          |           |                                                         |
|__mpegts__|__xml+bin__| threefive video.ts __xmlbin__                           |
|          |   |   |                                                     |
|__json__  |__xml__    | threefive  < json.json  __xml__                         |
|          |           |                                                         |

* __Additional functionality__ in the threefive cli tool.

| description                              | threefive command                                       |
|------------------------------------------|---------------------------------------------------------|
| Parse HLS for __SCTE35__                 |threefive __hls__ https://example.com/master.m3u8        |
|                                          |                                                         |
| Inject __SCTE35__ packets                |threefive __inject__ -i in.video -s sidecar.txt -o out.ts|
|                                          |                                                         |
| Show raw __SCTE35__ packets              |threefive __packets__ udp://@235.35.3.5:3535             |
|                                          |                                                         |
| Create __SCTE35__ sidecar file           |threefive __sidecar__ video.ts                           |
|                                          |                                                         |
|Fix __SCTE-35__ data mangled by __ffmpeg__| threefive __sixfix__ video.ts                           |
|                                          |                                                         |
| Show streams in mpegts stream            | threefive __show__ https://example.com/video.ts         |
|                                          |                                                         |
| Show __iframes__ in mpegts stream        |threefive __iframes__ srt://10.10.1.3:9000               |
|                                          |                                                         |
| Show __PTS__ values from mpegts stream   | threefive __pts__ udp://192.168.1.10:9000               |
|                                          |                                                         |
|__Proxy__ the __mpegts__ stream to stdout |threefive __proxy__ https://wexample.com/video.ts        |
|                                          |                                                         |
| __Multicast__ anything                   |threefive __mcast__ some.file                            |
|                                          |                                                         |

___

##  [ Examples ]
* [__Examples__](https://github.com/superkabuki/threefive/tree/main/examples)
## [ XML ]
* [XML](https://github.com/superkabuki/SCTE-35/blob/main/xml.md) __New__! _updated 05/01/2025_
## [ Cli ]
* [SCTE-35 Cli Super Tool](#the-cli-tool) Encodes, Decodes, and Recodes. This is pretty cool, it does SCTE-35 seven different ways.
     * The cli tool comes with builtin documentation just type `threefive help`
## [ HLS ]
* [Advanced Parsing of SCTE-35 in HLS with threefive](https://github.com/superkabuki/threefive/blob/main/hls.md) All HLS SCTE-35 tags, Sidecar Files, AAC ID3 Header Timestamps, SCTE-35 filters... Who loves you baby?

##  [ MPEGTS Packet Injection ]
* [The SuperKabuki MPEGTS Packet Injection Engine in the Cli](inject.md)

##  [ SCTE-35 As a Service ]
* Decode SCTE-35 without installing anything. If you can make an https request, you can use [__Sassy__](sassy.md) to decode SCTE-35. . 

##  [ Classes ]
* The python built in help is always the most up to date docs for the library.

```py3

a@fu:~/build7/threefive$ pypy3

>>>> from threefive import Stream
>>>> help(Stream)

```

* [Class Structure](https://github.com/superkabuki/threefive/blob/main/classes.md)
* [Cue Class](https://github.com/superkabuki/threefive/blob/main/cue.md)  Cue is the main SCTE-35 class to use. 
* [Stream Class](https://github.com/superkabuki/threefive/blob/main/stream.md)  The Stream class handles MPEGTS SCTE-35 streams local, Http(s), UDP, and Multicast.

___

## [ | more  ]

* [Online SCTE-35 Parser](https://iodisco.com/scte35)  Supporte Base64, Bytes,Hex,Int, Json, Xml, and Xml+binary.

* [Encode SCTE-35](https://github.com/superkabuki/threefive/blob/main/encode.md) Some encoding code examples. 


___

* Let me show you how easy threefive is to use.

* reading SCTE-35 xml from a file
```py3
a@fu:~/threefive$ pypy3
Python 3.9.16 (7.3.11+dfsg-2+deb12u3, Dec 30 2024, 22:36:23)
[PyPy 7.3.11 with GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>> from threefive import reader
>>>> from threefive import Cue
>>>> data =reader('/home/a/xml.xml').read()
```
* load it into a threefive.Cue instance
```py3
>>>> cue = Cue(data)
```
* Show the data as JSON
```py3
>>>> cue.show()
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 92,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 0.0,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 15,
        "splice_command_type": 5,
        "descriptor_loop_length": 60,
        "crc": "0x7632935"
    },
    "command": {
        "command_length": 15,
        "command_type": 5,
        "name": "Splice Insert",
        "break_auto_return": false,
        "break_duration": 180.0,
        "splice_event_id": 1073743095,
        "splice_event_cancel_indicator": false,
        "out_of_network_indicator": true,
        "program_splice_flag": false,
        "duration_flag": true,
        "splice_immediate_flag": false,
        "event_id_compliance_flag": true,
        "unique_program_id": 1,
        "avail_num": 12,
        "avails_expected": 5
    },
    "descriptors": [
        {
            "tag": 0,
            "identifier": "CUEI",
            "name": "Avail Descriptor",
            "provider_avail_id": 12,
            "descriptor_length": 8
        },
        {
            "tag": 0,
            "identifier": "CUEI",
            "name": "Avail Descriptor",
            "provider_avail_id": 13,
            "descriptor_length": 8
        },
      

    ]
}
```
* convert the data back to xml
```py3
>>>> print(cue.xml())
<scte35:SpliceInfoSection xmlns:scte35="https://scte.org/schemas/35"  ptsAdjustment="0" protocolVersion="0" sapType="3" tier="4095">
   <scte35:SpliceInsert spliceEventId="1073743095" spliceEventCancelIndicator="false" spliceImmediateFlag="false" eventIdComplianceFlag="true" availNum="12" availsExpected="5" outOfNetworkIndicator="true" uniqueProgramId="1">
      <scte35:BreakDuration autoReturn="false" duration="16200000"/>
   </scte35:SpliceInsert>
   <scte35:AvailDescriptor providerAvailId="12"/>
   <scte35:AvailDescriptor providerAvailId="13"/>
   <scte35:AvailDescriptor providerAvailId="14"/>
   <scte35:AvailDescriptor providerAvailId="15"/>
   <scte35:AvailDescriptor providerAvailId="16"/>
   <scte35:AvailDescriptor providerAvailId="17"/>
</scte35:SpliceInfoSection>
```
* convert to xml+binary
```py3
>>>> print(cue.xmlbin())
<scte35:Signal xmlns:scte35="https://scte.org/schemas/35">
    <scte35:Binary>/DBcAAAAAAAAAP/wDwVAAAT3f69+APcxQAABDAUAPAAIQ1VFSQAAAAwACENVRUkAAAANAAhDVUVJAAAADgAIQ1VFSQAAAA8ACENVRUkAAAAQAAhDVUVJAAAAEQdjKTU=</scte35:Binary>
</scte35:Signal>
```
* convert to base64
```py3
>>>> print(cue.base64())
/DBcAAAAAAAAAP/wDwVAAAT3f69+APcxQAABDAUAPAAIQ1VFSQAAAAwACENVRUkAAAANAAhDVUVJAAAADgAIQ1VFSQAAAA8ACENVRUkAAAAQAAhDVUVJAAAAEQdjKTU=
```
* convert to hex
```py3
>>>> print(cue.hex())
0xfc305c00000000000000fff00f05400004f77faf7e00f7314000010c05003c0008435545490000000c0008435545490000000d0008435545490000000e0008435545490000000f000843554549000000100008435545490000001107632935
```
* show just the splice command
```py3
>>>> cue.command.show()
{
    "command_length": 15,
    "command_type": 5,
    "name": "Splice Insert",
    "break_auto_return": false,
    "break_duration": 180.0,
    "splice_event_id": 1073743095,
    "splice_event_cancel_indicator": false,
    "out_of_network_indicator": true,
    "program_splice_flag": false,
    "duration_flag": true,
    "splice_immediate_flag": false,
    "event_id_compliance_flag": true,
    "unique_program_id": 1,
    "avail_num": 12,
    "avails_expected": 5
}
```
* edit the break duration
```py3
>>>> cue.command.break_duration=30
>>>> cue.command.show()
{
    "command_length": 15,
    "command_type": 5,
    "name": "Splice Insert",
    "break_auto_return": false,
    "break_duration": 30,
    "splice_event_id": 1073743095,
    "splice_event_cancel_indicator": false,
    "out_of_network_indicator": true,
    "program_splice_flag": false,
    "duration_flag": true,
    "splice_immediate_flag": false,
    "event_id_compliance_flag": true,
    "unique_program_id": 1,
    "avail_num": 12,
    "avails_expected": 5
}
```

* re-encode to base64 with the new duration
```py3
>>>> cue.base64()
'/DBcAAAAAAAAAP/wDwVAAAT3f69+ACky4AABDAUAPAAIQ1VFSQAAAAwACENVRUkAAAANAAhDVUVJAAAADgAIQ1VFSQAAAA8ACENVRUkAAAAQAAhDVUVJAAAAEe1FB6g='
```
* re-encode to xml with the new duration
```py3
>>>> print(cue.xml())
<scte35:SpliceInfoSection xmlns:scte35="https://scte.org/schemas/35"  ptsAdjustment="0" protocolVersion="0" sapType="3" tier="4095">
   <scte35:SpliceInsert spliceEventId="1073743095" spliceEventCancelIndicator="false" spliceImmediateFlag="false" eventIdComplianceFlag="true" availNum="12" availsExpected="5" outOfNetworkIndicator="true" uniqueProgramId="1">
      <scte35:BreakDuration autoReturn="false" duration="2700000"/>
   </scte35:SpliceInsert>
   <scte35:AvailDescriptor providerAvailId="12"/>
   <scte35:AvailDescriptor providerAvailId="13"/>
   <scte35:AvailDescriptor providerAvailId="14"/>
   <scte35:AvailDescriptor providerAvailId="15"/>
   <scte35:AvailDescriptor providerAvailId="16"/>
   <scte35:AvailDescriptor providerAvailId="17"/>
</scte35:SpliceInfoSection>
```
* show just the descriptors
```py3
>>>> _ = [d.show() for d in cue.descriptors]
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 12,
    "descriptor_length": 8
}
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 13,
    "descriptor_length": 8
}
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 14,
    "descriptor_length": 8
}
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 15,
    "descriptor_length": 8
}
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 16,
    "descriptor_length": 8
}
{
    "tag": 0,
    "identifier": "CUEI",
    "name": "Avail Descriptor",
    "provider_avail_id": 17,
    "descriptor_length": 8
}
```
* pop off the last descriptor and re-encode to xml
```py3

>>>> cue.descriptors.pop()
{'tag': 0, 'identifier': 'CUEI', 'name': 'Avail Descriptor', 'private_data': None, 'provider_avail_id': 17, 'descriptor_length': 8}
>>>> print(cue.xml())
<scte35:SpliceInfoSection xmlns:scte35="https://scte.org/schemas/35"  ptsAdjustment="0" protocolVersion="0" sapType="3" tier="4095">
   <scte35:SpliceInsert spliceEventId="1073743095" spliceEventCancelIndicator="false" spliceImmediateFlag="false" eventIdComplianceFlag="true" availNum="12" availsExpected="5" outOfNetworkIndicator="true" uniqueProgramId="1">
      <scte35:BreakDuration autoReturn="false" duration="2700000"/>
   </scte35:SpliceInsert>
   <scte35:AvailDescriptor providerAvailId="12"/>
   <scte35:AvailDescriptor providerAvailId="13"/>
   <scte35:AvailDescriptor providerAvailId="14"/>
   <scte35:AvailDescriptor providerAvailId="15"/>
   <scte35:AvailDescriptor providerAvailId="16"/>
</scte35:SpliceInfoSection>
```


## [ The Cli tool ]

#### The cli tool installs automatically with pip or the Makefile.

* [__SCTE-35 Inputs__](#inputs)
* [__SCTE-35 Outputs__](#outputs)
* [Parse __MPEGTS__ streams for __SCTE-35__](#streams)
* [Parse __SCTE-35__ in __hls__](#hls)
* [Display __MPEGTS__ __iframes__](#iframes)
* [Display raw __SCTE-35 packets__ from __video streams__](#packets)
* [__Repair SCTE-35 streams__ changed to __bin data__ by __ffmpeg__](#sixfix)

#### `Inputs`

* Most __inputs__ are __auto-detected.__ 
* __stdin__ is __auto selected__ and __auto detected.__
* __SCTE-35 data is printed to stderr__
* __stdout is used when piping video__
* mpegts can be specified by file name or URI.
```rebol
threefive udp://@235.2.5.35:3535
```
* If a file comtains a SCTE-35 cue as a string( base64,hex,int,json,or xml+bin), redirect the file contents.
```rebol

  threefive < json.json  

 ```

* quoted strings(( base64,hex,int,json or xml+bin), can be passed directly on the command line as well.

```awk

threefive '/DAWAAAAAAAAAP/wBQb+ztd7owAAdIbbmw=='

```


| Input Type |     Cli Example                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------|
| __Base64__     |  `threefive '/DAsAAAAAyiYAP/wCgUAAAABf1+ZmQEBABECD0NVRUkAAAAAf4ABADUAAC2XQZU='`
| __Hex__        |`threefive 0xfc301600000000000000fff00506fed605225b0000b0b65f3b`|
| __HLS__         |`threefive hls https://example.com/master.m3u8`                                                             |
| __JSON__        |`threefive < json.json`  |
| __Xmlbin__      | `js threefive < xmlbin.xml`                                                                                 |

# `Streams`

|Protocol       |  Cli Example                                                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|  __File__         |   `threefive video.ts`                                                                                                                            |
|  __Http(s)__      |   `threefive https://example.com/video.ts`                                                                                                        |
|  __Stdin__        |  `threefive < video.ts`            |
|  __UDP Multicast__|  `threefive udp://@235.35.3.5:9999`                                                                          |
|  __UDP Unicast__  |                                                                      `threefive udp://10.0.0.7:5555`                                              |
|  __HLS__          |                                                                                                    `threefive hls https://example.com/master.m3u8`|
|               |                                                                                                                                                    |


#### Outputs
* output type is determined by the key words __base64, bytes, hex, int, json, and xmlbin__.
* __json is the default__.
* __Any input (except HLS,) can be returned as any output__
  * examples __Base64 to Hex__ etc...) 


| Output Type | Cli Example         |
|-------------|----------------------------------------------------------|
|__Base 64__     |                                                                                                                                                                    `threefive 0xfc301600000000000000fff00506fed605225b0000b0b65f3b  base64  `                                                                                                                                                                                                                                                                                                                                         |
| __Bytes__       |                                                                                 `threefive 0xfc301600000000000000fff00506fed605225b0000b0b65f3b  bytes`                                                                                                                                                                                                                                                                                                                                                                                                                               |
| __Hex__         | `threefive '/DAsAAAAAyiYAP/wCgUAAAABf1+ZmQEBABECD0NVRUkAAAAAf4ABADUAAC2XQZU='  hex`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| __Integer__     |                                                                                                                                                                                                                                                       `threefive '/DAsAAAAAyiYAP/wCgUAAAABf1+ZmQEBABECD0NVRUkAAAAAf4ABADUAAC2XQZU='  int`   |
| __JSON__        |                                                                                                                                                                                                                                                                                                              `threefive 0xfc301600000000000000fff00506fed605225b0000b0b65f3b json ` |
| __Xml+bin__     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        `threefive 0xfc301600000000000000fff00506fed605225b0000b0b65f3b xmlbin   `      |`

#### `hls`
* parse hls manifests and segments for SCTE-35
```smalltalk
threefive hls https://example.com/master.m3u8
```
___
#### `Iframes`
* Show iframes PTS in an MPEGTS video

```smalltalk
threefive iframes https://example.com/video.ts
```
___

#### `packets`   
* Print raw SCTE-35 packets from multicast mpegts video

```smalltalk
threefive packets udp://@235.35.3.5:3535
```
___
#### `proxy`   
* Parse a https stream and write raw video to stdout

```smalltalk
threefive proxy video.ts
```
___
#### `pts`    
* Print PTS from mpegts video

```smalltalk
threefive pts video.ts
```
___
#### `sidecar`  
* Parse a stream, write pts,write SCTE-35 Cues to sidecar.txt

```smalltalk
threefive sidecar video.ts
```
___
#### `sixfix`  
* Fix SCTE-35 data mangled by ffmpeg

```smalltalk
threefive sixfix video.ts
```
___
#### `show`  

* Probe mpegts video _( kind of like ffprobe )_

```smalltalk
 threefive show video.ts
```
___
#### `version`     
* Show version

```smalltalk
 threefive version
```
___
#### `help`        
* Help
```rebol
 threefive help
```
___


## [ Stream Multicast with the threefive cli, it's easy. ]

* The threefive cli has long been a Multicast Receiver( client )
* The cli now comes with a builtin Multicast Sender( server).
 * __Start the Receiver first__
* It's optimized for MPEGTS (1316 byte Datagrams) but you can send any video or file.
* The defaults will work in most situations, you don't even have to set the address.
* threefive cli also supports UDP Unicast Streaming.
  
![image](https://github.com/user-attachments/assets/6042b8e0-5d6b-4de0-b6b0-9556cecc184f)
 
```js
a@fu:~$ threefive mcast help
usage: threefive mcast [-h] [-i INPUT] [-a ADDR] [-b BIND_ADDR] [-t TTL]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        like "/home/a/vid.ts" or "udp://@235.35.3.5:3535" or
                        "https://futzu.com/xaa.ts"
                        [default:sys.stdin.buffer]
  -a ADDR, --addr ADDR  Destination IP:Port [default:235.35.3.5:3535]
  -b BIND_ADDR, --bind_addr BIND_ADDR
                        Local IP to bind [default:0.0.0.0]
  -t TTL, --ttl TTL     Multicast TTL (1 - 255) [default:32]
a@fu:~$ 
```

## [iodisco.com/scte35](https://iodisco.com/scte35)





 <svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg> 

 <img width="258" height="256" alt="image" src="https://github.com/user-attachments/assets/642cb803-9465-408e-bb6e-03549eb22d78" />

___
 [__Install__](#install) |[__SCTE-35 Cli__](#the-cli-tool) | [__SCTE-35 HLS__](https://github.com/superkabuki/threefive/blob/main/hls.md) | [__Cue__ Class](https://github.com/superkabuki/threefive/blob/main/cue.md) | [__Stream__ Class](https://github.com/superkabuki/threefive/blob/main/stream.md) | [__Online SCTE-35 Parser__](https://iodisco.com/scte35) | [__Encode SCTE-35__](https://github.com/superkabuki/threefive/blob/main/encode.md) | [__SCTE-35 Examples__](https://github.com/superkabuki/threefive/tree/main/examples)
 | [__SCTE-35 XML__ ](https://github.com/superkabuki/SCTE-35/blob/main/xml.md) and [More __XML__](node.md) | [__threefive runs Four Times Faster on pypy3__](https://pypy.org/) | [__SuperKabuki SCTE-35 MPEGTS Packet Injection__](inject.md)


 <details><summary>

### mpegts 

 </summary>
 
* MPEGTS streams can be  Files, Http(s), Multicast, UDP Unicast, or  stdin. 

* __cli__
```js
threefive https://example.com/video.ts
```
* wildcards work too.
```js
threefive /mpegts/*.ts
```

* __lib__
```py3

from threefive import Stream
stream = Stream('https://example.com/video.ts')
stream.decode()

```

</details>



<details><summary>

### Base64

</summary>

* __cli__
```js
threefive '/DAsAAAAAyiYAP/wCgUAAAABf1+ZmQEBABECD0NVRUkAAAAAf4ABADUAAC2XQZU='
```
* __lib__
```py3

from threefive import Cue
data = '/DAsAAAAAyiYAP/wCgUAAAABf1+ZmQEBABECD0NVRUkAAAAAf4ABADUAAC2XQZU='
cue=Cue(data)
cue.show()
```

</details>


<details><summary>

### Bytes

</summary>

* __cli__
	* Bytes don't work on the cli

* __lib__
```py3

from threefive import Cue
data =  b'\xfc0\x16\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x05\x06\xfe\x00\xc0D\xa0\x00\x00\x00\xb5k\x88'
cue=Cue(data)
cue.show()
```

</details>


<details><summary>
	
### Hex

</summary>

* Can be a hex literal or hex string or bytes.

* __cli__
```js
threefive  0xfc301600000000000000fff00506fed605225b0000b0b65f3b
```
* __lib__
```py3

from threefive import Cue
data =  0xfc301600000000000000fff00506fed605225b0000b0b65f3b
cue=Cue(data)
cue.show()
```

</details>


<details><summary>
	
### Int

</summary>

* Can be a literal integer or string or bytes.

* __cli__
```js
threefive  1583008701074197245727019716796221243043855984942057168199483
```
* __lib__
```py3

from threefive import Cue
data =  1583008701074197245727019716796221243043855984942057168199483
cue=Cue(data)
cue.show()
```


</details>


<details><summary>
	
### JSON

</summary>

* __cli__
	* 	put JSON SCTE-35 in a file and redirect it into threefive 
```js
threefive  < json.json
```
* __lib__

```py3

 from threefive import Cue
 data = '''{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 22,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 0.0,
        "cw_index": "0x00",
        "tier": "0x0fff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 0,
        "crc": "0xb56b88"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 140.005333
    },
    "descriptors": []
}
'''
cue=Cue(data)
cue.show()
```

</details>


<details><summary><u>

### Xml

</u>
</summary>

* __cli__
	* put xml SCTE-35 in a [file](xml.xml) and redirect it into threefive 
	```js
	threefive < xml.xml
	```
* __lib__
```py3
from threefive import Cue
data =  '''
<scte35:SpliceInfoSection xmlns:scte35="https://scte.org/schemas/35" 
        ptsAdjustment="0" protocolVersion="0" sapType="3" tier="4095">
   <scte35:TimeSignal>
      <scte35:SpliceTime ptsTime="12600480"/>
   </scte35:TimeSignal>
</scte35:SpliceInfoSection>
'''
cue=Cue(data)

cue.show()
```


</details>



<details><summary>
	
### Xml+binary

</summary>

* __cli__
	* write xml+binary to a [file](xmlbin.xml) and redirect it to threefive
```js
threefive < xmlbin.xml
```
* __lib__
```py3

from threefive import Cue
data = '''<scte35:Signal xmlns:scte35="https://scte.org/schemas/35">
    <scte35:Binary>/DAWAAAAAAAAAP/wBQb+AMBEoAAAALVriA==</scte35:Binary>
</scte35:Signal>
'''
cue=Cue(data)
cue.show()
```

</details>

</samp>

