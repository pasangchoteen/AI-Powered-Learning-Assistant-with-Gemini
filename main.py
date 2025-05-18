import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Step 1: Configure Gemini Pro with your API key
# Replace "YOUR_API_KEY" with your actual Gemini Pro API key.  You'll need to obtain this from Google Cloud.
genai.configure(api_key=os.getenv('YOUR_API_KEY'))

# Step 2: Choose the Gemini Pro model
# We'll use the 'gemini-pro' model for this application.
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

# Step 3: Define the function to generate learning material
def generate_learning_material(topic, learning_style, output_type):
   """
   Generates learning material using the Gemini Pro model,
   with the potential to include relevant images.
   Args:
       topic: The topic of the learning material (e.g., "React JS").
       learning_style: The learning style (e.g., "visual", "auditory", "kinesthetic").
       output_type: The desired output type (e.g., "summary", "quiz", "examples").
   Returns:
       The generated learning material (text and potentially image URLs) as a string.
       Returns None on error.
   """
   # Step 4: Construct the prompt to request both text and images
   # We explicitly ask for images and specify the content type.
   prompt = f"Generate a {output_type} about {topic} tailored for a {learning_style} learner. Include relevant images to illustrate the points."

   try:
       # Step 5: Send the request to Gemini Pro
       # You might need to specify the model that supports image generation
       # and configure the response to include images.
       # The specific model and configuration will depend on your Gemini API setup.
       # For example, if using the Vertex AI SDK:
       # from google.cloud import aiplatform
       # model = aiplatform.preview.generative_models.GenerativeModel("gemini-2.0-flash-preview-image-generation")
       # response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
       # Or, if using the google-generative-ai library (ensure you're using a compatible version):
       # import google.generativeai as genai
       # model = genai.GenerativeModel('gemini-2.0-flash-preview-image-generation')
       # response = model.generate_content(prompt, generation_config={"response_modalities": ["TEXT", "IMAGE"]})


       # For this example, let's assume 'model' is already initialized
       # with a generative model that supports image generation.
       # If using the `google.generativeai` library, it might look like this:
       response = model.generate_content(prompt) # The model should be set up to handle image generation.

       # Step 6: Return the generated text and potentially image URLs
       # The exact way to access images from the response will depend on the SDK/API version.
       # For models that provide interleaved text and images, the response.text
       # might contain markdown for images (e.g., `![alt text](image_url)`).
       # You might need to parse the response to extract image URLs.
       return response.text
   except Exception as e:
       print(f"Error generating content: {e}")
       return None  # Handle errors gracefully
   
if __name__ == "__main__":
   # This block of code runs when you execute the Python script.
   # Step 7: Get user inputs
   # We ask the user for the topic, learning style, and output type.
   topic = input("Enter the learning topic: ")
   learning_style = input("Enter learning style (visual, auditory, kinesthetic): ")
   output_type = input("Enter desired output (summary, quiz, examples): ")
   # Step 8: Get resources (optional)
   resources = []
   while True:
       resource = input("Enter a resource (or type 'done' to finish): ")
       if resource.lower() == 'done':
           break
       resources.append(resource)
   # Step 9: Generate the learning material
   # We call the function we defined earlier to get the content from Gemini Pro.
   material = generate_learning_material(topic, learning_style, output_type)
   # Step 10: Display the generated material
   #  We check if material is None (indicating an error) before printing.
   if material:
       print("\nGenerated Learning Material:")
       print(material)
   else:
       print("Failed to generate learning material.") #error message