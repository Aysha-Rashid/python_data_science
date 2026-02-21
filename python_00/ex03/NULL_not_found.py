def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
        return (0)
    elif isinstance(object, bool) and object is False:
        print("Fake:", object, type(object))
        return (0)
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
        return (0)
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
        return (0)
    elif object == "":
        print("Empty:", object, type(object))
        return (0)
    print("Type not Found")
    return (1)
