#!/usr/bin/python3

import os
import tempfile
import shutil

# Check if we're root

if os.geteuid() != 0:
	print('fatal: pacdl must be run as root.')

# Lock the db. Note that the db itself isn't what needs to be locked, but the package archive.
# Otherwise, there could be file write collisions.

# TODO

# Create a temporary copy of the db structure, so that we can get the list of new packages without messing with the existing system <-> db relationship.

tmpdir = tempfile.TemporaryDirectory(prefix='pacdl-')

shutil.copytree('/var/lib/pacman/sync/', os.path.join(tmpdir.name, 'db'))

# Run pacman

# TODO

# Cleanup

tmpdir.cleanup()
