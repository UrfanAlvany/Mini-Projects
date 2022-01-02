from tkinter import *
from tkinter import font


x = 2 
y = ""
player_1 = []
player_2 = []

def signal(n):
      global  x , y 
      global  player_1,player_2
      
      if n==1:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button1.config(text = y)
          x = x+1


      
      if n==2:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button2.config(text = y)
          x = x+1



      
      if n==3:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button3.config(text = y)
          x = x+1



      
      if n==4:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button4.config(text = y)
          x = x+1



      
      if n==5:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button5.config(text = y)
          x = x+1



      
      if n==6:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button6.config(text = y)
          x = x+1



      
      if n==7:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button7.config(text = y)
          x = x+1



      
      if n==8:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button8.config(text = y)
          x = x+1



  
      
      if n==9:
          if x%2 == 0:
              y = 'X'
              player_1.append(n)
              print(player_1)
            
          elif x%2!= 0:
                y = 'O'
                player_2.append(n)
                print(player_2)
          button9.config(text = y)
          x = x+1





window = Tk()
window.title('TacToe')



button1 = Button(window, width = 25, bg='red',height = 15 , command = lambda: signal(1))
button1.grid(row = 1, column = 1)

button2 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(2))
button2.grid(row = 1, column = 2)

button3 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(3))
button3.grid(row = 1, column = 3)

button4 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(4))
button4.grid(row = 4, column = 1)

button5 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(5))
button5.grid(row = 4, column =2,)

button6 = Button(window, width = 25, bg='red', height = 15 , command = lambda: signal(6))
button6.grid(row = 4, column = 3)


button7 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(7))
button7.grid(row = 8, column = 1)

button8 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(8))
button8.grid(row = 8, column = 2)


button9 = Button(window, width = 25,bg='red', height = 15 , command = lambda: signal(9))
button9.grid(row = 8, column = 3)

window.geometry("550x700")
window.config(bg="gray")







window.mainloop()