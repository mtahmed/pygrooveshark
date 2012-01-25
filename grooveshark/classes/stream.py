# -*- coding:utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib.request
import urllib.parse

from grooveshark.core.const import *

class Stream(object):
    '''
    Get song's raw data.
    Do not use this class directly.
        
    :param ip: streaming server adress
    :param key: streaming key required to get the stream
    :param connection: underlying :class:`Connection` object
    '''
    def __init__(self, ip, key, connection):
        self._ip = ip
        self._key = key
        self._connection = connection
        self._data = None
        self._size = None
        
    def _request(self):
        request = urllib.request.Request('http://%s/stream.php' % (self._ip), data='streamKey=%s' % (self._key),
                                         headers={'User-Agent' : USER_AGENT})
        self._data = self._connection.urlopen(request)
        self._size = int(self.data.info().getheader('Content-Length'))
    
    @property
    def url(self):
        '''
        Stream URL.
        '''
        return 'http://%s/stream.php?streamKey=%s' % (self._ip, urllib.parse.quote_plus(self._key))
       
    @property
    def data(self):
        '''
        A file-like object containing song's raw data.
        '''
        if not self._data:
            self._request()
        return self._data
    
    @property
    def size(self):
        '''
        Size of the song's raw data in bytes.
        '''
        if not self._size:
            self._request()
        return self._size    