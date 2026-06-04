#!/usr/bin/env python3
import subprocess
import time

time.sleep(0.5)

subprocess.run(
    ["/usr/bin/xdotool", "type", "abc"]
)
"""

from pathlib import Path

Path("/tmp/test-hotkey.txt").write_text("it works\n n00o")
"""