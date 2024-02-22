import requests
import sys
import uuid

class Utility:
    @classmethod
    def dowmload_contol_size(cls,url,size_file):
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            if r.headers.get('content-type').lower() !='application/octet-stream':
                raise ('bad file content-type')
            size_content_in_bytes=sys.getsizeof(r.content)
            size_content_in_megabytes=cls.bytes_to_megabytes(size_content_in_bytes)
        else:
            raise('error download')
        assert size_content_in_megabytes == size_file
        filename=cls.url_to_file_name(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename

    @staticmethod
    def bytes_to_megabytes(ibytes):
        fmegabytes = round(ibytes/pow(2,20),2)
        return fmegabytes
    @staticmethod
    def url_to_file_name(url):
        filename=''
        len_filename = url[::-1].find('/')
        if len_filename>0:
            filename = url[-len_filename:]
        if len(filename) == 0:
            filename = uuid.uuid4()
        return filename