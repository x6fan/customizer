#! /usr/bin/env python
# Mega Man X6 tweaks

# Image:  Mega Man X6 (USA) (v1.1).bin
# Size:   599985792 bytes
# CRC-32: 8e6d014d
# MD5:    237b6feddd1a88e86ab1cddc8822f03f
# SHA-1:  d4f7e08371027a87a3bf13311db5a4c56733f4ea
# Redump: http://redump.org/disc/32516/
def verify(x6_image, target_sha1 = 'd4f7e08371027a87a3bf13311db5a4c56733f4ea', block_size = 64 * 1024):
    from hashlib import sha1

    sha1_hash = sha1()
    blocks = iter(lambda: x6_image.read(block_size), b'')

    for block in blocks:
        sha1_hash.update(block)

    computed_sha1 = sha1_hash.hexdigest()

    return computed_sha1 == target_sha1

def main(path):
    print('Verifying Mega Man X6 image: %s' % path)

    with open(path, 'rb', buffering = 0) as x6_image:
        if verify(x6_image):
            print('Verified: Mega Man X6 (USA) (v1.1)')
        else:
            print('Verification failed')

if __name__ == '__main__':

    from sys import argv

    path = argv[1]

    main(path)
