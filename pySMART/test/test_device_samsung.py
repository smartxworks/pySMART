from contextlib import nested

import mock
import pytest


@pytest.fixture
def samsung_cmd_all():
    """
    smartctl -a /dev/sda
    """
    stderr = ""
    stdout = """
smartctl 6.5 2016-01-24 r4214 [x86_64-linux-4.8.0-25-generic] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Device Model:     SAMSUNG SSD PM851 2.5 7mm 512GB
Serial Number:    S1CVNSAF500333
LU WWN Device Id: 5 002538 844584d30
Firmware Version: EXT06D0Q
User Capacity:    512,110,190,592 bytes [512 GB]
Sector Size:      512 bytes logical/physical
Rotation Rate:    Solid State Device
Device is:        Not in smartctl database [for details use: -P showall]
ATA Version is:   ACS-2, ATA8-ACS T13/1699-D revision 4c
SATA Version is:  SATA 3.1, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Wed Nov 30 07:50:00 2016 CET
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
See vendor-specific Attribute list for marginal Attributes.

General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      ( 249)	Self-test routine in progress...
					90% of test remaining.
Total time to complete Offline
data collection: 		(    0) seconds.
Offline data collection
capabilities: 			 (0x53) SMART execute Offline immediate.
					Auto Offline data collection on/off support.
					Suspend Offline collection upon new
					command.
					No Offline surface scan supported.
					Self-test supported.
					No Conveyance Self-test supported.
					Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 ( 110) minutes.
SCT capabilities: 	       (0x003d)	SCT Status supported.
					SCT Error Recovery Control supported.
					SCT Feature Control supported.
					SCT Data Table supported.

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0033   100   100   010    Pre-fail  Always       -       0
 12 Power_Cycle_Count       0x0032   099   099   000    Old_age   Always       -       79
175 Program_Fail_Count_Chip 0x0032   100   100   010    Old_age   Always       -       0
176 Erase_Fail_Count_Chip   0x0032   100   100   010    Old_age   Always       -       0
177 Wear_Leveling_Count     0x0013   094   094   005    Pre-fail  Always       -       61
178 Used_Rsvd_Blk_Cnt_Chip  0x0013   100   100   010    Pre-fail  Always       -       0
179 Used_Rsvd_Blk_Cnt_Tot   0x0013   100   100   010    Pre-fail  Always       -       0
180 Unused_Rsvd_Blk_Cnt_Tot 0x0013   100   001   010    Pre-fail  Always   In_the_past 8815
181 Program_Fail_Cnt_Total  0x0032   100   100   010    Old_age   Always       -       0
182 Erase_Fail_Count_Total  0x0032   100   100   010    Old_age   Always       -       0
187 Reported_Uncorrect      0x0032   100   100   000    Old_age   Always       -       0
195 Hardware_ECC_Recovered  0x001a   200   200   000    Old_age   Always       -       0
241 Total_LBAs_Written      0x0032   099   099   000    Old_age   Always       -       17859168296
242 Total_LBAs_Read         0x0032   099   099   000    Old_age   Always       -       3944005202

SMART Error Log Version: 1
No Errors Logged

SMART Self-test log structure revision number 1
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Short offline       Completed without error       00%       283         -
# 2  Short offline       Completed without error       00%       188         -
# 3  Short offline       Completed without error       00%       186         -
# 4  Short offline       Completed without error       00%       186         -
# 5  Extended offline    Completed without error       00%         6         -
# 6  Extended offline    Interrupted (host reset)      00%      2783         -
# 7  Short offline       Completed without error       00%         0         -

SMART Selective self-test log data structure revision number 1
 SPAN  MIN_LBA  MAX_LBA  CURRENT_TEST_STATUS
    1        0        0  Not_testing
    2        0        0  Not_testing
    3        0        0  Not_testing
    4        0        0  Not_testing
    5        0        0  Not_testing
Selective self-test flags (0x0):
  After scanning selected spans, do NOT read-scan remainder of disk.
If Selective self-test is pending on power-up, resume after 0 minute delay.

    """
    return stdout, stderr


@pytest.fixture
def samsung_cmd_scan_open_as_root():
    stderr = ""
    stdout = """
/dev/sda -d sat # /dev/sda [SAT], ATA device
/dev/sdb -d sat # /dev/sdb [SAT], ATA device
    """
    return stdout, stderr


@pytest.fixture
def intel_cmd_capabilities():
    """
    smartctl -c /dev/sda
    """
    stderr = ""
    stdout = """

smartctl 6.5 2016-01-24 r4214 [x86_64-linux-4.8.0-25-generic] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      ( 249)	Self-test routine in progress...
					90% of test remaining.
Total time to complete Offline
data collection: 		(    0) seconds.
Offline data collection
capabilities: 			 (0x53) SMART execute Offline immediate.
					Auto Offline data collection on/off support.
					Suspend Offline collection upon new
					command.
					No Offline surface scan supported.
					Self-test supported.
					No Conveyance Self-test supported.
					Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 ( 110) minutes.
SCT capabilities: 	       (0x003d)	SCT Status supported.
					SCT Error Recovery Control supported.
					SCT Feature Control supported.
					SCT Data Table supported.
     """
    return stdout, stderr


class TestDeviceWithSamsung:

    def test_device_with_samsung(
        self,
        samsung_cmd_all,
        samsung_cmd_scan_open_as_root,
        intel_cmd_capabilities
    ):
        """
        This test is to ensure that the parse can be executed without exception.
        """
        from pySMART.device import Device
        with nested(
            mock.patch.object(
                Device,
                "_cmd_all_with_type",
            ),
            mock.patch.object(
                Device,
                "_cmd_scan_open",
            ),
            mock.patch.object(
                Device,
                "_cmd_all",
            ),
            mock.patch.object(
                Device,
                "_cmd_get_capabilities",
            ),
        ) as (mocked_all_with_type, mocked_scan, mocked_all, mocked_cap):
            mocked_all_with_type.return_value = samsung_cmd_all
            mocked_scan.return_value = samsung_cmd_scan_open_as_root
            mocked_all.return_value = samsung_cmd_all
            mocked_cap.return_value = intel_cmd_capabilities
            device = Device("/dev/sda")
            assert device.serial == "S1CVNSAF500333"
            assert device.model == "SAMSUNG SSD PM851 2.5 7mm 512GB"
            assert device.capacity == "512 GB"
            assert device.firmware == "EXT06D0Q"
            assert device.supports_smart is True
            assert device.messages is not None
            assert device.is_ssd is True
            assert device.assessment == "WARN"
            assert device.get_current_test_status() == (15, "Self-test routine in progress... 90% of test remaining.")
