import os
import openai
import customtkinter as ctk
from tkinter import messagebox



# GPT-3 API call
def get_project_idea(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if openai.api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not found. Please set it and try again.")

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['choices'][0]['message']['content']

# Generate project idea
def generate():
    try:
        prompt = "I want to create a idea for you"
        language = language_dropdown.get()
        prompt += "The programming language is " + language + "."
        difficulty = difficulty_value.get()
        prompt += "The difficulty is " + difficulty + "."

        if checkbox1.get():
            prompt += "The project should include a database."
        if checkbox2.get():
            prompt += "The project should include an API."

        print(prompt)

        answer = get_project_idea(prompt)
        print(answer)
        result.delete("1.0", "end")
        result.insert("1.0", answer)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create a CTk object
root = ctk.CTk()
root.geometry("750x500")
root.title("Idea Generator")

# Set the theme
ctk.set_appearance_mode("light")

# Create the widgets
title_label = ctk.CTkLabel(root, text="Idea Generator", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(pady=(40, 20), padx=10)

# Create the widgets
frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

# Create the widgets
langguage_frame = ctk.CTkFrame(frame)
langguage_frame.pack(padx=100, pady=(20, 5), fill="x")
language_label = ctk.CTkLabel(langguage_frame, text="Programming Language", font=ctk.CTkFont(weight='bold'))
language_label.pack()

# Create a Combobox
language_dropdown = ctk.CTkComboBox(langguage_frame, values=["Python", "JavaScript", "Java", "C++", "C#", "PHP", "Ruby"])
language_dropdown.pack(pady=10)

# Create a frame
difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")

# Create a label
difficulty_label = ctk.CTkLabel(difficulty_frame, text="Difficulty", font=ctk.CTkFont(weight='bold'))
difficulty_label.pack()

# Create a StringVar object
difficulty_value = ctk.StringVar(value="Easy")

# Create the radio buttons
radiobutton1 = ctk.CTkRadioButton(difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)

radiobutton2 = ctk.CTkRadioButton(difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)

radiobutton3 = ctk.CTkRadioButton(difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)

# Create a frame
features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")

# Create a label
features_label = ctk.CTkLabel(features_frame, text="Features", font=ctk.CTkFont(weight='bold'))
features_label.pack()

# Create the checkboxes
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

# Create a button
button = ctk.CTkButton(frame, text="Generate", font=ctk.CTkFont(size=20, weight="bold"), command=generate)
button.pack(padx=100, fill='x', pady=(5, 20))

# Create a textbox
result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15, weight="bold"))
result.pack(fill="x", padx=100, pady=10)

# Start the main loop
root.mainloop()
