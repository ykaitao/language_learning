# %%
from langdetect import detect
from googletrans import Translator
from nltk.translate.bleu_score import sentence_bleu


# %%
def detect_language(text):
    """This function detects the language of the given text. Args: text: The text to detect the language of. Returns: A string representing the detected language code"""
    try:
        language = detect(text)
    except:
        language = "Unknown"
    return language


# %%


def evaluate_translation_quality(original_text, translated_text):
    """
    This function evaluates the quality of a translated text.

    Args:
        original_text: The original text.
        translated_text: The translated text.

    Returns:
        A numeric score representing the translation quality (higher is better)
    """
    # Choose a suitable translation quality evaluation metric here
    # Some options include BLEU score, METEOR, ROUGE-L, etc.
    # For example, using BLEU score:
    score = sentence_bleu([original_text.split()], translated_text.split())
    return score


# %%
original_text = "Hola! ¿Cómo estás?"
translated_text = "Hello! How are you?"

# %%
detected_language = detect_language(original_text)
print(f"Detected language: {detected_language}")
translation_quality = evaluate_translation_quality(original_text, translated_text)
print(f"Translation quality score: {translation_quality}")

# %%
