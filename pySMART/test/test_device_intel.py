from contextlib import nested

import mock
import pytest


@pytest.fixture
def intel_cmd_all():
    """
    smartctl -a /dev/sda
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===
Device Model:     INTEL SSDSC2BB480G4L
Serial Number:    BTWL435203C0480QGN
LU WWN Device Id: 5 5cd2e4 04b6cd88d
Firmware Version: D201LD12
User Capacity:    480,103,981,056 bytes [480 GB]
Sector Sizes:     512 bytes logical, 4096 bytes physical
Rotation Rate:    Solid State Device
Device is:        Not in smartctl database [for details use: -P showall]
ATA Version is:   ACS-2 T13/2015-D revision 3
SATA Version is:  SATA 2.6, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Mon Jul  4 10:05:25 2016 CST
SMART support is: Available - device has SMART capability.
SMART support is: Enabled
=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
General SMART Values:
Offline data collection status:  (0x02) Offline data collection activity
                                        was completed without error.
                                        Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0) The previous self-test routine completed
                                        without error or no self-test has ever
                                        been run.
Total time to complete Offline
data collection:                (    2) seconds.
Offline data collection
capabilities:                    (0x79) SMART execute Offline immediate.
                                        No Auto Offline data collection support.
                                        Suspend Offline collection upon new
                                        command.
                                        Offline surface scan supported.
                                        Self-test supported.
                                        Conveyance Self-test supported.
                                        Selective Self-test supported.
SMART capabilities:            (0x0003) Saves SMART data before entering
                                        power-saving mode.
                                        Supports SMART auto save timer.
Error logging capability:        (0x01) Error logging supported.
                                        General Purpose Logging supported.
Short self-test routine
recommended polling time:        (   1) minutes.
Extended self-test routine
recommended polling time:        (   2) minutes.
Conveyance self-test routine
recommended polling time:        (   2) minutes.
SCT capabilities:              (0x003d) SCT Status supported.
                                        SCT Error Recovery Control supported.
                                        SCT Feature Control supported.
                                        SCT Data Table supported.
SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0032   100   100   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   100   100   000    Old_age   Always       -       8713
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       104
170 Unknown_Attribute       0x0033   100   100   010    Pre-fail  Always       -       0
171 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
172 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
174 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       81
175 Program_Fail_Count_Chip 0x0033   100   100   010    Pre-fail  Always       -       163557081739
183 Runtime_Bad_Block       0x0032   100   100   000    Old_age   Always       -       0
184 End-to-End_Error        0x0033   100   100   090    Pre-fail  Always       -       0
187 Reported_Uncorrect      0x0032   100   100   000    Old_age   Always       -       0
190 Airflow_Temperature_Cel 0x0022   081   079   000    Old_age   Always       -       19 (Min/Max 16/21)
192 Power-Off_Retract_Count 0x0032   100   100   000    Old_age   Always       -       81
194 Temperature_Celsius     0x0022   100   100   000    Old_age   Always       -       30
197 Current_Pending_Sector  0x0032   100   100   000    Old_age   Always       -       0
199 UDMA_CRC_Error_Count    0x003e   100   100   000    Old_age   Always       -       0
225 Unknown_SSD_Attribute   0x0032   100   100   000    Old_age   Always       -       6255
226 Unknown_SSD_Attribute   0x0032   100   100   000    Old_age   Always       -       30
227 Unknown_SSD_Attribute   0x0032   100   100   000    Old_age   Always       -       72
228 Power-off_Retract_Count 0x0032   100   100   000    Old_age   Always       -       522094
232 Available_Reservd_Space 0x0033   100   100   010    Pre-fail  Always       -       0
233 Media_Wearout_Indicator 0x0032   100   100   000    Old_age   Always       -       0
234 Unknown_Attribute       0x0032   100   100   000    Old_age   Always       -       0
241 Total_LBAs_Written      0x0032   100   100   000    Old_age   Always       -       6255
242 Total_LBAs_Read         0x0032   100   100   000    Old_age   Always       -       15329
SMART Error Log Version: 1
No Errors Logged
SMART Self-test log structure revision number 1
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Short offline       Completed without error       00%      8706         -
# 2  Short offline       Completed without error       00%      8682         -
# 3  Short offline       Completed without error       00%      8658         -
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
Add Comment Collapse
    """
    return stdout, stderr


@pytest.fixture
def intel_scsi_cmd_all():
    """
    smartctl -d scsi -a
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

User Capacity:        480,103,981,056 bytes [480 GB]
Logical block size:   512 bytes
Rotation Rate:        Solid State Device
Form Factor:          2.5 inches
Logical Unit id:      0x55cd2e404b6cd88d
Serial number:        BTWL435203C0480QGN
Device type:          disk
Local Time is:        Fri Jul  1 10:56:20 2016 CST
SMART support is:     Available - device has SMART capability.
SMART support is:     Enabled
Temperature Warning:  Disabled or Not Supported

=== START OF READ SMART DATA SECTION ===
SMART Health Status: OK
Current Drive Temperature:     19 C

Error Counter logging not supported


[GLTSD (Global Logging Target Save Disable) set. Enable Save with '-S on']
No self-tests have been logged
    """
    return stdout, stderr


