# **SummarizeIt**
**Quick, Clear, Concise PDF Summaries in Seconds**

SummarizeIt is a simple web application built using Python, Streamlit, and LangChain with Google Gemini LLM (Large Language Model). The application allows users to upload PDF files and receive a concise summary of the content.

## **Features**
- Upload a PDF file and generate a brief summary in seconds.
- Powered by Google Gemini LLM via LangChain integration.
- Easy-to-use interface with Streamlit.

## **Getting Started**

Follow the instructions below to set up and run the application locally on your machine.

### **Prerequisites**
- Python 3.10
- Conda (for virtual environment management)
- A Google API key (for accessing Google Gemini LLM)

### **1. Set up the virtual environment**
First, create a virtual environment to isolate dependencies. You can create one using Conda:

```bash
conda create -p Venv python==3.10 -y
```

Activate the virtual environment (on Windows use `activate Venv`):

```bash
conda activate Venv
```

### **2. Install dependencies**
After activating the virtual environment, install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **3. Add your Google API Key**
To authenticate the application with Google Gemini LLM, paste your Google API key into a `.env` file in the root directory of your project. The `.env` file should look like this:

```bash
GOOGLE_API_KEY="your_google_api_key_here"
```

### **4. Run the application**
Once everything is set up, use the following command to run the application:

```bash
streamlit run app.py
```

This will launch the Streamlit app in your default browser, where you can upload a PDF and get a summarized version of it.

## **Project Structure**
```
SummarizeIt/
│
├── app.py                # Main application file
├── requirements.txt       # Dependencies
├── .env                   # API key for Google Gemini LLM
├── README.md              # Project documentation
└── Venv/                  # Virtual environment directory
```

## **Technologies Used**
- **Python**: The programming language used to develop the backend.
- **Streamlit**: A fast and lightweight library for building web applications.
- **LangChain**: Integration with LLMs for natural language processing.
- **Google Gemini LLM**: Google's large language model used for generating summaries.

## **Contributing**
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any ideas, suggestions, or bug reports are welcome!

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
