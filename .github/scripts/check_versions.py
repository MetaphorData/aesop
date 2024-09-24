# /usr/bin/env python3

import sys

from packaging.version import Version

if __name__ == "__main__":
    _, target_version, current_version = sys.argv
    print(f"target version = {target_version}")
    print(f"current version = {current_version}")
    if Version(target_version) <= Version(current_version):
        # Exit 1 if current version >= version to publish. Can't publish older versions!
        sys.exit(1)
