ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

tuple_list = list(ft_tuple)
tuple_list[1] = "United Arab Emirates!"
ft_tuple = tuple(tuple_list)

ft_set.remove("tutu!")
ft_set.add("Abudhabi!")

ft_dict["Hello"] = "42Abudhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
