car = {
    "brand" : "Mahindra",
    "model" : "Scorpio N",
    "year" : 2026
}
car["color"] = "Black"
del car["color"]
for k ,v in car.items():
    print(f"{k} : {v}")