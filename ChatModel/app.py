import chatModel

while True:
  query=input('Ask something! : ')
  if(query=='exit'):
    break
  else:
    response=chatModel.ask(query,temperature=0.8 )     #0.8 more creative
    print(response)  