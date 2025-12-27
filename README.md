<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday!</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            color: #333;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 20px;
        }
        .photo-container {
            width: 100%;
            height: 300px;
            background: #eee;
            border-radius: 15px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 5px solid #fff;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .photo-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        h1 { color: #ff6b6b; margin-bottom: 10px; }
        p { font-size: 1.1rem; line-height: 1.6; color: #555; }
        .confetti { font-size: 2rem; margin: 10px 0; }
    </style>
</head>
<body>

    <div class="card">
        <div class="confetti">🎉 🎂 🎈</div>
        <h1>Happy Birthday!</h1>
        
        <div class="photo-container">
            <img src="https://via.placeholder.com/400x300?text=Insert+Our+Photo+Here" alt="Us">
        </div>

        <p>To my best friend,</p>
        <p>Wishing you a year filled with adventure, laughter, and success. Thanks for being an awesome part of my life!</p>
        
        <div style="margin-top: 20px; font-weight: bold; color: #ff6b6b;">
            - From Your Friend Mohan
        </div>
    </div>

</body>
</html>
