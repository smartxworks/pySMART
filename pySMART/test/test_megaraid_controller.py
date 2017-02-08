from contextlib import nested

import mock
import pytest


@pytest.fixture
def megaraid_cmd_all():
    """
    smartctl -a -d sat+megaraid,1 /dev/bus/0
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.13.0-86-generic] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Western Digital RE4
Device Model:     WDC WD2003FYYS-18W0B0
Serial Number:    WD-WMAY03123456
LU WWN Device Id: 5 0014ee 6ac5aa123
Add. Product Id:  DELL(tm)
Firmware Version: 01.01D02
User Capacity:    2,000,398,934,016 bytes [2.00 TB]
Sector Size:      512 bytes logical/physical
Rotation Rate:    7200 rpm
Device is:        In smartctl database [for details use: -P show]
ATA Version is:   ATA8-ACS (minor revision not indicated)
SATA Version is:  SATA 2.6, 3.0 Gb/s
Local Time is:    Wed Feb  8 09:12:20 2017 UTC
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
Warning: This result is based on an Attribute check.

General SMART Values:
Offline data collection status:  (0x84)	Offline data collection activity
					was suspended by an interrupting command from host.
					Auto Offline Data Collection: Enabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
Total time to complete Offline
data collection: 		(30060) seconds.
Offline data collection
capabilities: 			 (0x7b) SMART execute Offline immediate.
					Auto Offline data collection on/off support.
					Suspend Offline collection upon new
					command.
					Offline surface scan supported.
					Self-test supported.
					Conveyance Self-test supported.
					Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 ( 306) minutes.
Conveyance self-test routine
recommended polling time: 	 (   5) minutes.
SCT capabilities: 	       (0x303f)	SCT Status supported.
					SCT Error Recovery Control supported.
					SCT Feature Control supported.
					SCT Data Table supported.

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   200   200   051    Pre-fail  Always       -       0
  3 Spin_Up_Time            0x0027   253   253   021    Pre-fail  Always       -       8191
  4 Start_Stop_Count        0x0032   100   100   000    Old_age   Always       -       20
  5 Reallocated_Sector_Ct   0x0033   200   200   140    Pre-fail  Always       -       0
  7 Seek_Error_Rate         0x002e   200   200   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   066   066   000    Old_age   Always       -       24853
 10 Spin_Retry_Count        0x0032   100   253   000    Old_age   Always       -       0
 11 Calibration_Retry_Count 0x0032   100   253   000    Old_age   Always       -       0
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       19
192 Power-Off_Retract_Count 0x0032   200   200   000    Old_age   Always       -       18
193 Load_Cycle_Count        0x0032   200   200   000    Old_age   Always       -       1
194 Temperature_Celsius     0x0022   113   108   000    Old_age   Always       -       39 (Min/Max 35/41)
196 Reallocated_Event_Count 0x0032   200   200   000    Old_age   Always       -       0
197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0030   100   253   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   200   200   000    Old_age   Always       -       0
200 Multi_Zone_Error_Rate   0x0008   200   200   000    Old_age   Offline      -       0

SMART Error Log Version: 1
No Errors Logged

SMART Self-test log structure revision number 1
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Extended offline    Completed without error       00%         8         -
# 2  Extended offline    Aborted by host               60%         3         -
# 3  Short offline       Completed without error       00%         1         -

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
def megaraid_cmd_sataphy():
    """
    smartctl -d sat+megaraid,1 -l sataphy /dev/bus/0
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.13.0-86-generic] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

SATA Phy Event Counters (GP Log 0x11)
ID      Size     Value  Description
0x0001  2            0  Command failed due to ICRC error
0x0002  2            0  R_ERR response for data FIS
0x0003  2            0  R_ERR response for device-to-host data FIS
0x0004  2            0  R_ERR response for host-to-device data FIS
0x0005  2            0  R_ERR response for non-data FIS
0x0006  2            0  R_ERR response for device-to-host non-data FIS
0x0007  2            0  R_ERR response for host-to-device non-data FIS
0x000a  2            1  Device-to-host register FISes sent due to a COMRESET
0x000b  2            0  CRC errors within host-to-device FIS
0x8000  4     22355855  Vendor specific

    """
    return stdout, stderr


@pytest.fixture
def megaraid_cmd_scan_open_as_root():
    stderr = ""
    stdout = """
