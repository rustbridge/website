#!/usr/bin/env python3

import glob, os, subprocess, sys

status, _ = subprocess.getstatusoutput('convert -h')

if status != 1:
    print("`convert` not found. ImageMagick is required to to optimise images.")
    print("<http://www.imagemagick.org/index.php>")
    sys.exit()

for filename in glob.glob('assets/img/*.original.jpg'):
    directory = os.path.dirname(filename)
    # foo.original.jpg -> foo.jpg
    basename = os.path.splitext(os.path.splitext(filename)[0])[0]
    new_name = f'{basename}.jpg'

    print(f'Processing {filename} -> {new_name}')

    # Adapted from https://stackoverflow.com/questions/7261855/recommendation-for-compressing-jpg-files-with-imagemagick
    command = [
        'convert',
        '-strip',
        '-interlace', 'Plane',
        '-gaussian-blur', '0.05',
        '-quality', '85%',
        # 'x1080' will scale the image's height to 1080px while maintaining the
        # current aspect ratio.
        '-resize', 'x1080',
        filename,
        new_name,
    ]

    subprocess.run(command, check=True)

print("All images optimised ☀️")
