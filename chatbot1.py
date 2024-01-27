#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Seprate Space to import modules and libraries
import random
import datetime
import calendar
import requests
import tkinter as tk
from tkinter import messagebox
import math
from PIL import Image
from io import BytesIO
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#A Predefined set of greetings to be used to greet the user to the program
greetings = ["hi", "hello", "hey","Hello!"]

greetings_reply=["Hi there!", "Hey!", "Greetings!How can i help you?", "Hi, how can I assist you?", "Nice to see you!","Hey, what can I do for you?","Hi, I'm here to help!",
    "Hey, ready to chat?","Hi, what's on your mind?","Hey, how can I make your day better?", "Hello! What can I do to brighten your day?","Hello, how can I be of service today?",
    "Hi, ready to dive into a chat?","Hey! Welcome to ChatWiz. How can I help you today?"]

responses = {
    'how are you': "I'm just a bot, but I'm here to help!",
    'tell me a joke': None,  # We'll handle this case separately
    'what can you do': "I can provide witty replies and perform simple commands.",
    'thank you': "You're welcome! Feel free to ask more questions.",
}
#A Set of Predefined jokes to be used by the chat bot
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the golgappa go to school? To get aloo-teducation!",
    "Why don't Indian cricketers open a door? Because they fear getting bowled over!",
    "Why was the tomato blushing? Because it saw the salad dressing!",
    "Why did the Indian bread go to therapy? Because it had too many naan-issues!",
    "Why don't we tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "What did the masala say to the spice? 'You're the best thing that ever happened to me!'",
    "Why did the dosa refuse to play hide and seek? Because it couldn't masquerade as anything else!",
    "Why did the traffic light turn red? Because it saw the car coming to a complete stop!",
    "Why was the math book sad? Because it had too many problems!",
    "Why was the cellphone stressed? It couldn't find a good network connection!",
    "Why did the Indian dad bring a ladder to the bar? He heard the drinks were on the house!",
    "Why did the laptop go to therapy? Because it had too many tabs open!",
    "Why did the cycle apply for a job? It wanted to get its life back on track!",
    "Why did the elephant bring a suitcase to the zoo? It wanted to pack its trunk!",
    "Why was the calendar always stressed? It had too many dates to keep up with!",
    "Why did the mango refuse to go to school? It didn't want to be a pulp fiction novel!",
    "Why don't Indian superheroes work out? They're already outstanding!",
    "Why did the coconut go to the party? It wanted to be a 'cool nut'!",
    "Why did the scarecrow win an award? Because it was outstanding in its field!",
    "Why don't Indian parents trust atoms? They make up everything!",
    "Why did the lamp go to school? To get a little brighter!",
    "Why don't Indian engineers play hide and seek? Because good players are always in high demand!",
    "Why did the smartphone enroll in school? It wanted to improve its apps!",
    "Why was the potato confused? Because it couldn't make 'heads' or 'tails' of things!",
    "Why don't Indian cricketers use Facebook? They are afraid of getting caught behind!",
    "Why don't Indian spices gossip? They curry favor!",
    "Why did the umbrella break up with the raincoat? It wanted a little space!",
    "Why did the Indian bread apply for a job? It wanted to earn some 'roti'!",
    "Why don't Indian parents believe in aliens? Because they've never seen their kids clean their rooms!",
    "Why did the tea go to therapy? It was steeped in stress!",
    "Why did the pen enroll in school? It wanted to improve its handwriting!",
    "Why was the computer cold? It left its Windows open!",
    "Why did the pencil get an award? Because it had the 'write' stuff!",
    "Why did the butter go to therapy? It had too many issues to spread around!",
    "Why did the onion become a comedian? It had layers of jokes!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the potato run for office? Because it wanted to be a 'common tater'!",
    "Why don't Indian ghosts like to go out in the rain? They're afraid of phantasma-goria!",
    "Why did the book go to the gym? To get a good cover story!",
    "Why don't Indian parents trust stairs? Because they're always up to something!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't Indian couples go to the gym? Because some relationships don't work out!",
    "Why did the smartphone go to school? It wanted to improve its apps!",
    "Why was the math book sad? It had too many problems!",
    "Why did the scarecrow win an award? Because it was outstanding in its field!",
    "Why did the golgappa go to school? To get aloo-teducation!",
    "Why did the laptop go to therapy? Because it had too many tabs open!",
    "Why did the traffic light turn red? Because it saw the car coming to a complete stop!",
    "Why did the cycle apply for a job? It wanted to get its life back on track!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.",
    "What do you call a fake noodle? An impasta!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why don't oysters donate to charity? Because they are shellfish.",
    "I used to be a baker, but I couldn't make enough dough.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How does a penguin build its house? Igloos it together!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "I'm friends with all electricians. We have great current connections.",
    "What's orange and sounds like a parrot? A carrot!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why was the math book sad? It had too many problems.",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "What do you call a bear with no teeth? A gummy bear!",
    "How do you organize a space party? You 'planet'!",
    "What do you call a snowman with a six-pack? An abdominal snowman.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "I used to play piano by ear, but now I use my hands.",
    "How do you organize a space party? You 'planet'!",
    "I used to be a baker, but I couldn't make enough dough.",
    "What do you call a sleeping bull? A bulldozer!",
    "Why don't eggs tell jokes? Because they might crack up.",
    "What do you call a fake noodle? An impasta!",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "I'm friends with all electricians. We have great current connections.",
    "What do you call a pile of cats? A meowtain!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "I'm friends with all electricians. We have great current connections.",
    "What's orange and sounds like a parrot? A carrot!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It's a shame they'll never meet.", ]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Quotes
