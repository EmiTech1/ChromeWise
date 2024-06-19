# from io import StringIO
# import pandas as pd
# import os
# import openai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key

# # Read the CSV file (limiting to the first 100 rows)
# data = pd.read_csv(
#     "/home/webexpert/Downloads/intervals_294260005.csv", nrows=100)
# #print(type(data))

# prompt_template = """
# Given the following CSV file data:
# {data}

# Process the CSV file based on these rules:
# 1. Retrieve the value from the index column [0] and save it in the 'ESIID' column of the new CSV file.
# 2. If any column name contains 'start_date' or any column has a start date value smaller than another date column, split date and time into 'USAGE_DATE' and 'USAGE_START_TIME' columns.
# 3. If any column contains date and time fields, save time in 'USAGE_END_TIME' column if the date is less than the 'start_date' field.
# 4. Directly map columns named 'end_time' to the 'USAGE_END_TIME' column.
# 5. Aggregate data from columns containing values like 'total' or 'net' into the 'USAGE_KWH' column.
# 6. Save the processed data in CSV format.

# Ensure the 'end_date' column is omitted from the resulting CSV file.
# Provide the processed data in CSV format based on these rules.

# """
# # Format the prompt with the CSV data
# print(prompt_template)
# csv_data = data.to_csv(index=False)
# formatted_prompt = prompt_template.format(data=csv_data)
# #print(formatted_prompt)

# # Function to get response from OpenAI


# def get_openai_response(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "You are a data processing assistant."},
#                   {"role": "user", "content": prompt}],
#         max_tokens=1500,
#         temperature=0
#     )
#     return response.choices[0].message['content'].strip()


# # Get the response from OpenAI
# response = get_openai_response(formatted_prompt)
# print(response)

# # Parse the response and convert to DataFrame
# processed_data = pd.read_csv(StringIO(response))

# # Save the processed data to a new CSV file
# output_path = "/home/webexpert/Downloads/llm_csv.csv"
# processed_data.to_csv(output_path, index=False)

# print(f"Processed data has been saved to {output_path}")





from io import StringIO
import pandas as pd
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Function to process CSV data in chunks
def process_csv_chunks(csv_file_path, chunk_size=100):
    # Initialize an empty list to accumulate processed data
    processed_chunks = []

    # Read CSV in chunks
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
        # Format the prompt with the current chunk
        prompt_template = """
        Given the following CSV file data:
        {data}

        Process the CSV file based on these rules:
        1. Retrieve the value from the index column [0] and save it in the 'ESIID' column of the new CSV file.
        2. If any column name contains 'start_date' or any column has a start date value smaller than another date column, split date and time into 'USAGE_DATE' and 'USAGE_START_TIME' columns.
        3. If any column contains date and time fields, save time in 'USAGE_END_TIME' column if the date is less than the 'start_date' field.
        4. Directly map columns named 'end_time' to the 'USAGE_END_TIME' column.
        5. Aggregate data from columns containing values like 'total' or 'net' into the 'USAGE_KWH' column.
        6. Save the processed data in CSV format.

        Ensure the 'end_date' column is omitted from the resulting CSV file.
        Provide the processed data in CSV format based on these rules.
        """

        # Format the prompt with the CSV data
        csv_data = chunk.to_csv(index=False)
        formatted_prompt = prompt_template.format(data=csv_data)
        print(formatted_prompt)

        # Get the response from OpenAI
        response = get_openai_response(formatted_prompt)

        # Parse the response and convert to DataFrame
        processed_data = pd.read_csv(StringIO(response))

        # Append processed chunk to the list
        processed_chunks.append(processed_data)

    # Concatenate all processed chunks into a single DataFrame
    processed_data_all = pd.concat(processed_chunks, ignore_index=True)

    return processed_data_all

# Function to get response from OpenAI
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data processing assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0
    )
    return response.choices[0].message['content'].strip()

# Main script
if __name__ == "__main__":
    csv_file_path = "/home/webexpert/Downloads/intervals_294260005.csv"
    processed_data = process_csv_chunks(csv_file_path)

    # Save the processed data to a new CSV file
    output_path = "/home/webexpert/Downloads/llms_csv.csv"
    processed_data.to_csv(output_path, index=False)

    print(f"Processed data has been saved to {output_path}")

