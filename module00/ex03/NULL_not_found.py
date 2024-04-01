def NULL_not_found(object: any) -> int:
	types_of_null = {
		None : "Nothing",
		float : "Cheese",
		int : "Zero",
		str : "Empty",
		bool : "Fake",
	}
	if isinstance(object, str) and len(object) < 1: #for the strings not empty
		print(f"{types_of_null[type(object)]}: {type(object)}")
		return 0
	elif object == None: #for the NoneType
		print(f"{types_of_null[None]}: {object} {type(object)}")
		return 0
	elif object == 0 or object == False: #for the numbers or bool not null
		print(f"{types_of_null[type(object)]}: {object} {type(object)}")
		return 0
	elif isinstance(object, float) and object != object: #for the float  not null
		print(f"{types_of_null[type(object)]}: {object} {type(object)}")
		return 0
	else:
		print("Type not found!")
		return 1