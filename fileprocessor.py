from PyPDF2 import PdfReader

def pdf_to_text(file):
    reader = PdfReader(file)
    all_text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        all_text += text

    file.close()

    return all_text

def remove_private(text, words_to_remove):
    # Split the string into a list of words
    words = text.split()

    # Create a new list without the words to remove
    filtered_words = [word for word in words if word not in words_to_remove]

    # Join the filtered words back into a string
    filtered_text = ' '.join(filtered_words)

    return filtered_text