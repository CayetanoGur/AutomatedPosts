from dis import dis
from email import header
from enum import auto
import tweepy
import requests

#Mensaje que se va a mandar en el post
post = "el loop anda"
#Discord Lista de servidores y la autentidicacion de discord
server_list = ["https://discord.com/api/v9/channels/947604617598996554/messages",
             "https://discord.com/api/v9/channels/751604539182022780/messages",
             "https://discord.com/api/v9/channels/782077406533255187/messages"]
def twitter(post):
    api_key="Fz0O2bKWJNIVSu4mUCp1X00MT"
    api_secret_key="lSlVVhmnHR11IBMNiQyCYJjN04iGaAwZwik3hUqCUOXU39Qhhg"
    #bearerToken= "AAAAAAAAAAAAAAAAAAAAAFbNZgEAAAAAMOx1TrH8pwDC60e5YSiak9xcLIo%3DLR22JQF8yTrUDw16gSw9tORCSXrkilIGig2PnPVhFz5HWnwTQE"
    access_token= "1051116491406499840-QLdwB6PwKlu4D65poG0hzkmz0U2Bal"
    access_token_secret= "jsDK9Ran7CkjtutuoGlw5nRja01etPZXVYo3Ezp1MaqPC"

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials() #verifica si se hace la autentificacion con la api
        print("OK")
    except:
        print("Auth Error")
    
    try:
        api.update_status(post) #update post es hacer un tweet
        print("Post Done")
    except:
        print("Post Error")

def discord(post, server):
    #URL api server test del post de mensajes: 
    
    payload = {
        'content': post
    }
    header = {
        'authorization': "NjkyMzk1OTI3Mjg5NDYyODY1.X1wywQ.xizukOyjoRxDPvW2yAuQ3xscpmw"
        #este es el acces token universal de mi cuenta para hacer posteos en cualquer servidor
    }
    try:
        r_post = requests.post(server, data=payload, headers=header)
        print("post Done")
    except:
        print("Post Error")

def main():
    #twitter(post)
    #falta que me autoricen la cuenta para usar la api de twitter
    """
    for i in range(len(server_list)):
        srv = server_list[i]
        discord(post, srv)
    """
    """    
    Todo el codigo de twitter ya anda, falta ir agregando servidores a la lista, 
    lo saco para no mandar mensajes cada vez que pruebo el codigo.
    """

main()