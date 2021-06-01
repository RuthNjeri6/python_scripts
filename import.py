#!/usr/bin/python3
import requests
import json

import functools

url = 'http://localhost:8500/api/doc'

root_id = "86164651-dd05-437a-a2ae-158ec3391ea7" 

# sample
child_objects = [
    {
        "label": "Grade 2",
        "children":[
            {
                "label": "Science",
                "children": [
                    {
                        "label": "Term 1 KBP5S",
                        "children": [
                            {
                                "label": "Opener Exam",
                                "children": [
                                    {
                                        "type": "question",
                                        "children": [
                                            {
                                                "type": "parts",
                                                "order": 0,
                                                "children": [
                                                    {
                                                        "type": "label",
                                                        "order": 0,
                                                        "label": "The type of tooth with pointed edges and one root is mainly used for",
                                                    },
                                                    {
                                                        "type": "dash",
                                                        "order": 1,
                                                        "children": [
                                                            {
                                                                "type": 'option',
                                                                "fraction": 1.0,
                                                                "label": "tearing flesh"
                                                            },
                                                            {
                                                                "type": 'option',
                                                                "fraction": 0.0,
                                                                "label": "cutting food"
                                                            },
                                                            {
                                                                "type": 'option',
                                                                "fraction": 0.0,
                                                                "label": "biting food"
                                                            },
                                                            {
                                                                "type": 'option',
                                                                "fraction": 0.0,
                                                                "label": "chewing food"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "label": "Math"
            },
            {
                "label": "English"
            }
        ]
    },
    {
        "label": "Grade 1",
        "children":[
            {
                "label": "Kiswahili",
                "children": [
                    {
                        "label": "Topic 1"
                    },
                    {
                        "label": "Topic 2"
                    },
                ]
            },
            {
                "label": "Math"
            },
            {
                "label": "English"
            },
            {
                "label": "Science"
            }
        ]
    },
  
]


def mapper(child_object, parent_id):
    # save the object
    data = child_object
    data["parent_id"] = parent_id
    data["type"] = 'node'

    res_data = requests.post(url, data = data, headers={
        'Accept': 'application/json'
    })

    res_data = json.loads(res_data.text)
    
    # check for errors
    print(res_data)

    # obtain the id
    newId = res_data['id']

    # repeat for kids
    if 'children' in child_object:
        res_data['children'] = list(map(functools.partial(mapper, parent_id=newId), child_object['children']))

    return res_data


tree = list(map(functools.partial(mapper, parent_id=root_id), child_objects))


# print(tree)