# /dev/sda -d scsi # /dev/sda, SCSI device open failed: DELL or MegaRaid controller, please try adding '-d megaraid,N'
/dev/bus/0 -d sat+megaraid,0 # /dev/bus/0 [megaraid_disk_00] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,1 # /dev/bus/0 [megaraid_disk_01] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,2 # /dev/bus/0 [megaraid_disk_02] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,3 # /dev/bus/0 [megaraid_disk_03] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,4 # /dev/bus/0 [megaraid_disk_04] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,5 # /dev/bus/0 [megaraid_disk_05] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,6 # /dev/bus/0 [megaraid_disk_06] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,7 # /dev/bus/0 [megaraid_disk_07] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,8 # /dev/bus/0 [megaraid_disk_08] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,9 # /dev/bus/0 [megaraid_disk_09] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,10 # /dev/bus/0 [megaraid_disk_10] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,11 # /dev/bus/0 [megaraid_disk_11] [SAT], ATA device
    """
    return stdout, stderr


@pytest.fixture
def megaraid_cmd_capabilities():
    """
    smartctl -c -d sat+megaraid,1 /dev/bus/0
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.13.0-86-generic] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
General SMART Values:
Offline data collection status:  (0x84)	Offline data collection activity
					was suspended by an interrupting command from host.
					Auto Offline Data Collection: Enabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
Total time to complete Offline
data collection: 		(30060) seconds.
Offline data collection
capabilities: 			 (0x7b) SMART execute Offline immediate.
					Auto Offline data collection on/off support.
					Suspend Offline collection upon new
					command.
					Offline surface scan supported.
					Self-test supported.
					Conveyance Self-test supported.
					Selective Self-test supported.
SMART capabilities:            (0x0003)	Saves SMART data before entering
					power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 ( 306) minutes.
Conveyance self-test routine
recommended polling time: 	 (   5) minutes.
SCT capabilities: 	       (0x303f)	SCT Status supported.
					SCT Error Recovery Control supported.
					SCT Feature Control supported.
					SCT Data Table supported.

     """
    return stdout, stderr


class TestMegaraidController:

    def test_device_with_megaraid(
        self,
        megaraid_cmd_all,
        megaraid_cmd_sataphy,
        megaraid_cmd_scan_open_as_root,
        megaraid_cmd_capabilities
    ):
        """
        This test is to ensure that the parse can be executed without exception.
        """
        from pySMART.device import Device
        with nested(
            mock.patch.object(
                Device,
                '_cmd_all_with_type',
            ),
            mock.patch.object(
                Device,
                '_cmd_sataphy',
            ),
            mock.patch.object(
                Device,
                '_cmd_scan_open',
            ),
            mock.patch.object(
                Device,
                '_cmd_all',
            ),
            mock.patch.object(
                Device,
                '_cmd_get_capabilities',
            ),
        ) as (mocked_all_with_type, mocked_sata, mocked_scan, mocked_all, mocked_cap):
            mocked_all_with_type.return_value = megaraid_cmd_all
            mocked_all.return_value = megaraid_cmd_all
            mocked_sata.return_value = megaraid_cmd_sataphy
            mocked_scan.return_value = megaraid_cmd_scan_open_as_root
            mocked_cap.return_value = megaraid_cmd_capabilities
            device = Device('/dev/bus/0', interface='sat+megaraid,1')
            assert device.serial == 'WD-WMAY03123456'
            assert device.model == 'DELL(tm)'
            assert device.capacity == '2.00 TB'
            assert device.firmware == '01.01D02'
            assert device.supports_smart is True
            assert device.messages is not None
            assert device.is_ssd is False
            assert device.assessment == 'PASS'
            assert device.get_current_test_status() == (0, 'The previous self-test routine completed without error or no self-test has ever been run.')
