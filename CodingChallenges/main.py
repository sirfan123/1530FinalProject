import json
from flask import Flask, url_for, redirect, render_template, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def default():
    if request.method == "POST":
        # Get data from the form
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        
        # Create a dictionary to store the data
        person_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        
        # Read the current data from the database
        with open("database.json", "r+") as db_file:
            # Load the data in the JSON file
            data = json.load(db_file)
            # Append the new data
            data.append(person_data)
            # Move the cursor to the beginning of the file
            db_file.seek(0)
            # Write the updated data back to the file
            json.dump(data, db_file, indent=4)
        
    
    # If it's a GET request, just render the form page
    return render_template("index.html")

@app.route('/learning_paths')
def play_details():
    return render_template("paths.html") 

if __name__ == "__main__":
    app.run(debug=True)
