import json

def convert_string_to_list(string):
    """
        Receive a comma-separated string and convert it to its type
        exm:
            convert_string_to_list("1,2.3,4,5.6")
        result:
            [1,2.3,4,5.6]
            int,float,int,float
    """
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json