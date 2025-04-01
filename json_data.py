# json_data
data = {
    "name": "Jackie Wang",
    "dob": "2007-10-18",
    "email": "wangash@gamil.com",
    "school": {
        "name": "MFA",
        "county": "Nairobi",
        "Kcse": {
            "score": "A",
            "students": 268
        }
    }
}

print(data["dob"])
county = data["school"]["county"]
print(county)
print(data["school"]["Kcse"]["score"])