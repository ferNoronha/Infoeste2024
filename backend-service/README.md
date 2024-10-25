# GameHub Service API

This API will be responsible for the gamehub's services responses and the user's track.

# List of services:
- Search-v1 (return a list of games based on a search term):
- Vectorial Search (Not implemented)
- Recommendations
    - released (new released games)
    - coming soon (games that will coming soon)
- User's Track
    - search track
    - click track
    - pageview track
       
## API Docummentation

### Searchs

#### Return a list of games

```http
  GET /search/
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `search_term` | `string` | **required**. The search term like a game name|
| `limit` | `int` | **optional**. Number of games to return by page, default=20|
| `offset` | `int` | **optional**. The offset of pagination, default=0|

```http
  GET /search/vector/
```
#### Return a list of games based on a search vector

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `search_term` | `string` | **required**. The search term like a game name|
| `limit` | `int` | **optional**. Number of games to return by page, default=20|
| `offset` | `int` | **optional**. The offset of pagination, default=0|

### Recommendations

#### Return a list of games that will be available soon
```http
  GET /recommendation/soon
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `date` | `int` | **optional**. The timestamp limit date of coming soon games, default=today|
| `limit` | `int` | **optional**. Number of games to return by rec, default=10|
| `theme` | `str` | **optional**. The filter theme game, default=None|
| `platform` | `str` | **optional**. The filter platform game, default=None|

#### Return a list of games that was released
```http
  GET /recommendation/released
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `date` | `int` | **optional**. The timestamp limit date of released games, default=today|
| `limit` | `int` | **optional**. Number of games to return by rec, default=10|
| `theme` | `str` | **optional**. The filter theme game, default=None|
| `platform` | `str` | **optional**. The filter platform game, default=None|

#### Return a list of best reviewed games based on igdb database 
```http
  GET /recommendation/reviewed
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `limit` | `int` | **optional**. Number of games to return by rec, default=10|
| `theme` | `str` | **optional**. The filter theme game, default=None|
| `platform` | `str` | **optional**. The filter platform game, default=None|




### Track

#### Insert search track
```http
  POST /track/search
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `date` | `int` | **optional**. The timestamp limit date of coming soon games, default=today|
| `error` | `str` | **optional**. If exists error on request|
| `ip` | `str` | **optional**. The network ip|
| `result_list` | `list` | **optional**. Games returned on search|
| `search_term` | `str` | **optional**. Search term|
| `time_response` | `str` | **optional**. Response time from search request|
| `total_result` | `int` | **optional**. Number of games found on search|
| `user_cookie` | `str` | **optional**. User cookie id|
| `user_id` | `str` | **optional**. User Id if they are logged|
| `user_session` | `str` | **optional**. User session|


#### Insert click track
```http
  POST /track/click
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `date` | `int` | **optional**. The timestamp limit date of coming soon games, default=today|
| `error` | `str` | **optional**. If exists error on request|
| `ip` | `str` | **optional**. The network ip|
| `url_game` | `str` | **optional**. Link of the clicked game|
| `click_type` | `str` | **optional**. If the click was on a search or recommendation|
| `time_response` | `str` | **optional**. Response time from search or recommendation request|
| `search_recommendation` | `str` | **optional**. The recommendation name or the search term|
| `user_cookie` | `str` | **optional**. User cookie id|
| `user_id` | `str` | **optional**. User Id if they are logged|
| `user_session` | `str` | **optional**. User session|

#### Insert pageview track 
```http
  POST /track/pv
```

| Param   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `date` | `int` | **optional**. The timestamp limit date of coming soon games, default=today|
| `error` | `str` | **optional**. If exists error on request|
| `ip` | `str` | **optional**. The network ip|
| `url_game` | `str` | **optional**. Link of the clicked game|
| `pv_time` | `str` | **optional**. Time that the user stay in the pagegame|
| `user_cookie` | `str` | **optional**. User cookie id|
| `user_id` | `str` | **optional**. User Id if they are logged|
| `user_session` | `str` | **optional**. User session|


## How to run

To run this API you need some python libs, to install just run:

```bash
  pip install -r requirements.txt
```
After this, you need create a .env file with API settings, the must itens in this file are:

```
ELASTIC_URL="http://localhost:9200"
GAME_INDEX_ELASTIC="index_name"
SEARCH_INDEX_ELASTIC="search_game_index"
CLICK_INDEX_ELASTIC="click_game_index"
PAGEVIEW_INDEX_ELASTIC="pv_game_index"
ENV="dev or production" (not using for now)
```

to run just execute this:
```bash
  uvicorn main:app --reload
```

## Stacks

**Back-end:** Python 3.12.3, FastAPI, Elasticsearch

**Readme:** https://readme.so/pt/editor 
