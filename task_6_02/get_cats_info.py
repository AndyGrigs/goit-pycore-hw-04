def get_cats_info(path:str)-> dict:
    cats = []
    try:
        with open(path, 'r') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat = {"id": id, "name": name, "age": age}
                cats.append(cat)
            return cats
    except Exception as e:
        print(f"Ой, помилочка: {e}")
        return None, None

cats_info = get_cats_info("cats_info.txt")
print(cats_info)
