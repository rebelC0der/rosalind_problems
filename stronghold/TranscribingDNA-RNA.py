def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


print(transcription("GATGGAACTTGACTACGTAAATT"))