inspirational_quotes = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Your time is limited, don't waste it living someone else's life.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", "Jordan Belfort"),
    ("The road to success and the road to failure are almost exactly the same.", "Colin R. Davis"),
    ("You are never too old to set another goal or to dream a new dream.", "C.S. Lewis"),
    ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
    ("The only person you are destined to become is the person you decide to be.", "Ralph Waldo Emerson"),
    ("Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", "Christian D. Larson"),
    ("The harder you work for something, the greater you'll feel when you achieve it.", "Anonymous"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("The only limit to our realization of tomorrow will be our doubts of today.", "Franklin D. Roosevelt"),
    ("Success is walking from failure to failure with no loss of enthusiasm.", "Winston Churchill"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("You are the master of your fate, you are the captain of your soul.", "William Ernest Henley"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", "Mark Zuckerberg"),
    ("Do not wait to strike till the iron is hot; but make it hot by striking.", "William B. Sprague"),
    ("You are never too old to set another goal or to dream a new dream.", "C.S. Lewis"),
    ("The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", "Joel Brown"),
    ("Don't let yesterday take up too much of today.", "Will Rogers"),
    ("The only limit to our realization of tomorrow will be our doubts of today.", "Franklin D. Roosevelt"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("I want to be the very best, like no one ever was.", "Ash Ketchum - Pokémon"),
    ("No one knows what the future holds. That's why its potential is infinite.", "Rintarou Okabe - Steins;Gate"),
    ("The world's not perfect, but it's there for us trying the best it can. That's what makes it so damn beautiful.", "Roy Mustang - Fullmetal Alchemist"),
    ("Sometimes people are beautiful. Not in looks, not in what they say, just in what they are.", "Mikasa Ackerman - Attack on Titan"),
    ("The only one who can beat me is me.", "Yugi Mutou - Yu-Gi-Oh!"),
    ("It's not the face that makes someone a monster; it's the choices they make with their lives.", "Naruto Uzumaki - Naruto"),
    ("I don't want to conquer anything. I just think the guy with the most freedom in this whole ocean... that's the Pirate King!", "Monkey D. Luffy - One Piece"),
    ("In our society, letting others find out that you're a nice person is a very risky move. It's extremely likely that someone would take advantage of that.", "Hitagi Senjougahara - Bakemonogatari"),
    ("If you have time to think of a beautiful end, then live beautifully until the end.", "Sakata Gintoki - Gintama"),
    ("I am the hope of the universe. I am the answer to all living things that cry out for peace.", "Goku - Dragon Ball Z"),
    ("It's not the face that makes someone a monster; it's the choices they make with their lives.", "Naruto Uzumaki - Naruto"),
    ("No one knows what the future holds. That's why its potential is infinite.", "Rintarou Okabe - Steins;Gate"),
    ("Even if I'm weak, I need to move forward!", "Natsu Dragneel - Fairy Tail"),
    ("When you have to save someone, they're usually in a scary situation. Calm people down first.", "Erza Scarlet - Fairy Tail"),
    ("I'm not gonna run away, I never go back on my word! That's my nindo: my ninja way!", "Naruto Uzumaki - Naruto"),
    ("No matter how deep the night, it always turns to day, eventually.", "Brook - One Piece"),
    ("I don't want to conquer anything. I just think the guy with the most freedom in this whole ocean... that's the Pirate King!", "Monkey D. Luffy - One Piece"),
    ("I'm not gonna run away, I never go back on my word! That's my nindo: my ninja way!", "Naruto Uzumaki - Naruto"),
    ("Sometimes people are beautiful. Not in looks, not in what they say, just in what they are.", "Mikasa Ackerman - Attack on Titan"),
    ("It's not the face that makes someone a monster; it's the choices they make with their lives.", "Naruto Uzumaki - Naruto"),
    ("I don't want to conquer anything. I just think the guy with the most freedom in this whole ocean... that's the Pirate King!", "Monkey D. Luffy"),
    ("I'm gonna be the world's best swordsman! The greatest swordsman in the world! The Pirate Hunter, Roronoa Zoro!", "Roronoa Zoro"),
    ("No matter how deep the night, it always turns to day, eventually.", "Brook"),
    ("I don't want to live a thousand years. If I just live through today, that'll be enough.", "Portgas D. Ace"),
    ("Inherited Will, the swelling of the changing times, and the dreams of people never cease. As long as people continue to pursue the meaning of freedom, these things will never cease.", "Gold Roger"),
    ("I've set myself to become the King of the Pirates...and if I die trying...then at least I tried!", "Monkey D. Luffy"),
    ("It's not a crime if no one sees you do it.", "Nami"),
    ("I don't wanna conquer anything. It's just the nature of my pirate blood.", "Monkey D. Luffy"),
]

def inspirational_quote():
    random_quote = random.choice(inspirational_quotes)
    quote = random_quote[0]
    author = random_quote[1]
    print(f'"{quote}" - {author}')



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Function for Password Genrator
def generate_secure_password(name, birthdate, city):
    # Define a list of special characters and numbers
    special_characters = "!@#$%^&*()_-+=<>?"
    numbers = "0123456789"

    # Shuffle the special characters and numbers
    characters = list(special_characters)
    x=random.choice(characters)
    y=random.choice(numbers)

    # Combine user inputs with shuffled characters
    password = name + x + birthdate + y + city

    # Ensure the password is not longer than 17 characters
    if len(password) > 18:
        password = password[:18]

    return password


def password():
    # Get user inputs
    name = input("Enter your name: ")
    birthdate = input("Enter your birthdate (MMDDYYYY): ")
    city = input("Enter your city name: ")

    # Generate and display the secure password
    secure_password = generate_secure_password(name, birthdate, city)
    print("Your secure password is:", secure_password)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Movie Review
def get_movie_details(movie_name, api_key):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": movie_name,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])
    else:
        return None

# Function to display movie details in a pleasant format
def display_movie_details(movie_data):
    if movie_data:
        print(f"Movie Details for '{movie_data[0]['title']}':")
        print("-----------------------------------------------------------------------")
        print(f"Title: {movie_data[0]['title']}")
        print(f"Release Date: {movie_data[0]['release_date']}")
        print(f"Overview: {movie_data[0]['overview']}")
        print(f"Vote Average: {movie_data[0]['vote_average']}")
        print(f"Vote Count: {movie_data[0]['vote_count']}")
        print("-----------------------------------------------------------------------")
    else:
        print("Movie not found or API request failed. Please try again.")

# Main chatbot loop
def movie_review():
    api_key = "####################################"

    while True:
        movie_name = input("Please enter the name of the movie (or 'exit' to quit): ").strip()

        if movie_name.lower() == 'exit':
            print("Goodbye!")
            break

        movie_data = get_movie_details(movie_name, api_key)
        display_movie_details(movie_data)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def facts():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': '###############################'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#calculator functionality
def run_calculator():
    # Create a main calculator window
    calculator = tk.Tk()
    calculator.title("Simple Calculator")

    # Entry field to display and input numbers
    entry = tk.Entry(calculator, width=30)
    entry.grid(row=0, column=0, columnspan=4)

    # Function to handle button clicks and update the entry field
    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))

    # Function to perform calculations and display the result
    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create buttons for numbers and operations
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3), ('.', 4, 0),
        ('C', 4, 4), ('=', 4, 2)  # Moved '=' button to the end
    ]

    for (text, row, col) in buttons:
        if text == '=':
            tk.Button(calculator, text=text, padx=20, pady=20, command=calculate).grid(row=row, column=col)
        else:
            tk.Button(calculator, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

    def open_scientific_calculator():

        scientific_calculator = tk.Toplevel(calculator)
        scientific_calculator.title("Scientific Calculator")

        entry_scientific = tk.Entry(scientific_calculator, width=30)
        entry_scientific.grid(row=0, column=0, columnspan=6)

        def button_click_scientific(number):
            current = entry_scientific.get()
            entry_scientific.delete(0, tk.END)
            entry_scientific.insert(0, current + str(number))

        def calculate_scientific():
            try:
                result = eval(entry_scientific.get())
                entry_scientific.delete(0, tk.END)
                entry_scientific.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))

        scientific_buttons = [
            ('sin', math.sin), ('cos', math.cos), ('tan', math.tan),
            ('log', math.log10), ('ln', math.log),
            ('sqrt', math.sqrt)
        ]

        row, col = 1, 0
        for (text, func) in scientific_buttons:
            tk.Button(scientific_calculator, text=text, padx=20, pady=20, command=lambda f=func: button_click_scientific(f(entry_scientific.get()))).grid(row=row, column=col)
            col += 1
            if col == 6:
                col = 0
                row += 1

        tk.Button(scientific_calculator, text="=", padx=20, pady=20, command=calculate_scientific).grid(row=4, column=2)

    tk.Button(calculator, text="Scientific Calculator", padx=20, pady=20, command=open_scientific_calculator).grid(row=5, column=0, columnspan=4)

    calculator.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions to show time , date and calender
