<!DOCTYPE html>
<html>
<head>
	<title>Number Guessing Game</title>
</head>
<body>
	<h1>Number Guessing Game</h1>
	<p>The Number Guessing Game is a simple command-line game in which the user tries to guess a randomly generated number within a specified range.</p>
    <h2>Requirements</h2>
<p>To play the Number Guessing Game, you need to have Python 3 installed on your computer. You can download Python 3 for free from the official Python website: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></p>

<h2>How to Play</h2>
<p>To play the game, open a terminal or command prompt and navigate to the directory where the number_guessing_game.py file is located. Then, run the following command:</p>

<pre><code>python number_guessing_game.py</code></pre>

<p>The game will prompt you to choose a difficulty level. You can choose from one of the following options:</p>

<ul>
	<li>Easy (range 0-20, 10 guesses, hint range of 5)</li>
	<li>Medium (range 0-50, 10 guesses, hint range of 10)</li>
	<li>Hard (range 0-500, 20 guesses, hint range of 20)</li>
	<li>Custom (you choose the range and number of guesses)</li>
</ul>

<p>After you choose a difficulty level, the game will generate a random number within the specified range and prompt you to make a guess. Enter your guess at the prompt and press Enter.</p>

<p>If your guess is too high or too low, the game will give you a hint and prompt you to guess again. If you make a repeated guess, the game will ask you to try again.</p>

<p>The game will continue until you correctly guess the random number, or until you run out of guesses (if you chose a difficulty level with a limited number of guesses). If you correctly guess the number, the game will print a congratulations message and tell you how many guesses it took you to win. If you run out of guesses, the game will reveal the correct number and tell you how many guesses you made.</p>
</body>
</html>