#!/usr/bin/python
# Copyright (c) 2013, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import shutil
import sys
import os
import stat
import struct

print "Generate Trusted OS Partition Image File"
input_name = filename = sys.argv[1]
output_name = filename = sys.argv[2]

with open(input_name) as f:
    data = f.read()

dest = open(output_name, 'w')
header = "NVTOSP\0" + str(len(data)) + '\0'
header = header + '\0' * (20-len(header)) #Align header to 512 bytes
header += struct.pack('<I', len(data))
header += struct.pack('<I', len(data))
header += struct.pack('<I', 0)
header += struct.pack('<I', 5)
header = header + '\0' * (512-len(header)) #Align header to 512 bytes
dest.write(header)

shutil.copyfileobj(open(input_name, 'rb'), dest)
dest.close()
os.chmod(output_name, (stat.S_IWUSR | stat.S_IRUSR) | stat.S_IRGRP | stat.S_IROTH)
