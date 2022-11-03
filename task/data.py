#!/usr/bin/python3
'''json string to be used as example data'''
import json
def json_example():
    #python dict
    data={
        'operation_type':'add',
        'x': 5,
        'y': 10
    }
    #convert to json
    data_json = json.dumps(data)
    #json string returned
    return data_json
if __name__ == '__main__':
    json_example()