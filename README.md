<p align="center">
<img title="vidur" src='https://github.com/ChiragKParmar/vidur/blob/master/img/vidur_logo.png'/>
</p>
------------------

Generating JSONPath from Json blob. 
---------------------------------

Vidur was a wisest minister of King Dhrutrashtra's cabinet in the great indian epic - "Mahabharat". Python script is our Vidur, generating JSONPath from JSON file.
https://en.wikipedia.org/wiki/Vidura

Example
-------------
```
python generate_jsonpath.py example/category_object_auto.json
```
```
["$['catdesc']",
 "$['catgroup']", 
 "$['catid']", 
 "$['catname']"
 ]
```
```
python generate_jsonpath.py ./example/nested_example.json
```
```
[   "$['id']",
    "$['image']['height']",
    "$['image']['url']",
    "$['image']['width']",
    "$['name']",
    "$['thumbnail']['height']",
    "$['thumbnail']['url']",
    "$['thumbnail']['width']",
    "$['type']"]
```

### Tested on Python 2.7.8

More Updates Coming Soon! 
---------------------------------
