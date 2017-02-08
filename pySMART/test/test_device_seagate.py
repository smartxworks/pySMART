from contextlib import nested
import pytest
import mock


@pytest.fixture
def seagate_cmd_all_attr():
    """
    This is output from smartctl -d scsi -a /dev/sdg, sdg is a seagate harddisk.
    :return:
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.el7.centos.lenovo.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===
Vendor:               SEAGATE
Product:              ST200FM0053
Revision:             LV60
User Capacity:        200,049,647,616 bytes [200 GB]
Logical block size:   512 bytes
Physical block size:  4096 bytes
Lowest aligned LBA:   0
Logical block provisioning type unreported, LBPME=1, LBPRZ=1
Rotation Rate:        Solid State Device
Form Factor:          2.5 inches
Logical Unit id:      0x5000c5003012c457
Serial number:        Z3E018060000Z3E01806
Device type:          disk
Transport protocol:   SAS
Local Time is:        Fri Jun 24 17:58:26 2016 CST
SMART support is:     Available - device has SMART capability.
SMART support is:     Enabled
Temperature Warning:  Enabled
=== START OF READ SMART DATA SECTION ===
SMART Health Status: OK
SS Media used endurance indicator: 2%
Current Drive Temperature:     28 C
Drive Trip Temperature:        65 C
Manufactured in week 46 of year 2014
Specified cycle count over device lifetime:  10000
Accumulated start-stop cycles:  78
Elements in grown defect list: 0
Vendor (Seagate) cache information
  Blocks sent to initiator = 3109652935
  Blocks received from initiator = 2909972264
  Blocks read from cache and sent to initiator = 2803869649
  Number of read and write commands whose size <= segment size = 3002819484
  Number of read and write commands whose size > segment size = 782728839
Vendor (Seagate/Hitachi) factory information
  number of hours powered up = 5728.55
  number of minutes until next internal SMART test = 11
Error counter log:
           Errors Corrected by           Total   Correction     Gigabytes    Total
               ECC          rereads/    errors   algorithm      processed    uncorrected
           fast | delayed   rewrites  corrected  invocations   [10^9 bytes]  errors
read:          0        0         0         0          0      21383.352           0
write:         0        0         0         0          0      47672.100           0
verify:        0        0         0         0          0          0.021           0
Non-medium error count:        0
SMART Self-test log
Num  Test              Status                 segment  LifeTime  LBA_first_err [SK ASC ASQ]
     Description                              number   (hours)
# 1  Background short  Completed                   -    2011                 - [-   -    -]
# 2  Background short  Completed                   -    1986                 - [-   -    -]
# 3  Background short  Completed                   -    1962                 - [-   -    -]
# 4  Background short  Completed                   -    1938                 - [-   -    -]
# 5  Background short  Completed                   -    1914                 - [-   -    -]
# 6  Background short  Completed                   -    1890                 - [-   -    -]
# 7  Background short  Completed                   -    1866                 - [-   -    -]
# 8  Background short  Completed                   -    1842                 - [-   -    -]
# 9  Background short  Completed                   -    1818                 - [-   -    -]
#10  Background short  Completed                   -    1794                 - [-   -    -]
#11  Background short  Completed                   -    1770                 - [-   -    -]
#12  Background short  Completed                   -    1746                 - [-   -    -]
#13  Background short  Completed                   -    1722                 - [-   -    -]
#14  Background short  Completed                   -    1698                 - [-   -    -]
#15  Background short  Completed                   -    1682                 - [-   -    -]
#16  Background short  Completed                   -    1650                 - [-   -    -]
#17  Background short  Completed                   -    1626                 - [-   -    -]
#18  Background short  Completed                   -    1602                 - [-   -    -]
#19  Background short  Completed                   -    1579                 - [-   -    -]
#20  Background short  Completed                   -    1555                 - [-   -    -]
Long (extended) Self Test duration: 32767 seconds [546.1 minutes]
    """
    return stdout, stderr


@pytest.fixture
def seagate_cmd_sataphy():
    """
    Output for seagate's disk for `smartctl -d scsi -l sataphy /dev/<sdx>`
    :return:
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.el7.centos.lenovo.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

SCSI device successfully opened

Use 'smartctl -a' (or '-x') to print SMART (and more) information
    """
    return stdout, stderr


@pytest.fixture
def seagate_cmd_sasphy():
    """
    cmd is `smartctl -d scsi -l sasphy /dev/sdg`
    """
    stderr = ""
    stdout = """
smartctl 6.2 2013-07-26 r3841 [x86_64-linux-3.10.0-327.el7.centos.lenovo.x86_64] (local build)
Copyright (C) 2002-13, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
Protocol Specific port log page for SAS SSP
relative target port id = 1
  generation code = 12
  number of phys = 1
  phy identifier = 0
    attached device type: end device
    attached reason: unknown
    reason: unknown
    negotiated logical link rate: phy enabled; 6 Gbps
    attached initiator port: ssp=1 stp=1 smp=1
    attached target port: ssp=0 stp=0 smp=0
    SAS address = 0x5000c5003012c449
    attached SAS address = 0x500605b00989e604
    attached phy identifier = 7
    Invalid DWORD count = 52
    Running disparity error count = 52
    Loss of DWORD synchronization = 19
    Phy reset problem = 0
    Phy event descriptors:
     Invalid word count: 52
     Running disparity error count: 52
     Loss of dword synchronization count: 19
     Phy reset problem count: 0
relative target port id = 2
  generation code = 12
  number of phys = 1
  phy identifier = 1
    attached device type: no device attached
    attached reason: unknown
    reason: unknown
    negotiated logical link rate: phy enabled; unknown
    attached initiator port: ssp=0 stp=0 smp=0
    attached target port: ssp=0 stp=0 smp=0
    SAS address = 0x5000c5003012c44a
    attached SAS address = 0x0
    attached phy identifier = 0
    Invalid DWORD count = 0
    Running disparity error count = 0
    Loss of DWORD synchronization = 0
    Phy reset problem = 0
    Phy event descriptors:
     Invalid word count: 0
     Running disparity error count: 0
     Loss of dword synchronization count: 0
     Phy reset problem count: 0

    """

    return stdout, stderr


class TestDeviceWithSeagate:

    def test_device_with_seagate(
        self,
        seagate_cmd_all_attr,
        seagate_cmd_sasphy,
        seagate_cmd_sataphy,
        cmd_scan_open_as_root,
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
        ) as (mocked_all_with_type, mocked_sas, mocked_sata, mocked_scan):
            mocked_all_with_type.return_value = seagate_cmd_all_attr
            mocked_sas.return_value = seagate_cmd_sasphy
            mocked_sata.return_value = seagate_cmd_sataphy
            mocked_scan.return_value = cmd_scan_open_as_root
            devices = [Device("sdg"),
                       Device('/dev/bus/0', interface='sat+megaraid,11')]
            for device in devices:
                assert device.serial == "Z3E018060000Z3E01806"
                assert device.model == "ST200FM0053"
                assert device.capacity == "200 GB"
                assert device.firmware == "LV60"
                assert device.supports_smart is True
                assert device.messages is not None
                assert device.is_ssd is True
                assert device.assessment == "PASS"
