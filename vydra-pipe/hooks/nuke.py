""" Hook and Nuke-related code """
from __future__ import unicode_literals, absolute_import, print_function, division
from .py3_fixes import builtins  # TODO: make sure this is in the system

import logging
from collections import namedtuple

import nuke  # TODO: make sure this is on the PATH? or PYTHONPATH?

from .. import parse  # TODO: write parse module

log = logging.getLogger(__name__)  # TODO: set up logging

class Hook(object):
    """Code for an open instance of Nuke"""
    def __init__(self, node):
        super(Hook, self).__init__()
        self.node = node

        cur_nuke_ver = parse.nuke_version(nuke.NUKE_VERSION_STRING)  # TODO: test this with Nuke
        self.nuke_version = namedtuple('NukeVersion', ['major', 'minor', 'micro'])(*cur_nuke_ver)
