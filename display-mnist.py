import gzip
import struct

# Display the contents of the MNIST dataset with minimal boilerplate.
# The following mapping from grayscale (byte) values to ASCII art is used:

def byte_to_ascii(val):
 intensities = " `.:^~;+*?D0#%B@"
 return intensities[int(val / 256.0 * len(intensities))]

# The image files have the following format:
# This is a gzipped big-endian file with the following format:
#   [offset] [type]          [value]          [description]
#   0000     32 bit integer  0x00000803(2051) magic number
#   0004     32 bit integer  60000            number of images
#   0008     32 bit integer  28               number of rows
#   0012     32 bit integer  28               number of columns
#   0016     unsigned byte   ??               pixel
#   0017     unsigned byte   ??               pixel
#   ...

images = gzip.open("t10k-images-idx3-ubyte.gz", "rb")
_, num_images, num_rows, num_cols = struct.unpack(">IIII", images.read(16))

# The label files have the following format:
#   [offset] [type]          [value]          [description]
#   0000     32 bit integer  0x00000801(2049) magic number (MSB first)
#   0004     32 bit integer  60000            number of items
#   0008     unsigned byte   ??               label
#   0009     unsigned byte   ??               label
#   ...

labels = gzip.open("t10k-labels-idx1-ubyte.gz")
_, num_labels = struct.unpack(">II", labels.read(8))

assert(num_labels == num_images)

for i in range(0, num_images):
  label = int(labels.read(1)[0])
  print()
  print(f"Entry: #{i:04}, Label: {label}")
  print("==" * (num_cols+1))
  for r in range(0, num_rows):
    col_data = images.read(num_cols)
    col_data = " ".join([byte_to_ascii(c) for c in col_data])
    print(f"={col_data} =")
  print("==" * (num_cols+1))
