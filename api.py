import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
from datetime import date


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model

def gemini(job_description):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        system_instruction= "Today is " + str(date.today()) + "."
                            "default is posted_days_ago: 0"
                            "Return the json of the job description with the following keys:"
                            "if no mention of freshman, sophomore, junior or senior then hiring_freshman: true "
                            "Also if graduations year includes 2028 then hiring_freshman: true. "  
                                                              
                            "list({"
                            "hiring_freshman: boolean, "
                            "posted_days_ago: int,"
                            "})"

        )

    response = model.generate_content(f"Job Description: {job_description}")

    return response.text

