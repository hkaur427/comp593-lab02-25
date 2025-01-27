def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = { 
        'full_name':'Harmanpreet kaur',
            'student_id': '10362758',
            'pizza_topping':
            ['CHEESE',
             'PINEAPPLES',
                'CAPCICUM',]
                }
     'movies':[
                'action_movies':'the dark knight',
                'horror_name': 'halloween', 
                'drama_movie': 'one fast move',
                'funny_movie': 'jackpot',  
                }

    # TODO: Step 3 - Add another movie to the data structure
    another_movie ={
        'sad_movie':'beautiful boy in the town'
      }
      about_me["movies"].append(another_movie)
      print(about_me)

    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    first_name = full_name.split()[0]
    print(f"my name is {full_name},but you can call me mam {first_name}.")
    print(f"my student ID is {about_me['student_id']}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()