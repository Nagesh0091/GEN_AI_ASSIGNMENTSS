## Task 1: The Data Extractor

**Prompt:**

Read the text below and do two things:
1. Summarize it in a single sentence.
2. Extract the key details into a valid JSON object with the keys: product_name, release_date, screen_size, weight, base_ram, base_price, main_complaint.

Text:
"The new 'Starlight' laptop was released on October 26, 2024. It features a 14-inch OLED screen, weighs 2.5 lbs, and the base model with 16GB of RAM costs $1,299. The main complaint from early reviews is its short 6-hour battery life."


**Response:**

1. **Summary:** 
The newly released 14-inch Starlight laptop offers 16GB of RAM and an OLED screen for $1,299, but early reviewers are disappointed by its short 6-hour battery life.

2. **JSON Extraction:**
```json
{
  "product_name": "Starlight",
  "release_date": "October 26, 2024",
  "screen_size": "14-inch",
  "weight": "2.5 lbs",
  "base_ram": "16GB",
  "base_price": "$1,299",
  "main_complaint": "short 6-hour battery life"
}
```

---

## Task 2: The Code Generator

**Prompt:**

Write a Python function called calculate_average that takes a list of numbers as input and returns the average of those numbers. Handle an empty list by returning 0. Return only the code.

**Response:**

```python
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

---

## Task 3: The Code Translator

**Prompt:**

Convert the following Python code into JavaScript. Keep the same logic and function name. Return only the JavaScript code.

```python
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```


**Response:**

```javascript
function calculate_average(numbers) {
    if (!numbers || numbers.length === 0) {
        return 0;
    }
    const sum = numbers.reduce((acc, current) => acc + current, 0);
    return sum / numbers.length;
}
```

---

## Task 4: The Social Media Manager

**Prompt:**

Act as a witty and enthusiastic social media manager. Write a tweet announcing the 'Starlight' laptop, a 14-inch OLED laptop that weighs 2.5 lbs and starts at $1,299. The tweet must include exactly two emojis and the hashtag #TechLaunch.

**Response:**

Meet the Starlight laptop: 14 inches of gorgeous OLED goodness, a featherlight 2.5 lbs, and a price tag starting at just $1,299! ✨ Say hello to your new tech obsession. Grab yours today! 💻 #TechLaunch

---

