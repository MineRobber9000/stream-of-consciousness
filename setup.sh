#!/bin/sh

# Sets up your stream of consciousness. A stream of consciousness is basically
# just a fancy front-end to a twtxt feed that you can post to from Gemini using
# client cert authentication.

# First things first, make the client cert list.
echo "# Client cert hashes (as received by certinfo.gmi) go in here, one per line." > .accepted_hashes
chmod a=r,u+w .accepted_hashes

# Next, the plaintext.txt file that holds the twtxt feed.
# It doesn't need to contain anything by default but some servers will refuse to
# create it if it doesn't exist.

touch plaintext.txt
chmod a=rw plaintext.txt

# Yes, I know having it be world-writeable is a bad idea but I need this so the
# server can write to it. If you're running it on your own server, this
# shouldn't be a problem.
