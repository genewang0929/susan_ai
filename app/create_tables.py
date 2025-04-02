from models import Base, Item, Room, Estimate
from dependencies import engine


print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine)
