import tokenizer
import stopWordRemover
import stemmer

tokenizer.tokenizeDocuments()
stopWordRemover.remove_DocumentStopword()
stemmer.stemDocuments()
stemmer.createIndexList()

print("Successfully indexed documents!!")
