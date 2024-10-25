def movieResponseEntity(movie) -> dict:
    return {
        "title":movie["title"],
        "image":movie["image"]
    }

def movieResponseList(movies) -> list:
    return [movieResponseEntity(movie["_source"]) for movie in movies]
