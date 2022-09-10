import turtle
import pandas as pd

# Use 'Exit' to display missed countries as csv file
# Use 'Finish' to display names of all countries on the map

screen= turtle.Screen()
screen.title("European Countries Game")
image= "europewithout-names4.gif"
screen.addshape(image)

turtle.shape(image)



country_data= pd.read_csv("europe_countries.csv")
country_data=country_data.set_index(keys='Country')

country_names=country_data.index.tolist()


guessed_countries=[]
while(len(guessed_countries)<48):

    answer_country = screen.textinput(title=f"{len(guessed_countries)}/47 Guess the Country",
                                    prompt="What is another countries name").title()

    found = False
    if answer_country == "Exit":
        break
    if answer_country=='Finish':
        break

    if answer_country in country_names:
        if answer_country in guessed_countries:
            continue
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('blue')
        t.setpos(int(country_data.x[answer_country]),int(country_data.y[answer_country]))
        t.write(answer_country,font=('Arial',9,'bold'))
        t.goto(0, 0)
        guessed_countries.append(answer_country)

missed_list=list()
missed_list= country_data.index.tolist()

for state in guessed_countries:
    missed_list.remove(state)

if answer_country =='Finish':
    for state in missed_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('blue')
        t.setpos(int(country_data.x[state]), int(country_data.y[state]))
        t.write(state, font=('Arial', 9, 'bold'))
        t.goto(0, 0)

df=pd.DataFrame(missed_list,columns=["Country"])
df.set_index("Country",inplace=True)
df.to_csv("missing.csv")


turtle.mainloop()

