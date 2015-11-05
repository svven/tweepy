# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.


class TweepError(Exception):
    """Tweepy exception"""

    def __init__(self, reason, response=None, wait=None):
        self.reason = unicode(reason)
        self.response = response
        self.wait = wait # in case rate limit reached
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason
