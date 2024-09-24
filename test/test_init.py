# coding=utf-8
"""Tests QGIS plugin init."""


__author__ = "Tim Sutton <tim@linfiniti.com>"
__revision__ = "$Format:%H$"
__date__ = "17/10/2010"
__license__ = "GPL"
__copyright__ = (
    "Copyright 2012, Australia Indonesia Facility for " + "Disaster Reduction"
)
import configparser
import logging
import os
import unittest

LOGGER = logging.getLogger("QGIS")


class TestInit(unittest.TestCase):
    """Test that the plugin init is usable for QGIS.

    Based heavily on the validator class by Alessandro
    Passoti available here:

    http://github.com/qgis/qgis-django/blob/master/qgis-app/
             plugins/validator.py

    """

    def test_read_init(self):
        """Test that the plugin __init__ will validate on plugins.qgis.org."""

        # You should update this list according to the latest in
        # https://github.com/qgis/qgis-django/blob/master/qgis-app/
        #        plugins/validator.py

        required_metadata = [
            "name",
            "description",
            "version",
            "qgisMinimumVersion",
            "email",
            "author",
        ]

        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, "metadata.txt")
        )
        LOGGER.info(file_path)
        metadata = []
        parser = configparser.ConfigParser()
        parser.optionxform = str
        parser.read(file_path)
        message = f'Cannot find a section named "general" in {file_path}'
        assert parser.has_section("general"), message
        metadata.extend(parser.items("general"))

        # sourcery skip: no-loop-in-tests
        for expectation in required_metadata:
            message = f'Cannot find metadata "{expectation}" in metadata source ({file_path}).'

            self.assertIn(expectation, dict(metadata), message)


if __name__ == "__main__":
    unittest.main()
