

def make_car(manufact, model_name, **rest):
    print(f"\tModel: {manufact.title()} {model_name.title()}")
    for key, value in rest.items():
        if isinstance(value, int):
            print(f"\t{key.title()}: {value}")
        else:
            print(f"\t{key.title()}: {value.title()}")


car = make_car('ford', 'escort', color='red', year=1986, tow_package=True)
