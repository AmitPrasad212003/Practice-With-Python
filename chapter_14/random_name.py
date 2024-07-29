import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        titlename = user_data["name"]["title"]
        firstname = user_data["name"]["first"]
        lastnane = user_data["name"]["last"]
        # userpicture = user_data["picture"]["medium"]
        # picturethumbnail = user_data["picture"]["thumnail"]

        return titlename , firstname,lastnane
    else:
        raise Exception("Failed to fetch user data")

def main():

    try : 
        titlename , firstname,lastname = fectch_random_user_freeapi()
        print(f"Name : {titlename} {firstname} {lastname} \n")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()