def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def show_date():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    return f"Today's date is {current_date}"

def show_calendar(year, month):
    cal = calendar.month(year, month)
    return f"Here's the calendar for {calendar.month_name[month]} {year}:\n{cal}"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PHONE NUMBER VERIFICATION
def search_mobile_number_info(mobile_number):

    api_url = f"http://apilayer.net/api/validate?access_key=###################&number={mobile_number}&country_code=IN&format=1"

    try:

        response = requests.get(api_url)

        if response.status_code == 200:

            data = response.json()
            return data
        else:
            return {"error": "Failed to fetch data from the API"}
    except Exception as e:
        return {"error": str(e)}

def main_phone_verify():
    mobile_number = input("Enter the mobile number to search: ")
    result = search_mobile_number_info(mobile_number)

    if "error" in result:
        print("An error occurred:", result["error"])
    else:
        print("Mobile number information:")
        print("Mobile Number:", result.get("international_format", "N/A"))
        print("Location:", result.get("location", "N/A"))
        print("Country Code:", result.get("country_code", "N/A"))
        print("Valid:", result.get("valid", "N/A"))
        print("Service Provider:", result.get("carrier", "N/A"))
        print("Line Type:", result.get("line_type", "N/A"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#news api
def get_top_news(API_KEY):
    api_url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&country=us'

    try:

        response = requests.get(api_url)
        if response.status_code == 200:

            news_data = response.json()

            articles = news_data['articles'][:10]

            news_message = "\nTop 10 News Headlines:\n\n"
            for idx, article in enumerate(articles, start=1):
                title = article['title']
                content = article['content']  # Use 'content' for longer summary
                if content:
                    news_message += f"{idx}. {title}\n"
                    news_message += f"   Summary: {content}\n"
                    news_message += "=" * 50 + "\n"

            return news_message
        else:
            return f"Error: Unable to fetch news. Status code {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Weather functionality
def get_weather_info(city):
    api_key = "#######################"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result = f"Weather in {city}:\n"
            result += f"Temperature: {temperature}°C\n"
            result += f"Description: {description}\n"
            result += f"Humidity: {humidity}%\n"
            result += f"Wind Speed: {wind_speed} m/s"

            return result
        else:
            return "Sorry, I couldn't find weather information for that location."
    except Exception as e:
        return f"An error occurred: {str(e)}"
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#NASA API FUNCTION
nasa_api_key = "5G5Ho9kuGoGO8sHC6WX2tDO0745V8VHz3KLMmDhs"


def nasa_chatbot():
    while True:
        print("\nNASA Chatbot Menu:")
        print("1. Astronomy Picture of the Day (APOD)")
        print("2. Mars Rover Photos")
        print("3. ISS Information")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            get_apod()
        elif choice == '2':
            get_mars_rover_photos()
        elif choice == '3':
            get_iss_information()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
    response = requests.get(url)
    data = response.json()

    print("Astronomy Picture of the Day (APOD)")
    print(f"Title: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Explanation: {data['explanation']}")

    image_url = data['url']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()



def get_mars_rover_photos():
    rover_name = input("Enter the Mars rover name (Curiosity, Opportunity, or Spirit): ")
    sol = input("Enter the Martian sol (e.g., 1000): ")

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos"
    params = {
        'api_key': nasa_api_key,
        'sol': sol
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'photos' in data:
        photos = data['photos']

        # Display the first 5 images using PIL
        for i in range(min(5, len(photos))):
            photo = photos[i]
            print(f"Image ID: {photo['id']}")
            print(f"Earth Date: {photo['earth_date']}")
            print(f"Image URL: {photo['img_src']}")

            image_url = photo['img_src']
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.show()

        # Provide links to the rest of the images
        if len(photos) > 5:
            print(f"\n{len(photos) - 5} more images are available. Here are their URLs:")
            for i in range(5, len(photos)):
                photo = photos[i]
                print(f"Image ID: {photo['id']}")
                print(f"Earth Date: {photo['earth_date']}")
                print(f"Image URL: {photo['img_src']}")
    else:
        print("No photos found for the given rover and sol.")


def get_iss_information():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    print("International Space Station (ISS) Information")
    print(f"Timestamp: {data['timestamp']}")
    print(f"Latitude: {data['iss_position']['latitude']}")
    print(f"Longitude: {data['iss_position']['longitude']}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_response(user_input):
    if user_input.lower() in greetings:
        return random.choice(greetings_reply)
    elif 'tell me a quote' in user_input.lower():
        return inspirational_quote()
    elif 'open calculator' in user_input.lower():
        return run_calculator()
    elif 'password generator' in user_input.lower():
        return password()
    elif 'show time'in user_input.lower():
        return show_time()
    elif 'show date' in user_input.lower():
        return show_date()
    elif 'show weather' in user_input.lower():
        city = input("Enter the name of your city:")
        weather_info = get_weather_info(city)
        print(weather_info)
    elif 'tell me a joke' in user_input.lower():
        return random.choice(jokes)
    elif 'show calendar' in user_input.lower():
        mon=int(input("Enter the month:"))
        year_in=int(input("Enter the year:"))
        return show_calendar(mon,year_in)
    elif 'tell me a fact' in user_input.lower():
        return facts()
    elif 'verify a number for me' in user_input.lower():
        return main_phone_verify()
    elif 'give me a movie review' in user_input.lower():
        return movie_review()
    elif 'tell me news' in user_input.lower():
        API_KEY_NEWS = '###################################'
        news_message = get_top_news(API_KEY_NEWS)
        print(news_message)
    elif 'open nasa menu' in user_input.lower():
        return nasa_chatbot()
    for command, response in responses.items():
        if command in user_input.lower():
            return response

    return "I'm sorry, I didn't quite catch that. Could you please rephrase?"

print("Welcome to ChatWiz! ")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatWiz: Goodbye! Have a great day.")
        break

    response = get_response(user_input)
    print("ChatWiz:", response)
