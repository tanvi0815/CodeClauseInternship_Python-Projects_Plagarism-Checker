from difflib import SequenceMatcher

def text_similarity(text1, text2):
    # Calculate the similarity ratio between two texts
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio

def check_plagiarism(file1_path, file2_path, threshold=0.8):
    # Read the contents of the files
    with open(file1_path, 'r', encoding='utf-8') as file1:
        text1 = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        text2 = file2.read()

    # Check similarity between the two texts
    similarity_ratio = text_similarity(text1, text2)

    # Compare similarity ratio with the threshold
    if similarity_ratio >= threshold:
        print(f"Plagiarism detected! Similarity ratio: {similarity_ratio:.2f}")
    else:
        print(f"No plagiarism detected. Similarity ratio: {similarity_ratio:.2f}")

if __name__ == "__main__":
    # Specify the paths to the files you want to compare
    file1_path = "file1.txt"
    file2_path = "file2.txt"

    # Set a threshold for similarity (adjust as needed)
    similarity_threshold = 0.8

    # Check plagiarism between the two files
    check_plagiarism(file1_path, file2_path, similarity_threshold)
