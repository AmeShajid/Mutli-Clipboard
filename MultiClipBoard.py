#this is a multiclipboard program
#it will save each piece of clipboard text under a keyword
#to run these on mac we use python3 to run the program in linux

#first import these modules
import sys
import clipboard
#we want to store everything in our json file
import json

#this is for storing the name of our json file
SAVED_DATA = "clipboard.json"

#we are printing this because when we do python3 MultiClipBoard.py and anything after it will print in the terminal 
#we added the [1:] because we want to print everything after the first argument
#this is just for testing purposes
#print(sys.argv[1:])

#here we are creating a json file
def save_data(filepath, data):
    with open(filepath, "w") as f:#here we are making a file name and then we are opening the file in w mode which is write mode and basically empty and recreate it, then open it as file, and then open it as f and  we will dump all our json data into it
        json.dump(data, f)


#after making function make the function call to make the json
#save_items("data.json", {"hello": "world"})#this is just for testing purposes

#now we are going to read the json file
def load_data(filepath):
    try:#we are tryin all of this code becasue we might run into an issue where the json might not exist
        with open(filepath, "r") as f:#we are opening the file in read mode
            data = json.load(f)#we are returning the json data
            return data
    except:
        return{}#if we run into an issue we will return an empty dictionary
    

#now we are checking if they only inputted one argument
if len(sys.argv) == 2:#we are doing 2 becasue its name of file and the argument
    command = sys.argv[1]#it is in index one because the firs tone is the file name and we want input in the second spot
   #attempt to load teh file SAVED_DATA and it will give us a python dictionary of whats inside
    data = load_data(SAVED_DATA)

    #now we are checking if the command equals our three commands: save load list
    if command == "save":
        #once we type in save it will ask for a key
        key = input("Enter the key: ")
        #then we will store the save key inside SAVED DATA and then we will store inside the datq SAVED DATA with whtats inside
        data[key] = clipboard.paste()
        #and then we will call save data and rewrite the json file with what we put
        save_data("data.json", data)

    elif command == "load":
        key = input("Enter the key: ")
        if key in data:#if the key is in the data
            clipboard.copy(data[key])#if the key is in the data then we access the key and copy it to the clipboard
            print("Key copied to clipboard")
        else:
            print("Key not found")

    elif command == "list":
        #this will just give us all the keys in the json file
        print(data)
    #this second else statment is for passing only making one command
else:
    print("Please pass exactly one command")




















