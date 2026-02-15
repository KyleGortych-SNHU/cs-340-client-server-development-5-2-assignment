""" 
Test script for CRUD_Python_Module.py

Maintainer: Kyle Gortych
Date: 02/11/2026
"""

from CRUD_Python_Module import CRUD

def main():
    db = CRUD()

    test_doc = {
        "name": "Luna",
        "species": "Cat",
        "age": 5
    }

    print("\n--- Create Test ---")

    db.delete({"name": "Luna"})

    created = db.create(test_doc)
    print("Create result:", created)

    print("\n--- Read Test ---")

    results = db.read({"name": "Luna"})
    print("Read results:")
    for doc in results:
        print(doc)

    print("\n--- Update Test ---")

    update_result = db.update(
        {"name": "Luna"},
        {"$set": {"age": 6}}
    )

    print("Number of documents updated:", update_result)

    updated_doc = db.read({"name": "Luna"})
    print("Updated document:")
    for doc in updated_doc:
        print(doc)

    print("\n--- Delete Test ---")

    delete_result = db.delete({"name": "Luna"})
    print("Number of documents deleted:", delete_result)

    final_check = db.read({"name": "Luna"})
    print("Final read after delete should return empty list:", final_check)

if __name__ == "__main__":
    main()
