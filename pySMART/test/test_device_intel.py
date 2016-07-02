from contextlib import nested

import mock
import pytest


@pytest.fixture
def intel_scsi_cmd_scsi_all():
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


class TestDeviceWithSeagate:

    def test_device_with_seagate(
        self,
        intel_scsi_cmd_scsi_all,
        intel_scsi_cmd_sasphy,
        intel_scsi_cmd_sataphy,
        intel_cmd_scan_open_as_root,
    ):
        """
        This test is to ensure that the parse can be executed without exception.
        """
        from pySMART.device import Device
        with nested(
            mock.patch.object(
                Device,
                "_cmd_all_attr",
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
        ) as (mocked_all, mocked_sas, mocked_sata, mocked_scan):
            mocked_all.return_value = intel_scsi_cmd_scsi_all
            mocked_sas.return_value = intel_scsi_cmd_sasphy
            mocked_sata.return_value = intel_scsi_cmd_sataphy
            mocked_scan.return_value = intel_cmd_scan_open_as_root
            device = Device("sdg")
            assert device.serial == "BTWL435203C0480QGN"
            assert device.model is None
            assert device.capacity == "480 GB"
            assert device.firmware is None
            assert device.supports_smart is True
            assert device.messages is not None
            assert device.is_ssd is True
            assert device.assessment == "PASS"