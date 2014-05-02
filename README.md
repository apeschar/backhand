Backhand
========

This is a super-simple version of the `bcvi` tool. You'll need to have web.py
installed:

    sudo easy_install web.py

The `server.py` script runs a HTTP server on the given port. This server
responds to POST requests on /vi and runs Vim with the supplied `sftp://` URL.

    python2.7 server.py 2398

Add the following to your `~/.ssh/config`:

    Host *
        RemoteForward 2398 localhost:2398

And copy over `remote/bhvi` to `~/bin` or `/usr/local/bin` on your remote host.
After this you'll be able to do this:

    [user@client]$ ssh user@host
    [user@host]$ bhvi /path/to/whatever/file

... and the file will open in your local Vim.

__Note:__ currently the Vim command that is run is hardcoded as:

    mvim --servername hq --remote-tab sftp://...

Change `mvim` to `gvim` in `server.py` if you're not on Mac.
