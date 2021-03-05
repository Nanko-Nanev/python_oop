class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]
        self.max_len = 4

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(int(photos_count / 4))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free spots"

    def display(self):
        res = ""
        for page in self.photos:
            res += "-----------\n"
            res += " ".join(['[]' for photo in page])
            res += "\n"
        res += "-----------"
        return res


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

