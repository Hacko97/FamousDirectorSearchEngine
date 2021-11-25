# FamousDirectorSearch
This repository includes configuring elasticsearch and query searches.
Directory Structure
---
```
 ├── director-corpus : Modified data from the pre-processed data from actual (corpus) 
 ├── data_uplaod.py : Python file that converts JSON to a bulkdata and uploads to ElasticSearch Bulk API
 ├── query.py : ElasticSearch search queries
 ├── search.py : Search API call
 ├── analyzers : custom filters
```
Demo
---
* Install ElasticSearch 
* Add 'analyze' folder in config of Elasticsaeach and add files from analyzers
* Run ElasticSearch
* Run 'data_upload.py' and add data
* Search for famous directors - basic queries


SampleQueries
---
* Can search for directors if you just know name/directed_movies/awards/DOB.
 > E.g.- "நோலன்"
```
{
    "query": {
        "query_string": {
            "query":"நோலன்"
        }
    }
}
```

* Can search specifying the field when you just know director_name/directed_movies/awards/born_year/nominations.
```
{
     "query" : {
          "match" : {
             "name_ta" : "கிறிஸ்டோபர் நோலன்"
         }
     }
 }
```
* Can search with WildCard queries
 > E.g.- "நோ*" for "நோலன்"
 ```{
     "query" : {
          "match" : {
             "name_ta" : "நோ*"
         }
     }
 }
 ```
 * Can search multi match queries
 > E.g.- "ஆஸ்கார்"
```
{
      "query" : {
         "multi_match" : {
             "query" : "ஆஸ்கார்",
             "fields": ["awards_ta","nominations_ta"]
         }
     }
}
```

* Can search for Top-30 directors of particular order where Top is marked on their score
 > E.g. - மிகச்சிறந்த 30 இயக்குனர்கள் 
```{
   "size":30,
   "sort" : [
       { "score" : {"order" : "desc"}}
   ],
   "query": {
       "multi_match": {
           "fields": ["awards_ta", "awards_en"],
           "query" : "Oscar",
           "fuzziness": "AUTO"
       }
   }
}
```
 
 * Can do aggregated bucket querying with terms
 
 ```{
  "aggs": {
    "ratings": {
      "terms": { "field": "category" }
    }
  }
}
```
