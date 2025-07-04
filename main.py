#Create, Reading and replacing the file.
with open("FileOperation.txt","r")as file:
    data = file.read()
    data = data.replace("abc", "def")
    print(data)

#Deleting the content
with open("FileDeleting.txt","w")as file:
    file.write("I have deleted data")
    with open("FileDeleting.txt") as file:
        print(file.read())

new_text = "Italian cuisine is known for its diverse regional dishes focusing on fresh ingredients and simple preparations Some iconic dishes include pizza pasta such as spaghetti and lasagna risotto and gelato Other popular items include bruschetta focaccia cacio e pepe and various seafood dishes"

# Check existing content
with open("Food.txt", "r") as file:
    existing_content = file.read()

# Only append if it's not already there
if new_text not in existing_content:
    with open("Food.txt", "a") as file:
        file.write(new_text + "\n")  # Add newline for readability

# Print file content
with open("Food.txt", "r") as file:
    print(file.read())
