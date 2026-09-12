#import core modules
import requests
import os

#class system
class EasyDownload:
    def __init__(self):
        pass


    def download_file(self, url, filename, directory, chunk_size=4096):
        percentage = 0.0
        if not os.path.exists(directory):
            os.makedirs(directory)


        full_path = os.path.join(directory, filename)

        #requests protocol

        response = requests.get(url, stream=True)

        total_size = int(response.headers.get('content-length'))

        if total_size is None:
            #DOWNLOAD WITHOUT PERCENTAGE
            with open(full_path, "wb") as file:
                file.write(response.content)
            print("FILE DOWNLOADED WITHOUT SIZE")
            percentage = 100.0
            return


        total_size = int(total_size)
        downloaded = 0

        with open(full_path, "wb") as file:

            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    downloaded += len(chunk)
                    #set percentage variable
                    percentage = (downloaded / total_size) * 100
                    yield percentage






