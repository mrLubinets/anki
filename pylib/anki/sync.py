# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
#
# Legacy attributes some add-ons may be using
#

from .httpclient import HttpClient

AnkiRequestsClient = HttpClient


class Syncer:
    def sync(self) -> str:
        pass
