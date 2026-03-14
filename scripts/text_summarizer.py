def summarize_text(text):
    words = text.split()
    summary = " ".join(words[:20])
    return summary

if __name__ == "__main__":
    text = input("Enter text: ")
    print("Summary:", summarize_text(text))
