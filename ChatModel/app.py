import chatModel

print('=================================================================================')
print('Say the chatbot for stop or enter exit')
print('=================================================================================')

while True:
  query=input('Ask something! : ')
  response=chatModel.ask(query,temperature=0.8 )     #0.8 more creative                     
  if(response=='exit'):
    break
  else:
    print(response)