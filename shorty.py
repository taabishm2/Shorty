import hashlib
import validate_url

def url_hash(url):
    '''Obtain 160 bit hash of the input url using SHA1'''

    url = url.encode('utf-8')
    h = hashlib.sha1(url)
    return h.digest()

def url_encode(url):
    '''Main function that executes all required processes to generate shortlink'''

    url = url.strip()
    
    if not validate_url.validate_url(url):
        raise Exception('URL_Validity_Error:Invlaid URL entered')

    h = url_hash(url)
    
    

    
