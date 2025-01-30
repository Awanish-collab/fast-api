from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Sample blog data (Each blog has an id and a title)
blogs = [
    {"id": 1, "title": "First Blog"},
    {"id": 2, "title": "Second Blog"},
    {"id": 3, "title": "Third Blog"},
    {"id": 4, "title": "Fourth Blog"},
    {"id": 5, "title": "Fifth Blog"},
    {"id": 6, "title": "Sixth Blog"},
    {"id": 7, "title": "Seventh Blog"},
    {"id": 8, "title": "Eighth Blog"},
    {"id": 9, "title": "Ninth Blog"},
    {"id": 10, "title": "Tenth Blog"},
]

@app.get("/blog")
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Filter out unpublished blogs (assuming all are published for now)
    filtered_blogs = blogs[:limit]

    # Apply sorting if requested
    if sort == "asc":
        sorted_blogs = sorted(filtered_blogs, key=lambda x: x["id"])
    elif sort == "desc":
        sorted_blogs = sorted(filtered_blogs, key=lambda x: x["id"], reverse=True)
    else:
        sorted_blogs = filtered_blogs  # No sorting applied

    return {"limit": limit, "published": published, "sort": sort, "blogs": sorted_blogs}
