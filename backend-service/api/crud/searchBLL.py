# import nltk
# from nltk.corpus import stopwords

# def term_vallidation(term: str):
#     nltk.download('stopwords')
#     stop_words = set(stopwords.words('english'))
#     terms = {}
#     terms["original"] = term
    
#     list_stop = []
#     for i in term.split(" "):
#         if i.lower() not in stop_words:
#             list_stop.append(i.lower())
    
#     terms["stopword"] = list_stop

#     terms["splited"] = term.lower().split(" ")
    
#     return terms


def build_search_query(terms: dict, limit: int, offset: int, first: bool, must_exist: list, vector: list):
    #to do
    #name normal sem remover stopword
    # prefix, fuzzy
    #primeira  remove stopword simple/lowercase/whitespace
    #segunda nao remove stopword stemmer/stopwords
    full_query = {
    }

    query = {
        "function_score":{
            "boost_mode": "multiply",
            "score_mode": "sum",
            "query":{
                "bool":{
                    "filter":[
                        #add filter
                    ]
                    # add query
                }
            }
        }
    }

    lista_exist = []
    for tp in must_exist:
        if "exists" in tp:
            for exists in must_exist[tp]:
                lista_exist.append(
                    {
                        "exists":{
                            "field":exists
                        }
                    }
                )
    
    if first:
        terms_stop = terms.get("stopword")
        if  terms_stop is not None and len(terms_stop)>0:
            lista_bool = []
            for i in terms["stopword"]:
                lista_bool.append(
                    {
                        "multi_match":{
                            "fields":[
                                "name.my_standard_stop",
                                "themes.my_standard_stop"
                            ],
                            "query": i,
                            "type": "most_fields"
                        }
                    }
                )
            query["function_score"]["query"]["bool"] = {
                "filter":lista_exist,
                "must":lista_bool
            }
        else:
            query["function_score"]["query"] = {
                "multi_match":{
                    "fields":[
                        "name.my_standard_stop",
                        "themes.my_standard_stop"
                    ],
                    "query": terms["original"],
                    "type": "most_fields"
                }
            }
    else:
        lista_bool = []
        terms_stop = terms.get("stopword")
        if  terms_stop is not None and len(terms_stop)>0:
            for i in terms["stopword"]:
                lista_bool.append(
                    {
                        "multi_match":{
                            "fields":[
                                "name.my_standard_stop",
                                "themes.my_standard_stop"
                            ],
                            "query": i,
                            "type": "most_fields",
                            "fuzziness" : "AUTO",
                            "prefix_length" : 2
                        }
                    }
                )
                lista_bool.append(
                    {
                        "multi_match":{
                            "fields":[
                                "name.my_standard",
                                "themes.my_standard"
                            ],
                            "query": i,
                            "type": "phrase_prefix"
                        }
                    }
                )
            # query["function_score"]["query"]["bool"] = {
            #     "filter":lista_exist,
            #     "should":lista_should
            # }
        else:
            for i in terms["splited"]:
                lista_bool.append(
                    {
                        "multi_match":{
                            "fields":[
                                "name.my_standard",
                                "themes.my_standard"
                            ],
                            "query": i,
                            "type": "most_fields",
                            "fuzziness" : "AUTO",
                            "prefix_length" : 2
                        }
                    }
                )
                lista_bool.append(
                    {
                        "multi_match":{
                            "fields":[
                                "name.my_standard",
                                "themes.my_standard"
                            ],
                            "query": i,
                            "type": "phrase_prefix"
                        }
                    }
                )
                
            # query["function_score"]["query"]["bool"] = {
            #     "filter":lista_exist,
            #     "should":lista_should
            # }
    
    query["function_score"] = {
        "boost_mode": "multiply",
        "score_mode": "sum",
        "query":{
            "bool":{
                "filter":lista_exist,
                "should":lista_bool
            }
        }
        ,
        "script_score":{
            "script": {
                "source": "doc['game_vector'].size() == 0 ? 0 : cosineSimilarity(params.queryVector, 'game_vector')+1.0",
                "params":{
                    "queryVector":vector
                }
            }
        }
    }


    
    full_query = query


    return full_query


def build_vector_search_query(vector: list,  limit: int = 20, offset: int = 0, must_exist: list = None):
   
    

    query = {
        "script_score":{
            "query":{
               "match_all":{
                   
               }
            },
            "script": {
                "source": "doc['image_vector'].size() == 0 ? 0 : cosineSimilarity(params.queryVector, 'image_vector')+1.0",
                "params":{
                    "queryVector":vector
                }
            }
        }
    }
    return query