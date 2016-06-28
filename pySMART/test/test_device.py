from contextlib import nested
import mock


def test_device_with_seagate(
    seagate_cmd_all_attr,
    seagate_cmd_sasphy,
    seagate_cmd_sataphy,
    cmd_scan_open_as_root,
    cmd_scan_open_non_root,
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
        mocked_all.return_value = seagate_cmd_all_attr
        mocked_sas.return_value = seagate_cmd_sasphy
        mocked_sata.return_value = seagate_cmd_sataphy
        mocked_scan.return_value = cmd_scan_open_as_root
        device = Device("sdg")
        mocked_scan.return_value = cmd_scan_open_non_root
        device = Device("sdg")