@pytest.fixture
def intel_scsi_cmd_sasphy():
    """
    smartctl -d scsi -l sasphy
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
scsiPrintSasPhy Log Sense Failed [unsupported field in scsi command]
    """
    return stdout, stderr


@pytest.fixture
def intel_scsi_cmd_sataphy():
    """
    smartctl -d scsi -l sataphy
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

SCSI device successfully opened

Use 'smartctl -a' (or '-x') to print SMART (and more) information
    """
    return stdout, stderr


@pytest.fixture
def intel_cmd_scan_open_as_root():
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
scsiPrintSasPhy Log Sense Failed [unsupported field in scsi command]

/dev/sda -d sat # /dev/sda [SAT], ATA device
/dev/sdb -d sat # /dev/sdb [SAT], ATA device
/dev/sdc -d sat # /dev/sdc [SAT], ATA device
/dev/sdd -d sat # /dev/sdd [SAT], ATA device
/dev/sde -d sat # /dev/sde [SAT], ATA device
/dev/sdf -d sat # /dev/sdf [SAT], ATA device
/dev/sdg -d sat # /dev/sdg [SAT], ATA device
/dev/sdh -d sat # /dev/sdh [SAT], ATA device
/dev/bus/0 -d sat+megaraid,8 # /dev/bus/0 [megaraid_disk_08] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,9 # /dev/bus/0 [megaraid_disk_09] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,10 # /dev/bus/0 [megaraid_disk_10] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,11 # /dev/bus/0 [megaraid_disk_11] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,12 # /dev/bus/0 [megaraid_disk_12] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,13 # /dev/bus/0 [megaraid_disk_13] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,14 # /dev/bus/0 [megaraid_disk_14] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,15 # /dev/bus/0 [megaraid_disk_15] [SAT], ATA device
    """
    return stdout, stderr

@pytest.fixture
def intel_cmd_capabilities():
    """
    smartctl -c /dev/sda
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.3.1.el7.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===
Device Model:     INTEL SSDSC2BB480G4L
Serial Number:    BTWL435203C0480QGN
LU WWN Device Id: 5 5cd2e4 04b6cd88d
Firmware Version: D201LD12
User Capacity:    480,103,981,056 bytes [480 GB]
Sector Sizes:     512 bytes logical, 4096 bytes physical
Rotation Rate:    Solid State Device
Device is:        Not in smartctl database [for details use: -P showall]
ATA Version is:   ACS-2 T13/2015-D revision 3
SATA Version is:  SATA 2.6, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Mon Jul  4 10:05:25 2016 CST
SMART support is: Available - device has SMART capability.
SMART support is: Enabled
=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
General SMART Values:
Offline data collection status:  (0x02) Offline data collection activity
                                        was completed without error.
                                        Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0) The previous self-test routine completed
                                        without error or no self-test has ever
                                        been run.
Total time to complete Offline
data collection:                (    2) seconds.
Offline data collection
capabilities:                    (0x79) SMART execute Offline immediate.
                                        No Auto Offline data collection support.
                                        Suspend Offline collection upon new
                                        command.
                                        Offline surface scan supported.
                                        Self-test supported.
                                        Conveyance Self-test supported.
                                        Selective Self-test supported.
SMART capabilities:            (0x0003) Saves SMART data before entering
                                        power-saving mode.
                                        Supports SMART auto save timer.
Error logging capability:        (0x01) Error logging supported.
                                        General Purpose Logging supported.
Short self-test routine
recommended polling time:        (   1) minutes.
Extended self-test routine
recommended polling time:        (   2) minutes.
Conveyance self-test routine
recommended polling time:        (   2) minutes.
SCT capabilities:              (0x003d) SCT Status supported.
                                        SCT Error Recovery Control supported.
                                        SCT Feature Control supported.
                                        SCT Data Table supported.
     """
    return stdout, stderr


class TestDeviceWithIntel:

    def test_device_with_intel(
        self,
        intel_cmd_all,
        intel_scsi_cmd_all,
        intel_scsi_cmd_sasphy,
        intel_scsi_cmd_sataphy,
        intel_cmd_scan_open_as_root,
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
                "_cmd_sasphy",
            ),
            mock.patch.object(
                Device,
                "_cmd_sataphy",
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
        ) as (mocked_all_with_type, mocked_sas, mocked_sata, mocked_scan, mocked_all, mocked_cap):
            mocked_all.return_value = intel_cmd_all
            mocked_all_with_type.return_value = intel_scsi_cmd_all
            mocked_sas.return_value = intel_scsi_cmd_sasphy
            mocked_sata.return_value = intel_scsi_cmd_sataphy
            mocked_scan.return_value = intel_cmd_scan_open_as_root
            mocked_cap.return_value = intel_cmd_capabilities
            device = Device("sdg")
            assert device.serial == "BTWL435203C0480QGN"
            assert device.model == "INTEL SSDSC2BB480G4L"
            assert device.capacity == "480 GB"
            assert device.firmware is None
            assert device.supports_smart is True
            assert device.messages is not None
            assert device.is_ssd is True
            assert device.assessment == "PASS"
            assert device.get_current_test_status() == (0, "The previous self-test routine completed without error or no self-test has ever been run.")
