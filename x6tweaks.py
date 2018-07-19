#! /usr/bin/env python
# Mega Man X6 tweaks

import os
import sys
import hashlib
import json

# Computes SHA-1 of a readable stream
def compute_sha1(io, block_size = 64 * 1024):
    sha1_hash = hashlib.sha1()
    blocks = iter(lambda: io.read(block_size), b'')

    for block in blocks:
        sha1_hash.update(block)

    return sha1_hash.hexdigest()

# Image:  Mega Man X6 (USA) (v1.1).bin
# Size:   599985792 bytes
# CRC-32: 8e6d014d
# MD5:    237b6feddd1a88e86ab1cddc8822f03f
# SHA-1:  d4f7e08371027a87a3bf13311db5a4c56733f4ea
# Redump: http://redump.org/disc/32516/
def verify(x6_image, target_sha1 = 'd4f7e08371027a87a3bf13311db5a4c56733f4ea'):
    return compute_sha1(x6_image) == target_sha1

# Converts value to size bytes and writes them at offset
def patch(io, offset, value, size):
    data = value.to_bytes(size, byteorder = 'little')
    io.seek(offset)
    io.write(data)

def tweak_parts_allowed(image, offsets, tweaks):
    patch(image, offsets['normal'], tweaks['normal'], 1)
    patch(image, offsets['limited'], tweaks['limited'], 1)

def tweak_ranks(image, rank_offsets, rank_tweaks):
    for rank, tweaks in rank_tweaks.items():
        offsets = rank_offsets[rank]

        if offsets['souls_required'] is not None:
            patch(image, offsets['souls_required'], tweaks['souls_required'], 2)

        tweak_parts_allowed(image, offsets['parts_allowed'], tweaks['parts_allowed'])

def tweak_x6(image, offsets, tweaks):
    if 'ranks' in tweaks:
        tweak_ranks(image, offsets['ranks'], tweaks['ranks'])

def main(x6_image_path, x6_offsets_path):
    x6_image = open(x6_image_path, 'r+b', buffering = 0)

    with x6_image:
        print('Verifying Mega Man X6 image: %s' % x6_image.name)

        if not verify(x6_image):
            print('Verification failed')
            return

        print('Verified: Mega Man X6 (USA) (v1.1)')

        with open(x6_offsets_path, 'r') as json_file:
            print('Loading offset data: %s' % json_file.name)

            x6_offsets = json.load(json_file)

        x6_tweaks = json.load(sys.stdin)

        tweak_x6(x6_image, x6_offsets, x6_tweaks)

if __name__ == '__main__':
    x6_image_path = os.path.abspath(sys.argv[1])
    x6_offsets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'x6_offsets.json'))

    main(x6_image_path, x6_offsets_path)
