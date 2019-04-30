import hashlib

def url_hash(url):
    '''Obtain 160 bit hash of the input url using SHA1'''

    url = url.encode('utf-8')
    h = hashlib.sha1(url)
    return h.hexdigest()


