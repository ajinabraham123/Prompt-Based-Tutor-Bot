# 💬 Python LeetCode Helper Chatbot

### **Make-Up Assignment 1: Develop a Prompt-Based Tutor Bot**

---

## **1. Tool Selection**

The tool used for this project is **OpenAI GPT API** via the `openai` Python SDK. This tool allows the creation of a flexible and intelligent chatbot capable of providing detailed solutions and step-by-step guidance for Python-related coding problems.

---

## **2. Bot Concept and Subject Area**

### **Subject Area**:
- Python programming and LeetCode-style problem solving.

### **Bot Name**:
- **"Python LeetCode Helper"**

---

## **3. Define the Bot's Personality and Learning Goals**

### **Personality**:
- The bot is **friendly, patient, and knowledgeable**. It provides detailed explanations and helps users understand Python coding concepts interactively. The bot breaks down complex problems into smaller, digestible steps.

### **Learning Goals**:
1. **Problem Solving**:
   - Assist users in solving Python-related coding problems.
2. **Step-by-Step Guidance**:
   - Provide detailed, step-by-step solutions for coding challenges.
3. **Interactive Learning**:
   - Engage users with a conversational chatbot interface for a personalized learning experience.

---

## **4. Core Bot Features**

### **4.1 Subject Q&A Module**

- **Function**: Respond to Python coding questions with detailed explanations and code examples.
- **Details**:
  - Structured answers ranging from basic to advanced concepts.
  - Includes sample Python code snippets.

#### **Example**
- **Prompt**:
How do I find the maximum subarray sum in Python?

python
- **Bot Response**:
# Solution using Kadane's Algorithm:
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6
4.2 Step-by-Step Problem Solving with Hints
Function: Guide users through coding problems step-by-step with hints.
Details:
Breaks problems into smaller steps for clarity.
Provides hints to guide the user when stuck.
Example
Prompt:
css
Copy code
Write a Python function to check if a number is a palindrome.
Bot Response:
python
Copy code
# Step 1: Understand what a palindrome is.
# Step 2: Convert the number to a string for easy reversal.
# Step 3: Check if the reversed string matches the original.

# Code:
def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]



OPENAI_API_KEY=your_openai_api_key
Note: Replace your_openai_api_key with your actual OpenAI API key.

Step 3: Run the Chatbot
bash
streamlit run leetcode_chatbot.py
Step 4: Interact with the Bot
Open the URL provided by Streamlit and start chatting!
