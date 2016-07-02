import pytest


@pytest.fixture
def cmd_scan_open_as_root():
    """
    run `smartctl --scan-open` as root user.
    """
    stderr = ""
    stdout = """
/dev/sda -d sat # /dev/sda [SAT], ATA device
/dev/sdb -d sat # /dev/sdb [SAT], ATA device
/dev/sdc -d sat # /dev/sdc [SAT], ATA device
/dev/sdd -d sat # /dev/sdd [SAT], ATA device
/dev/sde -d sat # /dev/sde [SAT], ATA device
/dev/sdf -d sat # /dev/sdf [SAT], ATA device
/dev/sdg -d scsi # /dev/sdg, SCSI device
/dev/sdh -d scsi # /dev/sdh, SCSI device
/dev/bus/0 -d sat+megaraid,8 # /dev/bus/0 [megaraid_disk_08] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,9 # /dev/bus/0 [megaraid_disk_09] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,10 # /dev/bus/0 [megaraid_disk_10] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,11 # /dev/bus/0 [megaraid_disk_11] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,12 # /dev/bus/0 [megaraid_disk_12] [SAT], ATA device
/dev/bus/0 -d sat+megaraid,13 # /dev/bus/0 [megaraid_disk_13] [SAT], ATA device
/dev/bus/0 -d megaraid,16 # /dev/bus/0 [megaraid_disk_16], SCSI device
/dev/bus/0 -d megaraid,17 # /dev/bus/0 [megaraid_disk_17], SCSI device
    """
    return stdout, stderr


@pytest.fixture
def cmd_scan_open_non_root():
    stderr = ""
    stdout = """
# /dev/sda -d scsi # /dev/sda, SCSI device open failed: Permission denied
# /dev/sdb -d scsi # /dev/sdb, SCSI device open failed: Permission denied
# /dev/sdc -d scsi # /dev/sdc, SCSI device open failed: Permission denied
# /dev/sdd -d scsi # /dev/sdd, SCSI device open failed: Permission denied
# /dev/sde -d scsi # /dev/sde, SCSI device open failed: Permission denied
# /dev/sdf -d scsi # /dev/sdf, SCSI device open failed: Permission denied
# /dev/sdg -d scsi # /dev/sdg, SCSI device open failed: Permission denied
# /dev/sdh -d scsi # /dev/sdh, SCSI device open failed: Permission denied
    """
    return stdout, stderr