def all_thing_is_obj(object: any) -> int:
    obj_types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }

    if (isinstance(object, str)):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (type(object) in obj_types):
        print(f"{obj_types[type(object)]} : {type(object)}")
    else:
        print("Type not found!")
    return 42