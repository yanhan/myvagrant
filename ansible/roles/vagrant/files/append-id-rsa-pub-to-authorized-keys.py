#!/usr/bin/env python

from __future__ import print_function

import os
import os.path
import sys

def main(ssh_pubkey_filename):
  ssh_pubkey = None
  with open(ssh_pubkey_filename, "r") as f:
    ssh_pubkey = f.readline().strip()
  authorized_keys_filename = os.path.join(os.environ["HOME"], ".ssh",
    "authorized_keys"
  )
  if os.path.isfile(authorized_keys_filename):
    found_ssh_pubkey_in_authorized_keys = False
    with open(authorized_keys_filename, "r") as f:
      for line in f:
        if line.strip() == ssh_pubkey:
          found_ssh_pubkey_in_authorized_keys = True
          break
    if not found_ssh_pubkey_in_authorized_keys:
      # append ssh public key to file
      with open(authorized_keys_filename, "a") as f:
        f.write("{}\n".format(ssh_pubkey))
      print(
        ("Appended SSH public key at \"{}\" to authorized keys file "
         "\"{}\"").format(ssh_pubkey_filename, authorized_keys_filename)
      )
  elif os.path.exists(authorized_keys_filename):
    print(
      "Error: SSH authorized keys file \"{}\" is not a file".format(
        authorized_keys_filename
      ), file=sys.stderr
    )
    sys.exit(1)
  else:
    # create new authorized keys file and write to it
    with open(authorized_keys_filename, "w") as f:
      f.write("{}\n".format(ssh_pubkey))
    print(
      ("Created new authorized keys file at \"{}\" with SSH public key "
       "\"{}\" as its contents".format(
         authorized_keys_filename, ssh_pubkey_filename
       )
      )
    )

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Please supply the path name to the SSH public key file you wish " +
      "to add to the authorized keys file.", file=sys.stderr
    )
    sys.exit(1)
  ssh_pubkey_filename = sys.argv[1]
  if not os.path.isfile(ssh_pubkey_filename):
    print("\"{}\" is not the name of a file".format(ssh_pubkey_filename),
      file=sys.stderr
    )
    sys.exit(1)
  main(ssh_pubkey_filename)
