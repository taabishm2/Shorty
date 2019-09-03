import hashlib
import validate_url
import arbitrary_encoder
import db_upload
import db_fetch

def url_hash(url):
    '''Obtain 160 bit hash of the input url using SHA1'''

    url = url.encode('utf-8')
    h = hashlib.sha1(url)
    return h.hexdigest()

def url_encode(url):
    '''Main function that executes all required processes to generate shortlink'''

    url = url.strip()

    if not validate_url.validate_url(url):
        raise Exception('URL_Validity_Error:Invlaid URL entered')

    h = url_hash(url)
    base = arbitrary_encoder.base_change(h,16,73) #160 bit Hex always generates 26 digit Base73 value

    for i in range(0,20):
        shortlink = base[i:i+6]
        if db_upload.upload_link(shortlink,url):
            return(shortlink)  #If shortlink not found in database or if found & link is same
    else:
        raise Exception("Shortkey_space_exhausted:Modify the url to check other scopes")

def url_decode(shortkey):
    '''Returns original link corresponsding to the shortkey (if present)'''

    return db_fetch.fetch_link(shortkey)


url_encode("www.google.com")

