from datetime import datetime


class CachedFileServer:
    def __init__(self):
        self.cache = dict()

    def read(self, filename):
        if not(filename in self.cache.keys()):
            content = self.__read_file(filename)
            self.__save_to_cache(filename, content)
            return content

        content = self.cache[filename]
        return content["content"]

    @staticmethod
    def __read_file(filename):
        file = open(filename, "r")
        content = str.encode(file.read())

        return content

    def __save_to_cache(self, filename, content):
        self.cache[filename] = {
            "last_open": datetime.now(),
            "content": content
        }
