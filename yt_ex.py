# ! pip install yt_dlp
# ! pip install pydub

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir = "youtube/"
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()
# print(docs[0].page_content[0:500])
