
from fastapi import APIRouter, UploadFile, File, Depends, Request, HTTPException, status, Response
from fastapi.responses import JSONResponse
from ..schemas.gameSchemas import GameResponse
from ..serializers.movieSerializers import movieResponseList
from core.db.elasticConnection import client
from ..crud.searchBLL import  build_vector_search_query
from ..crud.featuresBLL import get_vector
from datetime import datetime, timedelta
from config import settings
router = APIRouter()

index = settings.INDEX_ELASTIC


@router.get("/", tags=["GET"])
async def get():
    return {"teste"}

@router.post("/upload/", tags=["POST"])
async def upload_image(image: UploadFile = File(...)):

        print(image.filename)
        vector = get_vector(image.file)
        query = build_vector_search_query(vector)
        result = client.search(index = index, query = query, size=20,from_=0,min_score=1)
        movies = movieResponseList(result["hits"]["hits"])
        print(movies)
        return movies
        # Definindo o caminho para salvar a imagem
        file_location = f"uploads/{image.filename}"
        
        # Salvando o arquivo de imagem
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(image.file, file_object)
        
        return {"info": f"Image '{image.filename}' uploaded successfully"}

    

# @router.get("/", status_code=status.HTTP_202_ACCEPTED, tags=["GET"])
# def get_search(
#     search_term: str,
#     limit: int = 20, 
#     offset: int = 0
#     ) -> list:
    
#     terms = term_vallidation(search_term)
#     vector = get_vector(search_term)
#     query = build_search_query(terms,limit,offset,True,must_exist,vector)
    
#     result = client.search(index = index, query = query, size=limit,from_=offset,min_score=1)
#     if result["hits"]["total"]["value"] == 0:
#         query = build_search_query(terms,limit,offset,False,must_exist,vector)
#         result = client.search(index = index, query = query, size=limit,from_=offset,min_score=1)
    
#     games = gameResponseList(result["hits"]["hits"])
#     return games
    
# @router.get("/vector", status_code=status.HTTP_202_ACCEPTED, tags=["GET"])
# def get_vector_search(
#     search_term: str,
#     limit: int = 20, 
#     offset: int = 0
#     ) -> list:

#     vector = get_vector(search_term)
#     query = build_vector_search_query(vector, must_exist=must_exist)
#     result = client.search(index = index, query = query, size = limit,from_ = offset,min_score = 1)
#     games = gameResponseList(result["hits"]["hits"])
#     return games 