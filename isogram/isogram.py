def is_isogram(string):
    mystring=string.lower().replace("-","").replace(" ","")
    count=0
    for char in mystring:
      if mystring.count(char)==1:
          count+=1
    if len(mystring)==count: 
        return True
    else:    
         return False    
