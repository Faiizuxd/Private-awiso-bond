from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home Page with Password + Search Field
index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Gangster</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet" />
  <style>
    body {
      margin: 0;
      font-family: 'Be Vietnam Pro', sans-serif;
      background: #060606;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }

    form {
      background: #111;
      padding: 20px;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 0 10px #000;
    }

    input[type="search"], input[type="password"] {
      padding: 10px 15px;
      border-radius: 5px;
      border: 1px solid #444;
      background: #222;
      color: #fff;
      width: 250px;
    }

    button {
      background: #3772ff;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
    }

    button:hover {
      background: #5587ff;
    }

    .msg {
      margin-top: 20px;
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <form method="POST">
    <input type="password" name="password" placeholder="Enter Password..." required />
    <input type="search" name="searchBox" placeholder="Type 'Convo' to search..." required />
    <button type="submit">Search</button>
  </form>

  {% if message %}
    <div class="msg">{{ message }}</div>
  {% endif %}

</body>
</html>
'''

# Server List Page
convo_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Convo Results</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet" />
  <style>
    body {
      margin: 0;
      background: #060606;
      font-family: 'Be Vietnam Pro', sans-serif;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 40px 20px;
    }

    h1 {
      margin-bottom: 30px;
      font-size: 2rem;
      color: #5ff;
      text-shadow: 0 0 10px #0ff;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      width: 100%;
      max-width: 900px;
    }

    .card {
      background: #1b1b1b;
      border-radius: 15px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      box-shadow: 0 0 10px rgba(0,255,255,0.1);
      position: relative;
    }

    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 20px rgba(0,255,255,0.3);
    }

    .card img {
      width: 100%;
      height: 180px;
      object-fit: cover;
    }

    .card-title {
      padding: 15px;
      font-size: 1.2rem;
      font-weight: 600;
      text-align: center;
      color: #5ff;
      text-shadow: 0 0 5px #0ff;
    }

    .click-icon {
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #00ffff;
      color: #0ff;
      font-size: 1rem;
      padding: 5px 7px;
      border-radius: 6px;
      text-shadow: 0 0 5px #0ff;
      animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
      0% { box-shadow: 0 0 5px #0ff; }
      50% { box-shadow: 0 0 15px #0ff; }
      100% { box-shadow: 0 0 5px #0ff; }
    }

    .social-icons {
      margin-top: 40px;
      display: flex;
      gap: 20px;
    }

    .social-icons a {
      color: #0ff;
      font-size: 24px;
      transition: transform 0.3s ease;
      text-shadow: 0 0 5px #0ff;
    }

    .social-icons a:hover {
      transform: scale(1.3);
      color: #5ff;
    }
  </style>
</head>
<body>
  <h1> Awiso Don <3</h1>
  <div class="cards">
    <div class="card" onclick="window.open('https://awiso-da-server.onrender.com/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://raw.githubusercontent.com/Faiizuxd/The_Faizu_dpz/refs/heads/main/8c4894ad1db8fee86a8b1537527eaed6.jpg" alt="Awiiso Server">
      <div class="card-title">Awiso Don</div>
    </div>

    <div class="card" onclick="window.open('https://awiso-1-page.onrender.com/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://raw.githubusercontent.com/Faiizuxd/The_Faizu_dpz/refs/heads/main/b1a8d231a6f3fe5a0fd525babb978712.jpg" alt="Awiiso 2.0">
      <div class="card-title">Awiiso 2.0</div>
    </div>

    <div class="card" onclick="window.open('https://entri-awiso-3.onrender.com/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://raw.githubusercontent.com/Faiizuxd/Free/refs/heads/main/1751743008340.jpg" alt="Awiiso Server 3.0">
      <div class="card-title">Still pending  </div>
    </div>
    
    <div class="card" onclick="window.open('https://www.facebook.com/The.Unbeatble.Stark', '_blank')">
      <img src="https://raw.githubusercontent.com/Faiizuxd/The_Faizu_dpz/refs/heads/main/2b572c81b74b0af04ff1f1b0e8f8db4a.jpg" alt="Contact">
      <div class="card-title">Contact Owner</div>
    </div>
  </div>

  <div class="social-icons">
    <a href="https://www.facebook.com/awa.so.ansarii" target="_blank"><i class="fab fa-facebook-f"></i></a>
    <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
    <a href="https://www.instagram.com/awaisinam204?igsh=dDh2bHplczhmOGJv" target="_blank"><i class="fab fa-instagram"></i></a>
  </div>
</body>
</html>
'''

# Route Logic
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password", "").strip()
        search = request.form.get("searchBox", "").strip().lower()
        if password != "#Awiiso#":
            return render_template_string(index_html, message="❌ Wrong password.")
        elif search == "convo":
            return render_template_string(convo_html)
        else:
            return render_template_string(index_html, message="❌ Type 'Convo' to search.")
    return render_template_string(index_html)

# Run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
