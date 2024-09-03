from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.models import Filter, FieldCondition, MatchValue
from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd

df = pd.read_csv("C:/Users/ander.pascal/Desktop/SDG/SDG_Group-Prueba_tecnica-Innovation.csv")

client = QdrantClient(url="http://localhost:6333")

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")