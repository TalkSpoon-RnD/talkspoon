import os
import yaml

def create_directories(directories):
    for categories in directories:
        for category in categories.keys():
            category_path = "prompts/"+category.replace(' ', '_')
            os.makedirs(category_path, exist_ok=True)
            for subcategory in categories[category]:
                subcategory_path = os.path.join(category_path, subcategory.replace(' ', '_'))
                if not os.path.exists(subcategory_path) or not os.listdir(subcategory_path):
                    os.makedirs(subcategory_path+"/_posts")

with open('categories.yml', 'r') as f:
    directories = yaml.safe_load(f)
    create_directories(directories)