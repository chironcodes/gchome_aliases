from getpass import getuser
from os import walk
import json




def return_list_folders(your_path:str) -> list:
    # returns a list of folders in given path.
    # may act weird if you're not the root trying to access root-only folders
    return next(walk(your_path))[1] #[1] = only folders








if __name__ == "__main__":

    user = getuser()
    path = f'/home/{user}/.config'

    
    ggl = [x for x in return_list_folders(path) if x.__contains__("chrome")]

    if not ggl:
       raise ValueError(f"Chrome has no data stored in /home/{user}/.config")
    else:
        path = path+"/"+ggl[0]



    prfls = [x for x in return_list_folders(path) if x.__contains__("Profile ")]
    

    profile_dict={}

    for prfl in prfls:
        with open(f'{path}/{prfl}/Preferences') as json_file:
            pref_json = json.load(json_file)
            profile_dict[prfl] = pref_json['profile']['name']

    print(profile_dict)
    print(f"{len(profile_dict)} profiles identified. You want to rename any of them? \nProfile",end=' ')
    


    #google-chrome-stable --profile-directory="Profile n" 

