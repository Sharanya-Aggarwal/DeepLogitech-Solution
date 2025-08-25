This is my solution for the assignment to create a simple API that returns the latest 6 main stories from Time.com.

The Python script runs a local server on port 7000. When you visit http://localhost:7000/getTimeStories, it fetches the homepage, finds the main article links, and returns the top 6 headlines in JSON format. It only uses built-in Python modules and does not rely on any external libraries. To run this : Open Terminal and Run command : python Assignment_solution.py

OUTPUT is of this form:
<img width="1022" height="546" alt="image" src="https://github.com/user-attachments/assets/2c03488e-ab6c-460d-9ef1-aec8677dacbf" />

These are the main headlines. As the site has been upated, there was no latest-stories section as mentioned in Assignment hence , I used the main headlines and stories that were stored as static HTML and rendered first six queries.
In this I have no used Regex as required.
