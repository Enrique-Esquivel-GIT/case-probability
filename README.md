# case-probability
Interactive survival analysis simulation for case resolution times. Demonstrates conditional probabilities and median finish times with lognormal modeling. Built with HTML, JS, and Chart.js; suitable as a beginner-friendly project for learning programming, probability modeling, and web visualization.

# Case Resolution Probability Widget

**Interactive web tool to visualize and forecast case resolution times.**

This project models case resolution times using a **lognormal distribution**, allowing users to see:

- The **probability** that a case resolves by a target deadline (e.g., 3 months)
- The **most likely finish time (median)** given the current age of the case
- A **dynamic graph** showing how probabilities change as the case ages

It’s a beginner-friendly example of combining **probability modeling, conditional probability, and interactive web visualization**.

---

## Features

- Input slider to adjust **case age**
- Real-time update of:
  - Conditional probability of resolution
  - Median expected finish time
- Interactive chart of probability vs. case age
- Built with **HTML, JavaScript, and Chart.js** — no server required

---

## How to Run

1. Clone the repository or download the files
2. Open `index.html` in any modern web browser
3. Use the slider to explore probabilities and expected finish times

---

## Screenshot

![Screenshot](screenshot-placeholder.png)

> *(Will replace `screenshot-placeholder.png` with an actual screenshot of the widget)*

---

## Next Steps / Ideas

- Allow the user to **adjust the 80% target and 3-month deadline**
- Include **mean vs median** comparison for educational purposes
- Convert to a **Python web app** using Streamlit or Flask
- Add **confidence bands** for visualizing uncertainty
- Make mobile-friendly UI for better accessibility

---

## Keywords

probability, lognormal, conditional probability, survival analysis, interactive visualization, JavaScript, Chart.js, web widget
