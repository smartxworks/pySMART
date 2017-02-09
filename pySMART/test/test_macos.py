from contextlib import nested

import mock
import pytest


@pytest.fixture
def macos_cmd_all():
    """
    smartctl -a /dev/disk1
    """
    stderr = ""
    stdout = """
smartctl 6.5 2016-05-07 r4318 [Darwin 16.4.0 x86_64] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Apple SD/SM/TS...E/F SSDs
Device Model:     APPLE SSD SM0512G
Serial Number:    S29ANYAG123456
LU WWN Device Id: 5 001234 900000000
Firmware Version: BXW1SA0Q
User Capacity:    500,277,790,720 bytes [500 GB]
Sector Sizes:     512 bytes logical, 4096 bytes physical
Rotation Rate:    Solid State Device
Device is:        In smartctl database [for details use: -P show]
ATA Version is:   ATA8-ACS T13/1699-D revision 4c
SATA Version is:  SATA 3.0, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Tue Feb  7 14:10:04 2017 CET
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
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
recommended polling time: 	 (  10) minutes.

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x001a   200   200   000    Old_age   Always       -       0
  5 Reallocated_Sector_Ct   0x0033   100   100   000    Pre-fail  Always       -       0
  9 Power_On_Hours          0x0032   099   099   000    Old_age   Always       -       3818
 12 Power_Cycle_Count       0x0032   089   089   000    Old_age   Always       -       10461
169 Unknown_Attribute       0x0013   212   212   010    Pre-fail  Always       -       4527071692672
173 Wear_Leveling_Count     0x0032   195   195   100    Old_age   Always       -       8599765028
174 Host_Reads_MiB          0x0022   099   099   000    Old_age   Always       -       12752293
175 Host_Writes_MiB         0x0022   099   099   000    Old_age   Always       -       11997087
192 Power-Off_Retract_Count 0x0012   099   099   000    Old_age   Always       -       47
194 Temperature_Celsius     0x0022   070   017   000    Old_age   Always       -       30 (Min/Max 13/84)
197 Current_Pending_Sector  0x0022   100   100   000    Old_age   Always       -       0
199 UDMA_CRC_Error_Count    0x001a   200   199   000    Old_age   Always       -       0

SMART Error Log Version: 1
No Errors Logged

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]

Warning! SMART Selective Self-Test Log Structure error: invalid SMART checksum.
SMART Selective self-test log data structure revision number 1
 SPAN  MIN_LBA  MAX_LBA  CURRENT_TEST_STATUS
    1        0        0  Not_testing
    2        0        0  Not_testing
    3        0        0  Not_testing
    4        0        0  Not_testing
    5        0        0  Not_testing
  255        0    65535  Read_scanning was never started
Selective self-test flags (0x0):
  After scanning selected spans, do NOT read-scan remainder of disk.
If Selective self-test is pending on power-up, resume after 0 minute delay.

    """
    return stdout, stderr


@pytest.fixture
def macos_cmd_scan_open_as_root():
    stderr = ""
    stdout = """
IOService:/AppleACPIPlatformExpert/PCI0@0/AppleACPIPCI/RP06@1C,5/IOPP/SSD0@0/AppleAHCI/PRT0@0/IOAHCIDevice@0/AppleAHCIDiskDriver/IOAHCIBlockStorageDevice -d ata # IOService:/AppleACPIPlatformExpert/PCI0@0/AppleACPIPCI/RP06@1C,5/IOPP/SSD0@0/AppleAHCI/PRT0@0/IOAHCIDevice@0/AppleAHCIDiskDriver/IOAHCIBlockStorageDevice, ATA device
    """
    return stdout, stderr


@pytest.fixture
def macos_cmd_capabilities():
    """
    smartctl -c /dev/disk1
    """
    stderr = ""
    stdout = """
smartctl 6.5 2016-05-07 r4318 [Darwin 16.4.0 x86_64] (local build)
Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
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
recommended polling time: 	 (  10) minutes.

     """
    return stdout, stderr


class TestDeviceOnMacOs:

    def test_macos(
        self,
        macos_cmd_all,
        macos_cmd_scan_open_as_root,
        macos_cmd_capabilities,
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
            mocked_all_with_type.return_value = macos_cmd_all
            mocked_scan.return_value = macos_cmd_scan_open_as_root
            mocked_all.return_value = macos_cmd_all
            mocked_cap.return_value = macos_cmd_capabilities
            device = Device("IOService:/AppleACPIPlatformExpert/PCI0@0/AppleACPIPCI/RP06@1C,5/IOPP/SSD0@0/AppleAHCI/PRT0@0/IOAHCIDevice@0/AppleAHCIDiskDriver/IOAHCIBlockStorageDevice", interface='ata')

            assert device.serial == "S29ANYAG123456"
            assert device.model == "APPLE SSD SM0512G"
            assert device.capacity == "500 GB"
            assert device.firmware == "BXW1SA0Q"
            assert device.supports_smart is True
            assert device.messages is not None
            assert device.is_ssd is True
            assert device.assessment == "PASS"
            assert device.get_current_test_status() == (0, "The previous self-test routine completed without error or no self-test has ever been run.")
