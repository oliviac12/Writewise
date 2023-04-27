from django.shortcuts import render
from .models import Submission
from .forms import SubmissionForm
import openai

# Configure the OpenAI API key
openai.api_key = "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"

def index(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            original_text = form.cleaned_data['original_text']

            # Use ChatGPT to improve the text
            prompt = f"Proofread and rephrase the following text in a professional tone: {original_text}"
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.5)
            improved_text = response.choices[0].text.strip()

            # Save the original and improved texts to the database
            submission = Submission(original_text=original_text, improved_text=improved_text)
            submission.save()

            return render(request, 'writewise/result.html', {'original_text': original_text, 'improved_text': improved_text})
    else:
        form = SubmissionForm()

    return render(request, 'writewise/index.html', {'form': form})
