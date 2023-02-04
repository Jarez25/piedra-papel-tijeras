countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAm.union(centralAm.union(southAm)))

pais = new_set

print(new_set)
