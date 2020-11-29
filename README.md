# Stream of Consciousness

Fancy twtxt feed display on Gemini, with an added post-by-Gemini feature.

## How to set up

1. Clone this repository to somewhere your gemini server can access it.
2. Run `setup.sh`. Also, edit `DISPLAY_NAME` in `index.gmi` to be your handle instead of mine.
3. Set up your client to use a client certificate, and access `certinfo.gmi`. Copy the given hash into `.accepted_hashes` and refresh the page. The last line should now say `Certificate is in list`.
4. Go to `index.gmi`. There should be a link at the top saying `You can post to this stream of consciousness here.` (Don't worry; this only appears as a convenience feature, since you're using a client certificate that the Stream of Consciousness knows it can take a post from.)
5. Follow the link, input your text, and it should spit you back out to `index.gmi` with your new post included.

If all of this worked, congratulations! You've now got a working stream of consciousness. New certs can be added to `.accepted_hashes` in the same way as the first cert was.

## Compatibility

|Server name|Works|Notes|
|-|-|-|
|gemserv|Yes|I wrote this on tilde.team, which uses gemserv.|
|GLV-1.12256|Yes||
|molly-brown|No|[at least, not until my PR gets merged](https://tildegit.org/solderpunk/molly-brown/pulls/14)|
|blizanci|No|Exposes `REMOTE_USER`, but what I really need is `TLS_CLIENT_HASH`.|
|Agate|No|No CGI support in Agate as of yet.|
|Space-Age|No|Space-Age only supports Clojure CGI, and this is Python.|
|Denoscuri|No|Denoscuri has no CGI support, and doesn't plan to add arbitrary CGI support.|
|Flounder|No|[it uses a library that has no CGI support](https://github.com/MineRobber9000/stream-of-consciousness/issues/1)|

Let me know if you try this with any other servers.
