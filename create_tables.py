from models.models import Base, Item, Room, Estimate
from config.dependencies import engine


print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine)
