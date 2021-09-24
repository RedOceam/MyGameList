from django.core.management.utils import get_random_secret_key



def CreateNewSecretKey():
    f = open('secret-key.secret','w')
    new_key = get_random_secret_key()
    f.write(new_key)
    f.close()





if __name__ == "__main__":
    CreateNewSecretKey()
