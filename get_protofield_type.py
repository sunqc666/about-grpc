def get_F2F_field_type(field_name):
    type_dict={
        "1": "double",
        "2": "float",
        "3": "int64",
        "4": "uint64",
        "5": "int32",
        "6": "fixed64",
        "7": "fixed32",
        "8": "bool",
        "9": "string",
        "10": "group",
        "11": "message",
        "12": "bytes",
        "13": "uint32",
        "14": "enum",
        "15": "sfixed32",
        "16": "sfixed64",
        "17": "sint32",
        "18": "sint64"
    }
    obj=test_pb2.MyInfo()
    for field in obj.DESCRIPTOR.fields:
        if field.name==field_name:
            return type_dict[str(field.type)]
