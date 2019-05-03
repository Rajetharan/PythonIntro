import os

def rename_files():
    file_list = os.listdir(r"/Users/Rajetharan/Downloads/prank")
    print(file_list)

    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)

    os.chdir(r"/Users/Rajetharan/Downloads/prank")

    new_path = os.getcwd()

    print("Current working directory is " + new_path)

    for i in file_list:
        print("Old Name - " + i)

        New_name = i.translate(None,"0123456789")

        print ("New Name - " + New_name)

        os.rename(i,New_name)
        
    os.chdir(saved_path)



rename_files()
