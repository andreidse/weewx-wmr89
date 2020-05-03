#
#    Copyright (c) 2020 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
"""Installer for WMR89"""

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

import configobj
from weecfg.extension import ExtensionInstaller

wmr89_config = """
[WMR89]
    # This section is for the Oregon Scientific WMR89

    # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
    port = /dev/ttyUSB0

    # The driver to use:
    driver = weewx.drivers.wmr89
    
    # Sensor map: map from sensor name to observation name
    [[sensor_map]]
"""

wmr89_dict = configobj.ConfigObj(StringIO(wmr89_config))


def loader():
    return WMR89Installer()


class WMR89Installer(ExtensionInstaller):
    def __init__(self):
        super(WMR89Installer, self).__init__(
            version="1.0.0",
            name='wmr89',
            description='Driver for the Oregon Scientific WMR89',
            author="Thomas Keffer",
            author_email="tkeffer@gmail.com",
            config=wmr89_dict,
            files=[('bin/user', ['bin/user/wmr89.py'])]
        )
